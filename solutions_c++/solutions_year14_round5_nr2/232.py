#include <algorithm>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

const int oo = (~0u) >> 1;
int n, p, q;
int h[1000 + 2], g[1000 + 2];
int dp[1000 + 2][1000 + 2][2];

int calc(int i, int j, int k, int l, int m) {
	int hi = h[i];
	if (j <= l) {
		hi -= p * (l - j);
		if (hi <= 0) {
			if (hi + p <= 0 || m != k) {
				return -oo;
			} else {
				return g[i];
			}
		}
		if (m) {
			hi -= q;
		}
		if (hi <= 0) {
			if (k) {
				return -oo;
			} else {
				return 0;
			}
		}
		if (1 <= hi % (p + q) && hi % (p + q) <= p) {
			if (k) {
				return g[i];
			} else {
				return -oo;
			}
		} else {
			if (k) {
				return -oo;
			} else {
				return 0;
			}
		}
	} else {
		if (m)
			hi -= q;
		if (hi <= 0) {
			return -oo;
		}
		hi -= q * (j - l);
		if (hi <= 0) {
			if (hi + q <= 0 || k) {
				return -oo;
			} else {
				return 0;
			}
		}
		if (1 <= hi % (p + q) && hi % (p + q) <= p) {
			if (k) {
				return g[i];
			} else {
				return -oo;
			}
		} else {
			if (k) {
				return -oo;
			} else {
				return 0;
			}
		}
	}
}

void solve() {
	cin >> p >> q >> n;
	for (long long i = 1; i <= n; i++) {
		cin >> h[i] >> g[i];
	}
	dp[0][0][0] = 0;
	dp[0][0][1] = -oo;
	for (int i = 1; i <= 1000; i++) {
		dp[0][i][0] = -oo;
		dp[0][i][1] = -oo;
	}
	int ans = -oo;
	for (int i = 1; i <= n; i++) {
		for (int j = 0; j <= 1000; j++) {
			for (int k = 0; k <= 1; k++) {
				dp[i][j][k] = -oo;
				for (int l = 0; l <= 1000; l++) {
					for (int m = 0; m <= 1; m++) {
						if (dp[i - 1][l][m] >= 0) {
							dp[i][j][k] = max(dp[i][j][k],
									dp[i - 1][l][m] + calc(i, j, k, l, m));
//							if (j <= 10 && l <= 10) {
//									cerr << i << "," << j << "," << k << ","
//											<< l << "," << m << ":"
//											<< calc(i, j, k, l, m) << endl;
//							}
						}
					}
				}
//				if (dp[i][j][k] >= 0 && j <= 10) {
//					cerr << i << "," << j << "," << k << ":" << dp[i][j][k]
//							<< endl;
//				}
				if (i == n) {
					ans = max(ans, dp[i][j][k]);
				}
			}
		}
	}
	printf(" %d\n", ans);
}

int main() {
	freopen("src/out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		printf("Case #%d:", t);
		solve();
	}
}
