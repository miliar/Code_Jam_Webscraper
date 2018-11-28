#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

char num[10000];
int A[10000];
int main() {
	
	int T, t, i, j, Smax, N, added;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	
	for(t=0;t<T;t++) {
		scanf("%d %s", &Smax, num);
		N = 1;
		added = 0;
		A[0] = (num[0] - '0');
		for(i=1;num[i];i++) {
			A[i] = A[i-1] + (num[i] - '0');	
			N++;
		}
		//for(i=0;i<N;i++) printf("%d+", A[i]); printf("|\n");
		for(i=N-1;i>=1;i--) {
			int dif = i - (A[i-1]+added);
			if(dif <= 0) continue;
			added += dif;
			//printf("%d %d\n", i, dif);		
		}
		printf("Case #%d: %d\n", t+1, added);
	}

	return 0;
}
