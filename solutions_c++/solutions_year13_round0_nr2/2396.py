#include "stdio.h"

int main() {
	int num, i,j,k;

	int r,c;
	int b[100][100];
	int rm[100], cm[100];
	FILE *fp, *fp2;

	bool ans;

	fp = fopen("B-large.in", "r");
	fp2 = fopen("B-large-sol.in", "w");
	fscanf(fp, "%d", &num);
	for(i=0; i<num; ++i) {
		ans=true;
		fprintf(fp2,"Case #%d: ",i+1);
		fscanf(fp,"%d %d", &r,&c);
		for(j=0;j<r;++j) {
			rm[j]=0;
			for(k=0;k<c;++k) {
				fscanf(fp, "%d", &b[j][k]);
				if(b[j][k]>rm[j]) rm[j]=b[j][k];
			}
		}

		for(j=0;j<c;++j) {
			cm[j]=0;
			for(k=0;k<r;++k)
				if(b[k][j]>cm[j]) cm[j]=b[k][j];
		}

		for(j=0;j<r;++j) {
			for(k=0;k<c;++k) {
				if(b[j][k]<cm[k] && b[j][k]<rm[j]){
					ans=false;
					break;
				}
			}
			if(!ans) break;
		}

		if(ans) fprintf(fp2, "YES\n");
		else fprintf(fp2, "NO\n");
	}

	fclose(fp);
	fclose(fp2);
	return 0;
}
