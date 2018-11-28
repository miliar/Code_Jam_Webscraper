#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	FILE *fin, *fout;
	int i, j, k,l;
	int T;
	int w, h;
	char flag, f1, f2;
	int lawn[101][101];
	fin = fopen("B.in", "r");
	fout = fopen("B.out", "w+");
	
	fscanf(fin, "%d", &T);
	for(i = 1; i <= T; i++) {
		fscanf(fin, "%d%d", &w, &h);
		for(j=1; j<=w; j++) {
			for(k=1; k<=h; k++) {
				fscanf(fin, "%d", &lawn[j][k]);
			}
		}
		flag = true;
		for(j=1;flag&&j<=w;j++) {
			for(k=1;flag&&k<=h;k++) {
				f1 = true;
				f2 = true;
				for(l=1;l<=w;l++) {
					if(lawn[l][k]>lawn[j][k]) {
						f1 = false;
						break;
					}
				}
				for(l=1;l<=h;l++) {
					if(lawn[j][l]>lawn[j][k]) {
						f2 = false;
						break;
					}
				}
				flag = f1 || f2;
			}
		}
		fprintf(fout, "Case #%d: ", i);
		if(flag) {
			fprintf(fout, "YES\n");
		}
		else {
			fprintf(fout, "NO\n");
		}
	}
	fclose(fin);
	fclose(fout);
	return 0;
}
