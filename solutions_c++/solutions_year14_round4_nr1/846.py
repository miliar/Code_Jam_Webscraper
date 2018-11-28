#include "stdio.h"
#include <algorithm>

int main(){
	int discs[10001];
	int T, Ti, N, X, i, pj, j, x, used, ndisc, before;
	scanf("%d", &T);
	for(Ti=1; Ti<=T; Ti++){
		used = 0;
		scanf("%d %d", &N, &X);
		ndisc = N;
		for(i=0; i<N; i++) scanf("%d", &(discs[i]));
		std::sort(discs, discs+N);
		for(i=0; i<N/2; i++){
			x = discs[i];
			discs[i] = discs[N-1-i];
			discs[N-1-i] = x;
		}
		before = -1;
		for(i=0, j=N-1; i<N; i++){
			if(discs[i] < 0) continue;
			if(before == -1) before = j;
			for(pj=j=before, before=-1; j>i; j--){
				if(discs[j] < 0) continue;
				if(discs[i] + discs[j] > X) break;
				if(discs[j] != discs[pj]) pj = j;
				if(before == -1) before = j;
			}
			if(j<=i){
				used += (ndisc+1)/2;
				break;
			}
			used++; ndisc--;
			if(discs[pj] >= 0 && discs[i] + discs[pj] <= X){
				// printf("%d %d\n", discs[i], pj);
				ndisc--; discs[pj] = -1; j = pj-1;
			}
		}
		printf("Case #%d: %d\n", Ti, used);
	}
	return 0;
}
