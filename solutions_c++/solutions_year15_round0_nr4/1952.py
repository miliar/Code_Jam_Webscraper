#include<stdio.h>

int p, T, X, R, C;

int main(){
	freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (p = 1; p <= T; p++){
		scanf("%d %d %d", &X, &R, &C);
		printf("Case #%d: ", p);
		if (X >= 7){
			printf("RICHARD\n");
			continue;
		}
		if (X == 1){
			printf("GABRIEL\n");
			continue;
		}
		if (X == 2){
			if ((R & 1) && (C & 1)){
				printf("RICHARD\n");
				continue;
			}
			else{
				printf("GABRIEL\n");
				continue;
			}
		}
		if (X == 3){
			if (((R % 3 == 0)&&C>=2) || ((C % 3 == 0)&&R>=2)){
				printf("GABRIEL\n");
				continue;
			}
			else{
				printf("RICHARD\n");
				continue;
			}
		}
		if (X == 4){
			if (((R % 4 == 0) && C >= 3) || ((C % 4 == 0) && R >= 3)){
				printf("GABRIEL\n");
				continue;
			}
			else{
				printf("RICHARD\n");
				continue;
			}
		}
	}
}