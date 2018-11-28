#include <stdio.h>


int T;
int S, K, C;
long long base[200];

int min(int a, int b)
{
	return (a>b)?b:a;
}

void solve()
{
	base[1] = 1;
	for (int i = 2; i <= C; i++)
		base[i] = base[i-1] * K;
	for (int i = 1; i <= K; i += C) {
		long long idx = min(i+C-1, K);
		for (int j = C, k = i; j >= 2; j--, k++) {
			k = min(k,K);
			idx += base[j] * (k-1);
		}
		printf(" %lld", idx);
	}
	puts("");
}

int main()
{
	scanf(" %d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf(" %d %d %d", &K, &C, &S);
		printf("Case #%d:", cas);
		if (S*C >= K)	solve();
		else			puts(" IMPOSSIBLE");
	}

	return 0;
}