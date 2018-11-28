#include <iostream>
#include <stdio.h>
#include <vector>
#include <string.h>
#include <string>
#include <algorithm>

using namespace std;

const int MAXN = 111;

int n, P, Q;
int h[MAXN], g[MAXN], ret, rrt;

void Dfs()
{
	int lowi = 0;
	for (; h[lowi] <= 0 && lowi < n; lowi ++);
	if (lowi >= n)
	{
		ret = max(ret, rrt);
		return;
	}
	int lrrt = rrt, rem = 0;
	for (int i = 0; i < n; i ++)
		if (h[i] > 0)  rem += g[i];
	if (rrt + rem <= ret)  return;
	for (int i = 0; i < n; i ++)
		if (h[i] > 0)
		{
			h[i] -= P;
			if (h[i] <= 0) rrt += g[i];
			for (lowi = 0; h[lowi] <= 0 && lowi < n; lowi ++);
			h[lowi] -= Q;
			Dfs();
			h[lowi] += Q;
			rrt = lrrt;
			h[i] += P;
		}
	for (lowi = 0; h[lowi] <= 0 && lowi < n; lowi ++);
	h[lowi] -= Q;
	Dfs();
	h[lowi] += Q;
}

int Work()
{
	cin >> P >> Q >> n;
	for (int i = 0; i < n; i ++)
		cin >> h[i] >> g[i];
	ret = rrt = 0;
	Dfs();
	return ret;
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t ++)
		printf("Case #%d: %d\n", t, Work());
	return 0;
}