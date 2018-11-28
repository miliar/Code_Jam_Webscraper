// Round 1B Problem B
#include <stdio.h>
#define FOR(var, __n) for(int _##var = 0; _##var < __n; _##var++)

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int nCase;
	int A, B, K;
	int res;

	scanf("%d", &nCase);
	
	for (int n = 1; n <= nCase; n++) {
		res = 0;
		scanf("%d %d %d", &A, &B, &K);

		FOR (j, A) FOR (k, B) if ((_j & _k) < K)
			res++;

		printf("Case #%d: %d\n", n, res);
	}

	return 0;
}