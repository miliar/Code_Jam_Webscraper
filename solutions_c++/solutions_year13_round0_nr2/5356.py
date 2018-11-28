//============================================================================
// Name        : CJam2.cpp
// Author      : Daniel Gomez
// Version     :
// Copyright   :
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <String.h>

using namespace std;

short prop [10][10];
short ordn [10][10];
short cesp [10][10];
int T, fil, col;

void copiar_prop();
void ver_orden();
void ordnar_ordn(char dir);
void ver_cesped();
void cesped_reset();
void corta_cesped(int h, int l, char dir);
bool comparar();


int main(void) {

	 ifstream myReadFile;
	 ofstream myWriteFile;

	 myReadFile.open("B-small-attempt1.in");
	 myWriteFile.open("B-small-attempt1.out");
	 if (myReadFile.is_open()) {
		 myReadFile >> T;
		 for(int i=0; i<T ; i++){
			 myReadFile >> fil;
			 myReadFile >> col;

			 //Lectura del mapa cuadriculado
			 for(int k=0; k < fil ; k++)
				 for(int l=0; l < col ; l++)
					 myReadFile >> prop[k][l];

			 //Ordenar y realiza el corte horizonal
			 cesped_reset();

			 copiar_prop();
			 ordnar_ordn('h');
			 for(int k=0; k < fil ; k++)
					 corta_cesped(ordn[k][0], k, 'h');

			 copiar_prop();
			 ordnar_ordn('v');
			 for(int l=0; l < col ; l++)
					 corta_cesped(ordn[0][l], l, 'v');

			 ver_cesped();

			 //Determinar si es posible
			 myWriteFile << "Case #"<< (i+1) <<": "<< (comparar()?"YES":"NO") <<" \n";
			 cesped_reset();
		 }
	}
	myReadFile.close();
	myWriteFile.close();


	system("pause");
	return EXIT_SUCCESS;
}

//Compara si el cesped propuesto es igual al cesped generado.
bool comparar(){
	for(int i=0; i<fil ; i++)
		for(int j=0; j<col ; j++)
			if(prop[i][j] != cesp[i][j])
				return false;
	return true;
}

void copiar_prop(){
	for(int i=0; i<fil ; i++){
		for(int j=0; j<col ; j++)
			ordn[i][j] = prop[i][j];
	}
}

void ver_orden(){
	for(int i=0; i<fil ; i++){
		for(int j=0; j<col ; j++)
			printf("%i ", ordn[i][j]);
		printf("\n");
	}
	printf("\n \n");
}

void ordnar_ordn(char dir){
 bool orden;
 int tmp;
	for(int k=0; k < (dir=='h'?fil:col) ; k++){
		orden = false;
		while(!orden){
			orden = true;
			for(int l=0; l < (dir=='h'?col-1:fil-1) ; l++){
				if(ordn[dir=='h'?k:l][dir=='h'?l:k] < ordn[dir=='h'?k:l+1][dir=='h'?l+1:k]){
					tmp = ordn[dir=='h'?k:l][dir=='h'?l:k];
					ordn[dir=='h'?k:l][dir=='h'?l:k] = ordn[dir=='h'?k:l+1][dir=='h'?l+1:k];
					ordn[dir=='h'?k:l+1][dir=='h'?l+1:k]= tmp;
					orden = false;
				}
			}
		}
	 }

}

//Inicializa el cesped a cortar
void cesped_reset(){
	for(int i=0; i<10 ; i++)
			for(int j=0; j<10 ; j++){
				cesp[i][j] = 100;
				ordn[i][j] = 100;
			}
}

void corta_cesped(int h, int l, char dir){
	if(dir == 'h')
		for(int i=0; i<col ; i++)
			if(h<100 && h<cesp[l][i]) cesp[l][i] = h;
	if(dir == 'v')
		for(int i=0; i<fil ; i++)
			if(h<100 && h<cesp[i][l]) cesp[i][l] = h;

}

void ver_cesped(){
	for(int i=0; i<fil ; i++){
		for(int j=0; j<col ; j++)
			printf("%i ", cesp[i][j]);
		printf("\n");
	}
	printf("\n \n");
}


