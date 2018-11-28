#include <bits/stdc++.h>
using namespace std;


int n_test;
int n, k;
pair<int, int> a[222];
int dp[222][22222], ndp[222][22222];
bool trace[222][222][22222];
#define DP(i, j) dp[i][j + 10001]
#define nDP(i, j) ndp[i][j + 10001]
#define Trace(i, j, k) trace[i][j][k + 10001]

double prob[222][222];
#define Prob(i, j) prob[i][j + 101]

#define sqr(x) (x) * (x)

int f(int i) {
//	return abs(a[i].first);
	return sqr(max(100 - a[i].second, a[i].second));
}

int main() {
	freopen("B-small-attempt01.in", "r", stdin);
	freopen("B-small-attempt01.out", "w", stdout);
	scanf("%d", &n_test);
	for (int test = 1; test <= n_test; ++test) {
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n; ++i) {
			double x;
			scanf("%lf", &x);
			a[i].second = int(x * 100 + 1e-8);
			a[i].first = 2 * a[i].second - 100;
		}
		memset(dp, -1, sizeof dp);
		memset(trace, 0, sizeof trace);
		DP(0, 0) = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j <= k; ++j)
				for (int sum = -10000; sum <= 10000; ++sum)
					nDP(j, sum) = DP(j, sum);
			for (int j = 0; j <= k; ++j)
				for (int sum = -10000; sum <= 10000; ++sum)
					if (DP(j, sum) >= 0) {
						if (nDP(j + 1, sum + a[i].first) < DP(j, sum) + f(i)) {
							nDP(j + 1, sum + a[i].first) = DP(j, sum) + f(i);
							Trace(i, j + 1, sum + a[i].first) = true;
						} 
					}
			for (int j = 0; j <= k; ++j)
				for (int sum = -10000; sum <= 10000; ++sum)
					DP(j, sum) = nDP(j, sum);

		}

		double result = 0;
		int chosen = 0;
		for (int chosen = -10000; chosen <= 10000; ++chosen) {
			if (DP(k, chosen) >= 0) {
				memset(prob, 0, sizeof prob);
				Prob(k + 1, 0) = 1;
				for (int i = n - 1, s = chosen, j = k; i >= 0; --i) {
					if (Trace(i, j, s) == true) {
						for (int sum = -100; sum <= 100; ++sum)
							Prob(j, sum) = Prob(j + 1, sum - 1) * a[i].second / 100 + Prob(j + 1, sum + 1) * (100 - a[i].second) / 100;
						s -= a[i].first;
						--j;
					}
				}
				result = max(result, Prob(1, 0));
			}
		}
		printf("Case #%d: %.9lf\n", test, result);
	}
}
