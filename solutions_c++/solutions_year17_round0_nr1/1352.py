#include"stdio.h"
int T, t, N, M, K, A[3000];
char S[3000];
int main() {
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%s%d", S, &K);
		for (M = 0; S[M]; M++)
			A[M] = 0;
		N = 0;
		for (int i = 0; i < M; i++) {
			int z = (S[i] == '+')? 1: 0;
			if (A[i] ^ z == 0) {
				N++;
				A[i] ^= 1;
				A[i+K] ^= 1;
				if (i > M - K)
					N = -9999;
			}
			A[i+1] ^= A[i];
		}
		printf("Case #%d: ", t);	
		if (N < 0) printf("IMPOSSIBLE\n");
		else printf("%d\n", N);
	}
}
