/*
 * LawnMower.cpp
 *
 *  Created on: 13/04/2013
 *      Author: Tomás
 */

#include <fstream>
#include <string>
#include <iostream>
using namespace std;

int main(){
	ifstream input("lm.in");
	ofstream output("lm.out");
	int T, caso, N, M, fila, columna, cuadrado;
	int maxCol[100],maxFil[100],campo[100][100];
	bool esPosible;

	input >> T;
	for (caso = 1; caso <= T; caso ++){
		input >> N >> M;
		esPosible = true;

		//inicio los maximos en un valor mayor al que pueden tomar.
		for (int i = 0; i < N; i ++){
			maxFil[i] = -5;
		}
		for (int i = 0; i < M; i ++){
			maxCol[i] = -5;
		}


		//calculo simultáneamente mínimos.
		for (fila = 0; fila < N; fila ++){
			for (columna = 0; columna < M; columna ++){
				input >> cuadrado;
				if (cuadrado > maxFil[fila]){
					maxFil[fila] = cuadrado;
				}
				if (cuadrado > maxCol[columna]){
					maxCol[columna] = cuadrado;
				}
				campo[fila][columna] = cuadrado;
			}
		}
		/* chequeo que para cada fila si un cuadrado es menor al maximo entonces
		 * para ser posible ese cuadrado debe ser menor al maximo de la columna.
		 * seria un golazo hacerlo simultaneamente con las columnas.*/

		for (fila = 0; fila < N; fila ++){
			for (columna = 0; columna < M; columna ++){
				cuadrado = campo[fila][columna];
				if ((cuadrado < maxFil[fila])  && (cuadrado < maxCol[columna])){
						esPosible = false;
				}
			}
		}

		if (esPosible){
			output << "Case #" << caso<< ": YES" << endl;
		} else {
			output << "Case #" << caso<< ": NO" << endl;
		}

	}

	return 0;
}
