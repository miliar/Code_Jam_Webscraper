#include <stdio.h>
#include <stdlib.h>

int main(){

	FILE *fi = fopen("A-large (1).in", "r");
	FILE *fo = fopen("output.txt", "w");
	int T;
	int shy;

	fscanf(fi,"%d", &T);
	for (int i = 1; i <= T; i++){
		int fr = 0;
		int stk = 0, h;
		char aud;
		fscanf(fi,"%d", &shy);
		for (int j = 0; j <= shy; j++){
			fscanf(fi," %c", &aud);
			h = (int)aud - (int)'1'+1;
			if (h < 0)
				h = 0;
			if (j == 0){
				stk += h;
				continue;
			}
			
			if (stk < j){
				fr += j - stk;
				stk += j - stk;
			}
			stk += h;
				
		}
		fprintf(fo,"Case #%d: %d\n",i,fr);
	}
	return 0;
}