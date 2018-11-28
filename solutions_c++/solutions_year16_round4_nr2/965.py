#include <bits/stdc++.h>

using namespace std;
#define MAX 220

int n,t,k;
double v[MAX];
double dp[MAX][MAX][MAX];
int mark[MAX][MAX][MAX];
int casos;

double solve(int curr, int y, int no, vector<double>& vals)
{
	if (curr == vals.size() && y == no)
		return 1.0;
	else if (curr == vals.size())
		return 0;
	double & ret = dp[curr][y][no];
	if (mark[curr][y][no] == casos)
		return ret;
	mark[curr][y][no] = casos;
	ret = solve(curr + 1, y + 1, no, vals) * vals[curr] + solve(curr + 1, y, no + 1, vals) * (1.0 - vals[curr]);
	return ret;
}

int main(void)
{
	scanf("%d",&t);
	for (int cases = 1; cases <= t; ++cases)
	{
		scanf("%d %d",&n,&k);
		for (int i = 0; i < n; ++i)
		{
			scanf("%lf",&v[i]);
		}
		sort(v, v + n);
		double ans = 0;
		for (int i = 0; i < n; ++i)
		{
			vector<double> val;
			for (int j = 0; j < k; ++j)
			{
				int id = (i + j)%n;
				val.push_back(v[id]);
			}
			++casos;
			ans = max(ans, solve(0, 0, 0, val));
		}
		printf("Case #%d: %.7lf\n",cases,ans);
	}
	return 0;
}