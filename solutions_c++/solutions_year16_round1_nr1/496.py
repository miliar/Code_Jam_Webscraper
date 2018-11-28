#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
#include<time.h>
using namespace std;

const int N = 1005;
string s;
string dp[N][N];

string solve(string t, string has)
{
	if (t == "")
		return has;
	return max(
		solve(t.substr(1), t[0] + has),
		solve(t.substr(1), has + t[0]));
}

void solve()
{
	cin >> s;
	int n = s.length();
	
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			dp[i][j] = "";
	for (int i = 0; i < n; i++)
		dp[i][i] = s[0];

	for (int len = 1; len < n; len++)
		for (int l = 0; l + len <= n; l++)
		{
			int r = l + len - 1;
			string t = dp[l][r];
			string a = s[len] + t;
			string b = t + s[len];

			if (l > 0)
				dp[l - 1][r] = max(dp[l - 1][r], a);
			if (r < n)
				dp[l][r + 1] = max(dp[l][r + 1], b);
		}

	cout << dp[0][n - 1];
	//cout << solve(s, "");
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	long long T;
	cin >> T;
	for (long long t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		cerr << t << " " << 1.0 * clock() / CLOCKS_PER_SEC << endl;
	}
}