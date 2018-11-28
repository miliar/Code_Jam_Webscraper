// GCJ.cpp : Defines the entry point for the console application.
//

#include "stdio.h"

int main(){

	int numCasos;
	int resposta1;
	int numeros1[4][4];
	int resposta2;
	int numeros2[4][4];

	int resultado = 0;
	int resultadoNum = 0;

	scanf("%d", &numCasos);
	
	for(int i = 0; i < numCasos; i++){
		resultado = 0;
		
		scanf("%d", &resposta1);
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				int aux;
				scanf("%d", &aux);
				numeros1[i][j] = aux;
			}	
		}

		scanf("%d", &resposta2);
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				int aux;
				scanf("%d", &aux);
				numeros2[i][j] = aux;
			}	
		}

		resposta1--;
		resposta2--;
		
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(numeros1[resposta1][i] == numeros2[resposta2][j]){
					resultado++;
					resultadoNum = numeros1[resposta1][i];
				}
			}
		}
		if(resultado == 1){
			printf("Case #%d: %d\n", i + 1, resultadoNum);
		}
		else if(resultado > 1){
			printf("Case #%d: Bad magician!\n", i + 1);
		}
		else{
			printf("Case #%d: Volunteer cheated!\n", i + 1);
		}
	}
	return 0;
}

