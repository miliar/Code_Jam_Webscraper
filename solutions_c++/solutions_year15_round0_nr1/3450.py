#include <fstream>
#include <iostream>
#include <string>
#include <stdlib.h>  
using namespace std;
int main(int argc, char* argv[]){
	/*Here goes parameters file*/
	ifstream archivo_entrada("A-large.in", std::ios_base::in);
	ofstream archivo_salida;
	/*Here is declare output file*/
	archivo_salida.open("salidainstancias");
	 int t =0;
	archivo_entrada>>t;
	
	for(unsigned int j = 0; j < t; j++){
		 int smax;
		archivo_entrada>>smax;
		string Vchar;
		archivo_entrada >> Vchar;
		 
		  int V[smax+1];
		for(unsigned int w = 0; w < smax+1; w++){
			V[w] = Vchar.at(w) -48;
		}
		unsigned int parados = 0;
		unsigned int agregados = 0;
		if(V[0] == 0){
			V[0] = 1;
			agregados++;
		}

		parados = V[0];

	
		for(int i = 1; i <  smax+1; i++){
			/*Si hay alguna persona con i miedo sentada, y los parados hasta ahora son menores que i*/
			if(V[i] != 0){
				 if(parados < i){
					/*Agrego los que faltan para que se paren las personas con i miedo*/
					agregados += (i - parados);
					/*Logré que se paren todos los de V[i], cumplí su deshinibición, y además, tengo parados también los que agregué*/
					parados += ((i - parados) + V[i]);
				}else{
					parados += V[i];
				}
			}
	
		}
	
		archivo_salida<<"Case #" << j+1<<": "<<agregados<<endl;
		}	
}
