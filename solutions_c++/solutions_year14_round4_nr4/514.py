#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;

const int M(9), N(5), L(11), MOD(1000000007);

int ca, m, n;
char s[M][L];
int g[M * L][26];
int cost[1 << M];
int f[N][1 << M], cnt[N][1 << M];

int main() {
	freopen("in.txt", "r", stdin);
	scanf("%d", &ca);
	for (int c = 1; c <= ca; ++c) {
		scanf("%d%d", &m, &n);
		for (int i = 0; i != m; ++i)
			scanf("%s", s[i]);
		for (int i = 1; i != (1 << m); ++i) {
			int si = 1;
			memset(g[1], 0, sizeof(g[1]));
			for (int j = 0; j != m; ++j)
				if (i & (1 << j)) {
					int p = 1;
					for (int k = 0; k != strlen(s[j]); ++k) {
						if (!g[p][s[j][k] - 'A']) {
							++si;
							memset(g[si], 0, sizeof(g[si]));
							g[p][s[j][k] - 'A'] = si;
						}
						p = g[p][s[j][k] - 'A'];
					}
				}
			cost[i] = si;
		}
		memset(f, 0, sizeof(f));
		memset(cnt, 0, sizeof(cnt));
		cnt[0][0] = 1;
		for (int i = 0; i != n; ++i) {
			for (int j = 0; j != (1 << m); ++j) {
				int mask = ((1 << m) - 1) ^ j;
				for (int k = mask; k; k = (k - 1) & mask) {
					if (f[i + 1][j | k] > f[i][j] + cost[k]) continue;
					if (f[i + 1][j | k] < f[i][j] + cost[k]) {
						f[i + 1][j | k] = f[i][j] + cost[k];
						cnt[i + 1][j | k] = 0;
					}
					cnt[i + 1][j | k] = (cnt[i + 1][j | k] + cnt[i][j]) % MOD;
				}
			}
		}
		printf("Case #%d: %d %d\n", c, f[n][(1 << m) - 1], cnt[n][(1 << m) - 1]);
	}
	return 0;
}