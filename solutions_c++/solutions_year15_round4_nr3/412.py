#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

using namespace std;

char s[20][20005];
map<string, int> mp;
int sz = 0;
vector<int> ve[22];
int en[10005][2];

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++)
	{
		mp.clear();
		sz = 0;
		for (int i = 0; i < 20; i++)
			ve[i].clear();
		memset(en, 0, sizeof(en));

		int n;
		scanf("%d", &n);
		gets(s[0]);
		for (int i = 0; i < n; i++)
		{
			gets(s[i]);
			string wo = "";
			for (int j = 0; s[i][j]; j++)
			{
				if (s[i][j] == ' ')
				{
					if (mp.count(wo) == 0)
						mp[wo] = sz++;
					ve[i].push_back(mp[wo]);
					wo = "";
				}
				else
					wo += s[i][j];
			}
			if (mp.count(wo) == 0)
				mp[wo] = sz++;
			ve[i].push_back(mp[wo]);
		}
		for (int i = 0; i < 2; i++)
		{
			for (int j = 0; j < ve[i].size(); j++)
				en[ve[i][j]][i] ++;
		}
		int ans = sz;
		for (int i = 0; i < (1 << (n - 2)); i++)
		{
			for (int j = 0; j < n - 2; j++)
			{
				int id = (i & (1 << j)) > 0;
				for (int k = 0; k < ve[j + 2].size(); k++)
					en[ve[j + 2][k]][id]++;
			}
			int res = 0;
			for (int j = 0; j < sz; j++)
				res += (en[j][0] > 0 && en[j][1] > 0);
			ans = min(ans, res);
			for (int j = 0; j < n - 2; j++)
			{
				int id = (i & (1 << j)) > 0;
				for (int k = 0; k < ve[j + 2].size(); k++)
					en[ve[j + 2][k]][id]--;
			}
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}

	return 0;
}



/*
int n;
double v, t;
double r[105], ti[105];

int main()
{
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 0; tt < T; tt++)
	{
		scanf("%d%lf%lf", &n, &v, &t);
		for (int i = 0; i < n; i++)
			scanf("%lf%lf", &r[i], &ti[i]);

		printf("Case #%d: ", tt + 1);
		if (n == 1)
		{
			if (fabs(ti[0] - t) > 1e-5)
				printf("IMPOSSIBLE\n");
			else
				printf("%.9lf\n", v / r[0]);
		}
		else
		{
			if ((ti[0]-t) * (ti[1] - t) > 1e-9)
				printf("IMPOSSIBLE\n");
			else if (fabs(ti[0] - ti[1]) < 1e-5)
				printf("%.9lf\n", v / (r[0] + r[1]));
			else
			{
				double v1 = v * (t - ti[1]) / (ti[0] - ti[1]), v2 = v - v1;
				printf("%.9lf\n", max(v1 / r[0], v2 / r[1]));
			}
		}
	}


	return 0;
}*/