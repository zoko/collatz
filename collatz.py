# -*- coding: UTF-8 -*-
# programa para el cálculo de la serie de collatz
# Vamos ha hacer la versión del programa en modo gráfico

# Importamos los módulos gráficos necesarios
import gtk
import gtk.glade

# Fucion para calcular la conjetura de collatz
# de la wikipedia pero vale para practicar
# el siguiente paso es ordenar la serie

def collatz(n):
    # calcula la función de collatz y la mete en una lista.
        result = [n]
        while n > 1:
                if (n % 2) == 0:
                        n = n/2
                else:
                        n = n*3 + 1             
                result.append(n)
        return result #en lugar de print usamos return porque hay que mostrarlo en un widget gtk2

def imprimir():
    # le vamos a pasar los datos de la función collatz y los vamos a presentar por pantalla.
    pass

# Creamos una clase que almacena la informacion del programa (despues se usara)
class Info:
    """clase donde se guarda la info del programa"""
    name = "Collatz"
    version = "0.1"
    copyright = "Copyright 2013 Zoko."
    authors = ["Zoko <zokoster @ gmail com>"]
    website = "http://zoko.tumblr.com"
    description = "A Collatz conjeture calculator written in python using PyGTK"
    license = "This program is free software; you can redistribute it and/or \
modify it under the terms of the GNU General Public License as published by \
the Free Software Foundation; either version 2 of the License, or (at your \
option) any later version. \n\nThis program is distributed in the hope that \
it will be useful, but WITHOUT ANY WARRANTY; without even the implied \
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. \
See the GNU General Public License for more details. \n\nYou should have \
received a copy of the GNU General Public License along with this program; \
if not, write to the Free Software Foundation, Inc., 51 Franklin Street, \
Fifth Floor, Boston, MA 02110-1301, USA."

class Collatz:
	
	def gtk_main_quit(self, widget, data=None):
		
		gtk.main_quit()
		return False
    


	# Primero definimos la ventana y la dibujamos.
	def __init__(self):
		builder = gtk.Builder()
		builder.add_from_file("collatz.glade")
		self.window = builder.get_object("window1")
		builder.connect_signals(self)
		self.window.show()

		# Del archivo glade tenemos que obtener los objetos / widgets
		# que vamos a necesitar
		self.entry1 = builder.get_object("entry1")
		self.textview1 = builder.get_object("textview1")


	# Definimos las acciones al hacer click en aceptar
	def on_button1_clicked(self, widget):
		'''función que define lo que pasa cuando hacemos click en aceptar'''

		# Se crea un buffer en donde se guardaran los resultados
		text_buffer = gtk.TextBuffer()
		# Se obtiene el valor para convertir desde la entrada
		valor = self.entry1.get_text()
		# Intenta transformar el valor ingresado en un numero. En caso
		# de fallar (por ejemplo falla si lo ingresado son letras) se
		# lanza la excepcion, si es exitoso se continua con la conversion
		temp_ini = int(valor)
		
		# Funciona pero no nos muestra el resultado en el textview1 :(
		resultado = collatz(temp_ini)

		text_buffer.set_text(str(resultado))
		self.textview1.set_buffer(text_buffer)

	# Definimos las acciones al pulsar intro
	def on_entry1_activate(self, widget):
		'''función que define lo que pasa cuando pulsamos intro en el cuadro de entrada'''

		# Se crea un buffer en donde se guardaran los resultados
		text_buffer = gtk.TextBuffer()
		# Se obtiene el valor para convertir desde la entrada
		valor = self.entry1.get_text()
		# Intenta transformar el valor ingresado en un numero. En caso
		# de fallar (por ejemplo falla si lo ingresado son letras) se
		# lanza la excepcion, si es exitoso se continua con la conversion
		temp_ini = int(valor)
		
		# Funciona pero no nos muestra el resultado en el textview1 :(
		resultado = collatz(temp_ini)

		text_buffer.set_text(str(resultado))
		self.textview1.set_buffer(text_buffer)
   
def main():
    gtk.main()

if __name__=='__main__':
    h = Collatz()
    main()