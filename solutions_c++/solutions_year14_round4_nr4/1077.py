#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
#include <queue>
#include <string>
#include <ctime>
#include <map>

using namespace std;

char s[10][20];
int pos[10];
int m, n;
vector<string> ve[4];
int ans[200];
bool was[10];

void rec(int id)
{
	if (id == m)
	{
		memset(was, 0, sizeof(was));
		for (int i = 0; i < m; i++)
			was[pos[i]] = 1;
		for (int i = 0; i < n; i++)
			if (!was[i])
				return;
		for (int i = 0; i < n; i++)
			ve[i].clear();
		for (int i = 0; i < m; i++)
		{
			string str = "";
			for (int j = 0; s[i][j]; j++)
			{
				str += s[i][j];
				ve[pos[i]].push_back(str);
			}
		}
		int cnt = n;
		for (int i = 0; i < n; i++)
		{
			sort(ve[i].begin(), ve[i].end());
			cnt += unique(ve[i].begin(), ve[i].end()) - ve[i].begin();
		}
		ans[cnt]++;
		return;
	}

	for (int i = 0; i < n; i++)
	{
		pos[id] = i;
		rec(id + 1);
	}
}

int main()
{
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++)
	{
		scanf("%d%d", &m, &n);
		for (int i = 0; i < m; i++)
			scanf("%s", s[i]);

		memset(ans, 0, sizeof(ans));
		rec(0);
		int res = 0, cntRes = 0;
		for (int i = 0; i < 200; i++)
			if (ans[i] > 0)
				res = i, cntRes = ans[i];
		printf("Case #%d: %d %d\n", tt + 1, res, cntRes);
	}


	return 0;
}


/*
int n;
int a[100005];
int b[100005];
int c[100005];
int rev[100005];
map<int, int> mp;

int getAns()
{
	for (int i = 0; i < n; i++)
		c[i] = a[i];
	for (int i = 0; i < n; i++)
		rev[c[i]] = i;
	
	int ans = 0;
	for (int i = 0; i < n; i++)
	{
		while (c[i] != b[i])
		{
			int id = rev[b[i]];
			rev[c[id]] = i;
			rev[c[i]] = id;
			swap(c[i], c[id]);
			ans++;
		}
	}
	return ans;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]), b[i] = a[i];
		sort(b, b + n);

		mp.clear();
		for (int i = 0; i < n; i++)
			mp[b[i]] = i;

		for (int i = 0; i < n; i++)
			a[i] = mp[a[i]], b[i] = i;

		int ans = 1000000000;
		while (true)
		{
			int isGood = 0;
			for (int i = 1; i < n; i++)
			{
				if (isGood == 0 && b[i] < b[i - 1])
					isGood++;
				if (isGood == 1 && b[i] > b[i - 1])
					isGood = 2;
			}
			if (isGood < 2)
				ans = min(ans, getAns());

			if (!next_permutation(b, b + n))
				break;
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}
	

	return 0;
}*/