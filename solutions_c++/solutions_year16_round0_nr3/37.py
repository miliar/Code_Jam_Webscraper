#include <cstdio>

typedef long long i64;

int T;
int N, J;

int count_even(i64 n)
{
	int ret = 0;
	for (int i = 1; i < 32; i += 2) if (1 & (n >> i)) ++ret;
	return ret;
}

int main()
{
	scanf("%d", &T);
	for (int t = 0; t++ < T; ) {
		scanf("%d%d", &N, &J);
		printf("Case #%d:\n", t);
		for (i64 i = (1LL << (i64)(N - 1)) + 1; i < (1LL << (i64)N); i += 2) {
			if (__builtin_popcountll(i) == 2 * count_even(i)) {
				for (int j = N - 1; j >= 0; --j) {
					printf("%d", (int)(1 & (i >> j)));
				}
				printf(" 3 4 5 6 7 8 9 10 11\n");
				if (--J == 0) break;
			}
		}
		if (J != 0) fprintf(stderr, "%d\n", J);
	}
	return 0;
}
