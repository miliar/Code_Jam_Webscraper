#include <stdio.h>

int T, N, M;
int i, j, k;
int a[100][100];
int rMax[100];
int cMax[100];



void process(){
	int cas;
	FILE *fip, *fop;
	fip = fopen("input.txt", "r");
	fop = fopen("output.txt", "w");

	fscanf(fip, "%d", &T);

	for (k=0; k<T; k++){
		fscanf(fip, "%d %d", &N, &M);

		cas = 0;

		for (i=0; i<N; i++){
			for (j=0; j<M; j++){
				fscanf(fip, "%d", &a[i][j]);
			}
		}

		for (i=0; i<N; i++){
			rMax[i]=0;
			for (j=0; j<M; j++){
				if (rMax[i] < a[i][j]){
					rMax[i] = a[i][j];
				}
			}
		}

		for (i=0; i<M; i++){
			cMax[i]=0;
			for (j=0; j<N; j++){
				if (cMax[i] < a[j][i]){
					cMax[i] = a[j][i];
				}
			}
		}


		for (i=0; i<N; i++){
			for (j=0; j<M; j++){
				if ((a[i][j] < rMax[i]) && (a[i][j] < cMax[j])){
					cas = 1;
					break;
				}
			}
			if (cas ==1) break;
		}


		if (cas == 0) fprintf(fop, "Case #%d: YES\n", k+1);
		else fprintf(fop, "Case #%d: NO\n", k+1);
	}
}

int main(){
	process();
	return 0;
}



