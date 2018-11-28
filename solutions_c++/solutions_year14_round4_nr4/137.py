#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
using namespace std;
const int MOD = 1000000007;
int n, m, ans1, ans2;
vector<string> s;
vector<vector<string> > d;
int ord[10];


int mdl(vector<string> &data)
{
	sort(data.begin(), data.end());
	vector<string>::iterator it;
	it = unique(data.begin(), data.end());
	data.resize(distance(data.begin(), it));
	return 0;
}

int init()
{
	cin >> m >> n;
	s.clear();
	for (int i = 0; i < m; i++)
	{
		string tmp;
		cin >> tmp;
		s.push_back(tmp);
	}
	d.resize(m);
	for (int i = 0; i < m; i++)
	{
		d[i].clear();
		for (int j = 1; j <= s[i].length(); j++)
		{
			d[i].push_back(s[i].substr(0, j));
		}
	}
	return 0;
}

void dfs(int depth)
{
	if (depth >= m)
	{
		vector<vector<string> > final;
		final.resize(n);
		for (int i = 0; i < n; i++)
			final[i].clear();
		for (int i = 0; i < m; i++)
		{
			int k = ord[i];
			for (int j = 0; j < d[i].size(); j++)
				final[k].push_back(d[i][j]);
		}

		int tot = 0;
		for (int i = 0; i < n; i++)
		{
			if (final[i].size() == 0) return;
			mdl(final[i]);
			tot += (int)final[i].size() + 1;
		}
		
		if (tot > ans1)
		{
			ans1 = tot;
			ans2 = 1;
		}
		else if (tot == ans1)
		{
			ans2++;
		}
		return;
	}
	for (int i = 0; i < n; i++)
	{
		ord[depth] = i;
		dfs(depth + 1);
	}
}

int work()
{
	ans1 = ans2 = 0;
	dfs(0);
	return 0;
}

int main()
{
	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test)
	{
		init();
		work();
		cout << "Case #" << test << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}