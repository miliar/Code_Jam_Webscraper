#include<stdio.h>

int result(int, int, int, int);
int compare(int, int);
int l(int);
int c(int);

char tab[4][4];

int main(){
	int i,j;
	int T, teste=1;

	scanf("%d%*c", &T);

	while(T--){
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%c", &tab[i][j]);
			}
			scanf("%*c");
		}
		scanf("%*c");//reads the empty line

		printf("Case #%d: ", teste++);

		if( result(0,1,2,3)==1 || result(4,5,6,7)==1 || result(8,9,10,11)==1 || result(12,13,14,15)==1 ||
			result(0,4,8,12)==1 || result(1,5,9,13)==1 || result(2,6,10,14)==1 || result(3,7,11,15)==1 ||
			result(0,5,10,15)==1 || result(3,6,9,12)==1){

			printf("X won\n");
			continue;	
		} 

		if( result(0,1,2,3)==-1 || result(4,5,6,7)==-1 || result(8,9,10,11)==-1 || result(12,13,14,15)==-1 ||
			result(0,4,8,12)==-1 || result(1,5,9,13)==-1 || result(2,6,10,14)==-1 || result(3,7,11,15)==-1 ||
			result(0,5,10,15)==-1 || result(3,6,9,12)==-1){

			printf("O won\n");
			continue;	
		}

		if( result(0,1,2,3)==-20 || result(4,5,6,7)==-20 || result(8,9,10,11)==-20 || result(12,13,14,15)==-20 ||
			result(0,4,8,12)==-20 || result(1,5,9,13)==-20 || result(2,6,10,14)==-20 || result(3,7,11,15)==-20 ||
			result(0,5,10,15)==-20 || result(3,6,9,12)==-20){

			printf("Game has not completed\n");
			continue;	
		}		

		printf("Draw\n");
	}

	return 0;
}

/*
Returns
0: draw
1: X wins
-1: O wins
-20: not completed yet
*/
int result(int a, int b, int c, int d){
	if(compare(a,b) + compare(b,c) + compare(c,d) == 3) return 1;
	else if(compare(a,b) + compare(b,c) + compare(c,d) == -3) return -1;
	else if(compare(a,b) + compare(b,c) + compare(c,d) <= -20) return -20;
	return 0;
}

/*
Returns
0: different
1: X match
-1: O match
-20: empty space
*/
int compare(int a, int b){
	char first = tab[l(a)][c(a)];
	char second = tab[l(b)][c(b)];

	if(first == '.' || second == '.') return -20;

	if(first == second || first == 'T' || second == 'T') {
		if(first == 'X' || second=='X') return 1;
		return -1;
	}
	return 0;
}

int l(int n){
	return n/4;
}

int c(int n){
	return n%4;
}