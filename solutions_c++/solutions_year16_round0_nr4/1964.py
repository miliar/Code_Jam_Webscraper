#include <cstdio>

int casei, cases;
long long K, C, S;

int main() {
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%lld%lld%lld", &K, &C, &S);
		printf("Case #%d:", casei);
		long long N = (K - 1) / C + 1;
		if (N > S) {
			printf(" IMPOSSIBLE\n");
			continue;
		}
		long long num = 0LL;
		for (long long i = 0LL, j = 0LL; i < K; ++i) {
			num = num * K + i;
			if (++j == C) {
				j = 0LL;
				--N;
				printf(" %lld", num + 1);
				num = 0;
			}
		}
		if (N > 0) printf(" %lld", num + 1);
		printf("\n");
	}
	return 0;
}
