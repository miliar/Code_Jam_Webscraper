#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

ifstream fin ("Mgtr.in");
ofstream fout ("Magic-trick.out");

int main(){	
	//lee numero de casos
	int T = 0;
	fin >> T;
	
	//respuestas del voluntario
	int v1 = 0, v2 = 0;
	//cuadrado de cartas
	int cartas1[4];
	int cartas2[4];
	int a;
	
	//cada caso de prueba
	for(int t=0; t<T; t++){
		
		fin >> v1;
		v1--;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(i==v1){
				//si se para en la fila elegida por el voluntario guarda esa fila en cartas1[]
					fin >> cartas1[j];
				}else
					fin >> a;
			}
		}
		
		fin >> v2;
		v2--;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(i==v2){
				//si se para en la fila elegida por el voluntario guarda esa fila en cartas2[]
					fin >> cartas2[j];
				}else
					fin >> a;
			}
			
				
		}
		
		//busca los numeros que coincidan en lo elegido por el voluntario
		//numero del voluntario
		int num = 0;
		//contador de numeros posibles
		int contador=0;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(cartas1[i]==cartas2[j]){
					contador++;
					num=cartas1[i];
				}
			}
		}
		
		if(contador==0)fout << "Case #" << t+1 << ": Volunteer cheated!" << endl;
		if(contador>1)fout << "Case #" << t+1 << ": Bad magician!" << endl;
		if(contador==1)fout << "Case #" << t+1 << ": " << num << endl;
	}
	
	
	return 0;
}
