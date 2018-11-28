#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n, t, k;
double p[205];
double dp[205][205];

void addin(double y, int tot) {
	for (int i = 0; i <= tot; ++i) {
		dp[tot+1][i] += dp[tot][i]*(1-y);
		dp[tot+1][i+1] += dp[tot][i]*y;
	}
}

void run(int t) {
	cout << "Case #" << t+1 << ": ";
	cin >> n >> k;
	double best = 0;

	for (int i = 0; i < n; ++i)
		cin >> p[i];
	sort(p, p+n);
	for (int i = -1; i < k; ++i) {
		memset(dp, 0, sizeof(dp));
		dp[0][0] = 1.0;
		for (int j = 0; j <= i; ++j)
			addin(p[j], j);
		for (int j = n-1; j >= n-(k-i-1); --j)
			addin(p[j], i+1+(n-1-j));
		best = max(best, dp[k][k/2]);
	}

	cout << fixed << setprecision(20) << best << endl;
}

int main() {
	cin >> t;
	for (int i = 0; i < t; ++i)
		run(i);
}
