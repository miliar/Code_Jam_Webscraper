#include <stdio.h>
#include <stdlib.h>

int N;

int tam;
char pancakes[100];

int main(){
	char aux;
	char state;
	int auxPosc;
	int movtos;
	// Lee mos el numero de casos
	scanf("%d ", &N);
	for (int i = 0; i < N; i++){
		tam = 0;
		movtos = 0;
		// Leemos el caso
		scanf("%c", &aux);
		while (aux != 10){
			pancakes[tam ++] = aux;
			scanf("%c", &aux);
		}
		// Procesamos la cadena
		state = pancakes[0];
		auxPosc = 1;
		while (auxPosc < tam){
			if (pancakes[auxPosc] != state){
				state = state == '-' ? '+' : '-';
				movtos++;
			}
			auxPosc++;
		}
		if (state == '-')
			movtos++;
		printf("Case #%d: %d\n", i + 1, movtos);
	}
	return 0;
}