#include <stdio.h>

long long ONE = 1;

int main(void){
	int t, T, N;
	long long P, A, B;
	long long tmp;
	int i;

	scanf("%d", &T);
	for (t=1; t<=T; t++){
		scanf("%d%lld", &N, &P);
		if (P==(ONE<<N)){
			printf("Case #%d: %lld %lld\n", t, P-1, P-1);
			continue;
		}

		A = 1; tmp = (ONE<<N)/2;
		for (i=N-2; i>=0; i--){
			if (tmp>=P) break;
			tmp += (ONE<<i);
			A = A*2+1;
		}
		A --;

		B = (ONE<<N)-1; tmp = (ONE<<N)/2;
		for (i=1; i<N; i++){
			if (tmp<=P) break;
			B -= (ONE<<i);
			tmp /= 2;
		}
		B --;

		printf("Case #%d: %lld %lld\n", t, A, B);
	}
}

