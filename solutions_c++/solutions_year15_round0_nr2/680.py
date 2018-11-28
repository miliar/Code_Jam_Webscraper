#include <bits/stdc++.h> 
using namespace std;

int memo[1001][1001];

int DP(int i, int j) {
	if (i <= j) return 0;
	if (memo[i][j] + 1) return memo[i][j];
	memo[i][j] = 1e5;
	for (int c = 1; c < i; ++c)
		memo[i][j] = min(memo[i][j], DP(c, j) + DP(i - c, j) + 1);
	return memo[i][j];
}

int main() {
	memset(memo, -1, sizeof memo);
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	cin >> t;
	for (int tst = 1; tst <= t; ++tst) {
		vector<int> vec;
		int d, tmp;
		cin >> d;
		while (d--)
			cin >> tmp, vec.push_back(tmp);
		int mn = 1e5;
		for (int l = 1; l < 1001; ++l) {
			int ans = l;
			for (int i = 0; i < vec.size(); ++i)
				ans += DP(vec[i], l);
			mn = min(ans, mn);
		}
		cout << "Case #" << tst << ": " << mn << '\n';
	}
}
