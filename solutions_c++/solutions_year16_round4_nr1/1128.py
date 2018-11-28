#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
using namespace std;
typedef long long int64;
#define rep(x, n) for (int x = 1; x <= n; ++x)
#define zrp(x, n) for (int x = n; x; --x)
#define FOR(x, l, r) for (int x = l; x <= r; ++x)
#define foredge(i, x) for (int i = start[x]; i; i = e[i].l)
struct edge{int a, l;};
int p[10000];
int n, x, y, z;
string a[20][1000];
char nxt[1000];
string ans;

int main()
{
	nxt['R'] = 'S';
	nxt['S'] = 'P';
	nxt['P'] = 'R';
	a[0]['R'] = "R";
	a[0]['S'] = "S";
	a[0]['P'] = "P";
	rep(i, 12) rep(j, 200) if (nxt[j])
	{
		char y = nxt[j];
		if (a[i - 1][y] < a[i - 1][j])
		{
			a[i][j] = a[i - 1][y] + a[i - 1][j];
		}
		else
		{
			a[i][j] = a[i - 1][j] + a[i - 1][y];
		}
	}
	p[1] = 0;
	for (int i = 1; i < (1 << 12); ++i)
	{
		p[i + i] = p[i];
		p[i + i + 1] = (p[i] + 1) % 3;
	}
	int T;
	scanf("%d", &T);
	rep(ca, T)
	{
		scanf("%d%d%d%d", &n, &x, &y, &z);
		printf("Case #%d: ", ca);
		ans = "";
		int c[10];
		memset(c, 0, sizeof(c));
		FOR(i, (1 << n), ((1 << (n + 1)) - 1))
		{
			c[p[i]]++;
		}
		if (c[0] == x && c[1] == z && c[2] == y)
		{
			ans = a[n]['R'];
		}else
		if (c[1] == y && c[2] == x && c[0] == z)
		{
			ans = a[n]['S'];
		}else
		if (c[2] == z && c[0] == y && c[1] == x)
		{
			ans = a[n]['P'];
		}else
		{
			ans = "IMPOSSIBLE";
		}

		printf("%s\n", ans.c_str());
	}
	return 0;
}
