#include <iostream>
#include <set>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;
//#define int long long
const int INF = 1234567890;
signed main() {
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int q;
	cin >> q;
	
	for (int qq = 1; qq <= q; ++qq) {
		string s;
		cin >> s;
		vector <pair <int, int> > dp(s.size(), make_pair(INF, INF));
		if (s[0] == '-') {
			dp[0].first = 1;
			dp[0].second = 0;
		}
		else {
			dp[0].second = 1;
			dp[0].first = 0;
		}
		for (int i = 1; i < s.size(); ++i) {
			if (s[i] == '-') {
				dp[i].first = min(dp[i].first, dp[i - 1].second + 1);
				dp[i].first = min(dp[i].first, dp[i - 1].second + 2);
				dp[i].second = min(dp[i].second, dp[i - 1].first + 1);
				dp[i].second = min(dp[i].second, dp[i - 1].second);
			}
			else {
				dp[i].second = min(dp[i].second, dp[i - 1].first + 1);
				dp[i].second = min(dp[i].second, dp[i - 1].first + 2);
				dp[i].first = min(dp[i].first, dp[i - 1].second + 1);
				dp[i].first = min(dp[i].first, dp[i - 1].first);
			}
		}
		printf("Case #%d: %d\n", qq, dp[s.size() - 1].first);
	}
}