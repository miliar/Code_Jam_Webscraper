#include <fstream>
#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;
int main(int argc, char* argv[]){
	/*Here goes parameters file*/
	ifstream archivo_entrada("B-large.in", std::ios_base::in);
	ofstream archivo_salida;
	/*Here is declare output file*/
	archivo_salida.open("salidainstancias");
	int t = 0;
	archivo_entrada>>t;
	
	/*Por cada instancia*/
	for(unsigned int j = 0; j < t; j++){
		unsigned int cantidadComenzales;
		archivo_entrada >> cantidadComenzales;

		double comenzales[cantidadComenzales];
		double maximosPancakes = 0; 
		for(unsigned int w = 0; w < cantidadComenzales; w++){
			archivo_entrada >>comenzales[w];
			maximosPancakes = max(comenzales[w],maximosPancakes);
		}	

		
		double solucionMinimaMinutos = maximosPancakes;
		double solucionMinutosMagicos = 0;
		
		for(unsigned int i = maximosPancakes; i > 0  ; i--){

				double minutosNecesariosSinMover = i;
				double minutosMagicosActuales = 0;

				for(int j = 0; j < cantidadComenzales; j++){
					if(comenzales[j]>minutosNecesariosSinMover){
						minutosMagicosActuales += (ceil(comenzales[j]/minutosNecesariosSinMover) - 1);

					}
				}

				if(solucionMinimaMinutos + solucionMinutosMagicos > minutosNecesariosSinMover + minutosMagicosActuales){
					solucionMinimaMinutos = minutosNecesariosSinMover;
					solucionMinutosMagicos = minutosMagicosActuales;
				}
			}
		

	/*Tomo la solucion final*/
	archivo_salida<<"Case #" << j+1 <<": "<<solucionMinimaMinutos + solucionMinutosMagicos<<endl;
	}
}