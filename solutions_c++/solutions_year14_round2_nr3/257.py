#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

const int sz = 10;
string zip[sz];
string dp[1000][1000];

vector<int> G[sz];
string ans, inf;
int all, n, m;

string myMin(string &a, string &b)
{
	if (a.size() < b.size())
		return a;
	if (a.size() > b.size())
		return b;
	return min(a, b);
}

string fly(int s, int mask)
{
	if (dp[s][mask] != inf)
		return dp[s][mask];
	if ((mask & (1 << s)) == 0)
		return inf;

	for (int mask2 = 0; mask2 <= all; mask2++)
	{
		if ((mask & mask2) != mask2 || mask == mask2 || (mask2 & (1 << s)) == 0)
			continue;

		string p1 = fly(s, mask2);
		int mask3 = (mask ^ mask2);

		for (int i = 0; i < G[s].size(); i++)
		{
			int k = G[s][i];
			string p2 = fly(k, mask3);
			dp[s][mask] = myMin(dp[s][mask], p1 + p2);
		}
	}

	return dp[s][mask];
}

void solve()
{
	n, m;
	cin >> n >> m;
	all = (1 << n) - 1;
	
	inf = "";
	for (int i = 0; i < n * 6; i++)
		inf += "9";
	for (int i = 0; i <= all; i++)
		for (int s = 0; s < n; s++)
			dp[s][i] = inf;

	for (int i = 0; i < n; i++)
	{
		cin >> zip[i];
		dp[i][1 << i] = zip[i];
		G[i].clear();
	}
	for (int i = 0; i < m; i++)
	{
		int a, b;
		cin >> a >> b;
		a--;
		b--;
		G[a].push_back(b);
		G[b].push_back(a);
	}

	ans = inf;
	for (int s = 0; s < n; s++)
		ans = min(ans, fly(s, all));
	cout << ans;
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}