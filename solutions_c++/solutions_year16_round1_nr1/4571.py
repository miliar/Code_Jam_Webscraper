#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>

int getBefore(int posc){
	if ((posc - 1) < 0)
		return 15;
	return posc - 1;
}

int getNext(int posc){
	if (posc + 1 < 16)
		return posc + 1;
	return 0;
}

char buffer[16];

int main(){
	int ini;
	int fin;
	int N;
	char aux;
	scanf("%d ", &N);
	for (int i = 0; i < N; i++){
		ini = 0;
		fin = 1;
		scanf("%c", &aux);
		buffer[0] = aux;
		while (aux != '\n'){
			scanf("%c", &aux);
			if (aux >= buffer[ini]){
				buffer[getBefore(ini)] = aux;
				ini = getBefore(ini);
			}
			else{
				buffer[fin++] = aux;
			}
		}
		printf("Case #%d: ", i + 1);
		while (ini != getBefore(fin)){
			printf("%c", buffer[ini]);
			ini = getNext(ini);
		}
		printf("\n");
	}
	return 0;
}