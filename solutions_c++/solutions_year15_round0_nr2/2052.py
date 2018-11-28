#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1010;
int a[MAXN];
int dp[MAXN][MAXN];

void precalc() {
	for (int i = 1; i < MAXN; ++i) {
		dp[i][0] = MAXN * MAXN;
		for (int k = 1; k <= MAXN; ++k) {
			dp[i][k] = dp[i - 1][k - 1];
			for (int d = 1; d <= i; ++d) {
				dp[i][k] = min(dp[i][k], 1 + dp[d][k] + dp[i - d][k]);
			}
		}
	}
/*
	for (int k = 1; k < MAXN; ++k) {
		for (int i = 0; i <= k; ++i) {
     		dp[k][i] = 0;
     	}
     	for (int i = k + 1; i < MAXN; ++i) {
     		dp[k][i] = 1 + dp[k][i / 2] + dp[k][i - (i / 2)];
     	}
	}*/
}

int cans = MAXN;

void go(int n, int cur) {
	if (cur >= cans) return;
	bool ok = true;
	for (int i = 0; i < n; ++i) {
		if (a[i] > 0) {
			ok = false;
		}
		--a[i];
	}
	if (ok) {
		cans = cur;
	} else {
		go(n, cur + 1);
	}
	for (int i = 0; i < n; ++i) {
		++a[i];
	}
	if (!ok) {
    	for (int i = 0; i < n; ++i) if (a[i] > 1) {
    		int d = a[i] / 2;
    		a[i] -= d;
    		a[n] = d;
    		go(n + 1, cur + 1);
    		a[i] += d;
    		a[n] = 0;
    	}
	}
}

void solve() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", a + i);
	}
//	sort(a, a + n);
	int ans = MAXN;
	for (int k = 1; k < MAXN; ++k) {
		int cans = k;
		for (int i = 0; i < n; ++i) {
			cans += dp[a[i]][k];
		}
//		cerr << k << ' ' << cans << endl;
		ans = min(ans, cans);
	}
//	cans = MAXN;
//	go(n, 0);
	printf("%d\n", ans);
}

int main() {
	int tt;
	scanf("%d", &tt);
	precalc();
	for (int t = 1; t <= tt; ++t) {
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}