#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long s64;

const int MaxN = 1000000;

int n, limD;
int a[MaxN], fa[MaxN];
int xL[MaxN], xR[MaxN];
int wei[MaxN];

inline int handle()
{
	xL[0] = a[0] - limD, xR[0] = a[0];
	for (int v = 1; v < n; v++)
		xL[v] = max(xL[fa[v]], a[v] - limD), xR[v] = min(xR[fa[v]], a[v]);
	for (int v = 0; v < n; v++)
		wei[v] = 0;
	for (int v = n - 1; v >= 0; v--)
	{
		wei[v]++;
		if (fa[v])
			wei[fa[v]] += wei[v];
	}

	int li_n = 0;
	static pair<int, int> li[MaxN * 2];
	for (int v = 0; v < n; v++)
		if (xL[v] <= xR[v])
			li[li_n++] = make_pair(xL[v], 1), li[li_n++] = make_pair(xR[v] + 1, -1);
	sort(li, li + li_n);

	int res = 0;
	int cur = 0;
	for (int i = 0; i < li_n; i++)
		cur += li[i].second, res = max(res, cur);
	return res;
}

int main()
{
	int nT;
	cin >> nT;

	for (int nt = 1; nt <= nT; nt++)
	{
		int s0, as, cs, rs;
		int m0, am, cm, rm;
		cin >> n >> limD;
		cin >> s0 >> as >> cs >> rs;
		cin >> m0 >> am >> cm >> rm;

		a[0] = s0;
		fa[0] = m0;
		for (int i = 1; i < n; i++)
		{
			a[i] = ((s64)a[i - 1] * as + cs) % rs;
			fa[i] = ((s64)fa[i - 1] * am + cm) % rm;
		}
		fa[0] = 0;
		for (int i = 1; i < n; i++)
			fa[i] %= i;

		printf("Case #%d: %d\n", nt, handle());
	}

	return 0;
}
