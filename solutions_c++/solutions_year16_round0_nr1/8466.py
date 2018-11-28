#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

// Leemos el numero de casos
int N;

int start;

bool discover[10];
int numDiscover;

int GetNewDigits(int num){
	int reg = 0;
	int aux;
	while (num != 0){
		aux = num % 10;
		if (!discover[aux]){
			discover[aux] = true;
			reg++;
		}
		num /= 10;
	}
	return reg;
}

int main(){
	int auxCount;
	scanf("%d", &N);
	for (int i = 0; i < N; i++){
		// Leemos en que numero empieza la oveja
		scanf("%d", &start);
		if (start != 0){
			numDiscover += GetNewDigits(start);
			auxCount = start;
			while (numDiscover != 10){
				auxCount += start;
				numDiscover += GetNewDigits(auxCount);				
			}
			printf("Case #%d: %d\n", i + 1, auxCount);
			// Inicializamos los valores
			for (int j = 0; j < 10; j++){
				discover[j] = false;
			}
			numDiscover = 0;
		}else{
			printf("Case #%d: INSOMNIA\n", i + 1);
		}
	}

	return 0;
}