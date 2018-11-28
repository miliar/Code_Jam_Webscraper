#include <stdio.h>
#include <stdlib.h>


int main(){

	int cnt;
	FILE *fi = fopen("A-large.in-2.txt", "r");
	FILE *fo = fopen("output.txt", "w");
	fscanf(fi,"%d", &cnt);

	for (int i = 0; i < cnt; i++){
		int n;
		fscanf(fi,"%d", &n);
		int chk[10] = { 0, };
		int tmp;
		int end = 0;
		for (int j = 1; j <= 100; j++){
			tmp = j*n;
			while (tmp > 0){
				chk[tmp % 10]++;
				tmp /= 10;
			}
			for (int k = 0; k < 10; k++){
				if (chk[k] == 0){
					break;
				}
				if (k == 9){
					fprintf(fo,"Case #%d: %d\n", i + 1, j*n);
					end = 1;
					break;
				}
			}
			if (end == 1)
				break;
			
		}
		for (int j = 0; j < 10; j++){
			if (chk[j]>0)
				break;
			if (j==9){
				fprintf(fo,"Case #%d: INSOMNIA\n",i+1);
			}
		}


	}
	return 0;
}