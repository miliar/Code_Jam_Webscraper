#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;


const int maxn = 4005;
vector <int> g[maxn];
bool used[85][85][2];
int dp[85][85][2];

const int inf = 1e9;
int c[maxn];

bool usedV[maxn];
bool usedE[maxn][maxn];


int getAns(int a, int b, int t)
{
	if (used[a][b][t] )
		return dp[a][b][t];


	used[a][b][t] = true;
	dp[a][b][t] = 0;
	
	int addAns = 0;
	bool un = false;
	if (!usedV[a] )
	{
		un = true;
		usedV[a] = true;
		addAns = c[a];
	}

	int ans = -inf;
	int eht = false;
	for (int i = 0; i < g[b].size(); i++)
	{
		int nb = g[b][i];
		if (usedE[b][nb] )
			continue;
		eht = true;
	}
	int ht = false;
	for (int i = 0; i < g[a].size(); i++)
	{
		int na = g[a][i];
		if (usedE[a][na] )
			continue;
		usedE[a][na] = usedE[na][a] = true;

		ht = true;
		ans = max(ans, -getAns(b, na, t ^ 1) );

		usedE[a][na] = usedE[na][a] = false;
	}
	if (!usedV[b] )
		eht = true;
	if (!ht && !eht)
		ans = 0;
	else if (!ht)
		ans = -getAns(b, a, t ^ 1);
	
	if (un)
		usedV[a] = false;

	//fprintf(stderr, "dp: a = %d, b = %d, ans = %d\n", a, b, ans + addAns);
	return dp[a][b][t] = ans + addAns;
}


void solve()
{
	for (int i = 0; i < maxn; i++)
		g[i].clear();

	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &c[i] );
	for (int i = 0; i < n - 1; i++)
	{
		int a, b;
		scanf("%d", &b);
		a = i;
		b--;
		g[a].push_back(b);
		g[b].push_back(a);
	}
	int ans = -inf;

//	int x = getAns(7, 0);
//	fprintf(stderr, "\ni = %d, j = %d, ans = %d ", 7, 0, x);


	for (int i = 0; i < n; i++)
	{
		int curans = inf;
		for (int j = 0; j < n; j++)
		{
			memset(used, false, sizeof used);
			int x = getAns(i, j, 0);
			//fprintf(stderr, "\ni = %d, j = %d, ans = %d", i, j, x);
			curans = min(curans, x);
		}
		ans = max(ans, curans);
	}
	printf("%d", ans);
}



int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		fprintf(stderr, "Case #%d: ", i + 1);
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
		fprintf(stderr, "OK\n");
	}


	return 0;
}