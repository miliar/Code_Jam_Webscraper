#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef long double LD;
const int maxint = 0x7f7f7f7f, mod = 1000000007;
const double eps = 1e-8, pi = acos(-1.0);

void rd() { }
template<typename... T> void rd(int &h, T &... t) { scanf("%d", &h); rd(t...); }
template<typename... T> void rd(long long &h, T &... t) { scanf("%lld", &h); rd(t...); }
template<typename... T> void rd(double &h, T &... t) { scanf("%lf", &h); rd(t...); }

const int maxn = 101 + 10;
int tests, n, p, q, h[maxn], g[maxn], w1[maxn], w2[maxn]; // direct, indirect kill
int dp[maxn][1001][2], need[maxn], need2[maxn];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	rd(tests);
	for (int tt = 1; tt <= tests; ++tt) {
		rd(p, q, n);
		for (int i = 1; i <= n; ++i) {
			rd(h[i], g[i]);
			w1[i] = h[i] / p + 1;
			if (h[i] % p == 0) --w1[i];
			need[i] = h[i] / q + 1;
			if (h[i] % q == 0) --need[i];
			int tmp = h[i], cnt = 0, us;
			while (tmp > q) {
				tmp -= q;
				++cnt;
			}
			us = tmp / p + 1;
			if (tmp % p == 0) --us;
			w2[i] = us;
			need2[i] = cnt;
		}
		memset(dp, 0x80, sizeof(dp));
		dp[0][1][0] = 0;
		for (int i = 0; i < n; ++i) {
			for (int extra = 0; extra <= 1000; ++extra) {
				for (int last = 0; last <= 1; ++last) { // last = 0, killed by tower
					if (dp[i][extra][last] < 0) continue;
					if (0 == 0) { // give up
						int &v = dp[i + 1][extra + need[i + 1]][0];
						v = max(v, dp[i][extra][last]);
					}
					if (extra >= w1[i + 1]) { // 
						int &v = dp[i + 1][extra - w1[i + 1]][1];
						v = max(v, dp[i][extra][last] + g[i + 1]);
					}
					//if (last == 1 && rem[i + 1] <= q && h[i + 1] <= q) continue;
					int towert = need2[i + 1];
					if (extra + towert >= w2[i + 1]) {
						int nturn = extra + towert - w2[i + 1];
						int &v = dp[i + 1][nturn][1];
						v = max(v, dp[i][extra][last] + g[i + 1]);
					}
				}
			}
		}
		int ret = 0;
		for (int e = 0; e <= 1000; ++e) {
			ret = max(ret, dp[n][e][0]);
			ret = max(ret, dp[n][e][1]);
		}
		printf("Case #%d: %d\n", tt, ret);
	}

	return 0;
}

