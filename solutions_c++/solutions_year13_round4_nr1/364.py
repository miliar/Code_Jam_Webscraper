#include <stdio.h>
#include <string.h>
#include <algorithm>

long long n;
int m;
const int MAXM = 1000;
const long long MOD = 1000002013;
long long o[MAXM], e[MAXM], p[MAXM];
long long *ref[MAXM * 2];
int tot;
long long x[MAXM * 2];
long long c[MAXM * 2];
long long s1, s2;

void init()
{
	s1 = s2 = 0;
	memset(c, 0, sizeof(c));
	scanf("%lld%d", &n, &m);
	for (int i = 0; i < m; ++i) {
		scanf("%lld%lld%lld", &o[i], &e[i], &p[i]);
		long long d = e[i] - o[i];
		s1 += (2 * n - d + 1) * d / 2 % MOD * p[i] % MOD;
		s1 %= MOD;
		ref[i + i] = &e[i]; ref[i + i + 1] = &o[i];
	}
	// printf("%d\n", s1);
	std::sort(ref, ref + m + m, [](long long *a, long long *b) { return *a < *b; });
	int k = 0; x[0] = *ref[0]; *ref[0] = 0;
	for (int i = 1; i < m + m; ++i) {
		if (*ref[i] == x[k]) *ref[i] = k;
		else x[++k] = *ref[i], *ref[i] = k;
	}
	tot = k + 1;

	for (int i = 0; i < m; ++i) {
		for (int j = o[i]; j < e[i]; ++j) c[j] += p[i];
	}
}

void solve()
{
	for (;;) {
		int i = 0;
		while (i < tot && !c[i]) ++i;
		if (i >= tot) break;
		int j = i;
		long long k = c[i];
		while (j < tot && c[j]) k = std::min(k, c[j++]);
		long long d = x[j] - x[i];
		s2 += (2 * n - d + 1) * d / 2 % MOD * k % MOD;
		s2 %= MOD;
		while (i < j) c[i++] -= k;
		// printf("%d %d %d\n", i, j - 1, s2);
	}
}

int main()
{
	int dat;
	scanf("%d", &dat);
	for (int k = 1; k <= dat; ++k) {
		init();
		solve();
		printf("Case #%d: %lld\n", k, (s1 - s2 + MOD) % MOD);
	}
}
