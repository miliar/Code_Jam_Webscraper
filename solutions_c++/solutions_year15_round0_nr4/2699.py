#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#define DEBUG 1

//Para Cualquier caso, si es X mayor a 7 siempre gana RICHARD
//Siempre puede escoger el caso donde ponga una figura semejante a la siguiente:
//
// 0 0 0
// 0   0
// 0 0 
//
// Donde va a quedar siempre un espacio en el medio.
// Si X < R || x < C Richard gana
// Si (R * C) % X != 0  Richard gana
// De cualquier otra forma, Gabriel gana
char evaluate(int X,int R, int C);

int main(){
	int T;
	int n_T=0;
	int X, R, C;
	char winner; 	//R = richard, G = Gabriel

	char c_num[10];

	fflush(stdin);
	gets(c_num);
	T = atoi(c_num);
	while(n_T < T){
		
		printf("Case #%d: ",n_T+1);
		scanf("%d %d %d\n",&X,&R,&C);
		winner = evaluate(X,R,C);
		if(winner == 'R'){
			printf("RICHARD");
		}
		else{
			printf("GABRIEL");
		}
		printf("\n");
		n_T ++;
	}
}

char evaluate(int X,int R, int C){
#ifdef DEBUG
	printf("X = %d, R = %d, C = %d\n",X,R,C);
#endif
	if((X > R && X > C) || (R*C)%X > 0 || X >= 7){
		return 'R';
	}
	if((X+1)/2 > R || (X+1)/2 > C){
		return 'R';
	}
	if(X > 3 && ((X+1)/2 == R || (X+1)/2 == C) ){
		return 'R';
	}

	return 'G';
}