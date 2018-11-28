#include <stdio.h>
#include <stdlib.h>


int main(){
	double nao[1000], ken[1000];
	int N;

	int i, j, k;
	int cas;
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w", stdout);
	
	scanf("%d", &cas);


	for (k=1; k<=cas; k++){
		scanf("%d", &N);
		for (i=0; i<N; i++){
			scanf("%lf", &nao[i]);
		}
		for (i=0; i<N; i++){
			scanf("%lf", &ken[i]);
		}
		
		for (i=0; i<N; i++){
			for (j=0; j<N; j++){
				if (nao[i] < nao[j]){
					double temp = nao[i];
					nao[i] = nao[j];
					nao[j] = temp;
				}
			}
		}

		//qsort(ken, N, sizeof(double), cmp);

		for (i=0; i<N; i++){
			for (j=0; j<N; j++){
				if (ken[i] < ken[j]){
					double temp = ken[i];
					ken[i] = ken[j];
					ken[j] = temp;
				}
			}
		}
	
		int s=0, t=0;
		int bwin=0;

		while(1){
			if (t >= N) break;
			if (nao[s] < ken[t]){
				bwin++;
				s++;
				t++;
			}else{
				t++;
			}
		}
		s=0, t=0;
		int awin=0;

		while(1){
			if (t >= N) break;
			if (ken[s] < nao[t]){
				awin++;
				s++;
				t++;
			}else{
				t++;
			}
		}
		
		printf("Case #%d: %d %d\n", k, awin , N-bwin );
	}

	return 0;
}