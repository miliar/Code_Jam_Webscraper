#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


typedef long double f64;

int main()
{
	int testcase;

	scanf("%d", &testcase);

	for(int casenum = 1; casenum <= testcase; ++casenum) {

		int n, t;
		vector<double> p;

		scanf("%d%d", &n, &t);
		p.resize(n);
		for(int i = 0; i < n; ++i)
			scanf("%lf", &p[i]);

		sort(p.begin(), p.end());

		f64 ans = 0;

		for(int pre = 0; pre <= t; ++pre) {

			vector<double> sel;

			for(int i = 0; i < pre; ++i)
				sel.push_back(p[i]);
			for(int i = 0; i < t - pre; ++i)
				sel.push_back(p[n - 1 - i]);

			vector<vector<f64>> dp;

			dp.resize(t + 1);
			for(int i = 0; i < t + 1; ++i)
				dp[i].resize(t + 1, 0);

			dp[0][0] = 1;

			for(int c = 1; c <= t; ++c) {
				for(int s = 0; s <= t; ++s) {
					f64 x = sel[c - 1];
					dp[c][s] =
						x * (s > 0 ? dp[c - 1][s - 1] : 0) +
						(1 - x) * dp[c - 1][s];
				}
			}

			ans = max(ans, dp[t][t / 2]);
		}

		printf("Case #%d: %.10lf\n", casenum, (double)ans);
	}

	return 0;
}
