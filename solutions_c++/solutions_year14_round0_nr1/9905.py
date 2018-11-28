// A.cpp: define el punto de entrada de la aplicación de consola.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int _tmain(int argc, _TCHAR* argv[]){

	//Input file
	ifstream cin("A-small-attempt0.in");
	ofstream cout("A-small.out");
	//Create number test cases
	int N, R1, R2, M1[4][4],M2[4][4],count,index;
	string respuesta;
	char buffer[3];

	cin >> N;
	for(int i=0; i<N; i++){
		//R1: fila en la baraja donde esta la carta numerada
		cin >> R1;
		//M1: Baraja1
		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
				cin >> M1[j][k];
		//R2: fila en la baraja donde esta la carta numerada
		cin >> R2;
		//M1: Baraja2
		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
				cin >> M2[j][k];

		count = 0;
		respuesta = "Volunteer cheated!";
		//Contar cuantas coincidencias hay entre la fila de la baraja1 y la fila de la baraja 2
		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
				if(M1[R1-1][j] == M2[R2-1][k]){
					count++;
					itoa (M1[R1-1][j],buffer,10);
					if(count==1) respuesta = buffer;
				}
		if(count > 1) respuesta = "Bad magician!";

		cout << "Case #" << (i+1) << ": " << respuesta <<"\n";
	}

	system("pause");
	return 0;
}

