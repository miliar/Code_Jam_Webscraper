/*
	Author:USETC_elfness
*/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
typedef long long LL;
const int V=1100;
const int P=1000000007;
using namespace std;
int s[V], mx[V], mi[V], now[V], n, m;
int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int _;
	scanf("%d", &_);
	for(int ca = 1; ca <= _; ++ca)
	{
		scanf("%d%d", &n, &m);
		for(int i = 0; i < m; ++i)
		mx[i] = mi[i] = now[i] = 0;
		scanf("%d", &s[0]);
		for(int i = 1; i <= n - m; ++i)
		{
			scanf("%d", &s[i]);
			now[(i - 1) % m] += s[i] - s[i - 1];
			mx[(i - 1) % m] = max(mx[(i - 1) % m], now[(i - 1) % m]);
			mi[(i - 1) % m] = min(mi[(i - 1) % m], now[(i - 1) % m]);
		}
		int add = 0;
		for(int i = 0; i < m; ++i)
		{
			mx[i] += mi[0] - mi[i];
			add += mi[0] - mi[i];
			mi[i] = mi[0];
		}
		add = (((add - s[0]) % m) + m) % m;
		int nd = (m - add) %m;
		int ret = 0;
		for(int i = 0; i <m; ++i) ret = max(ret, mx[i] - mi[i]);
		int df = 0;
		//for(int i = 0; i < m; ++i) printf("M %d %d\n",mx[i],mi[i]);
		for(int i = 0; i < m; ++i) df += ret - (mx[i] - mi[i]);
		//printf("%d %d %d\n", ret, df, nd);
		if(df < nd) ret++;
		printf("Case #%d: %d\n", ca, ret);
	}
	return 0;
}
