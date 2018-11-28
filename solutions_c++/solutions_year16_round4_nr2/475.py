#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <complex> 
#include <ctime>
#include <cstring>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()


double solve(const vector<double> &p) {
	int n = sz(p);
	vector<vector<double>> dp(n + 1, vector<double>(n + 1));
	dp[0][0] = 1;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j <= i + 1; ++j) {
			if (j > 0)
				dp[j][i + 1 - j] += p[i] * dp[j - 1][i + 1 - j];
			if (i + 1 - j > 0)
				dp[j][i + 1 - j] += (1 - p[i]) * dp[j][i - j];
		}
	}
	return dp[n / 2][n / 2];
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int t = 0; t < tests; ++t) {
    	cout << "Case #" << t + 1 << ": ";
    	int n, k;
    	cin >> n >> k;
    	vector<double> p(n);
    	for (int i = 0; i < n; ++i)
    		cin >> p[i];
    	sort(all(p));
    	double ans = 0;
    	for (int i = 0; i <= k; ++i) {
    		vector<double> q;
    		for (int j = 0; j < i; ++j)
    			q.push_back(p[j]);
    		for (int j = n - k + i; j < n; ++j)
    			q.push_back(p[j]);
    		ans = max(ans, solve(q));
    	}
    	printf("%.10f\n", ans);
    }

    return 0;
}