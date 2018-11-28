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

string a[1000];
vector<pair<int, char> > p[1000];
int cnt[1000];

void solve()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		p[i].clear();
		cin >> a[i];
		cnt[i] = 0;
	}

	for (int str = 0; str < n; str++)
	{
		for (int i = 0; i < a[str].size(); i++)
			if (p[str].empty() || a[str][i] != p[str].back().second)
				p[str].push_back(make_pair(1, a[str][i]));
			else
				p[str].back().first++;
	}

	bool win = 1;
	for (int i = 1; i < n; i++)
	{
		if (p[i].size() != p[0].size())
		{
			win = 0;
			break;
		}
		for (int j = 0; j < p[0].size(); j++)
		{
			if (p[0][j].second != p[i][j].second)
				win = 0;
		}
	}

	if (!win)
	{
		cout << "Fegla Won";
		return;
	}

	int ans = 0;
	for (int i = 0; i < p[0].size(); i++)
	{
		int best = 1e9;
		for (int len = 1; len <= 200; len++)
		{
			int loc = 0;
			for (int j = 0; j < n; j++)
				loc += abs(len - p[j][i].first);
			best = min(best, loc);
		}

		ans += best;
	}

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