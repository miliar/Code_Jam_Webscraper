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
int n, m, p[105][105];

void init()
{
	char s[105];
	scanf("%d%d", &n, &m);
	rep(i, n)
	{
		scanf("%s", s + 1);
		rep(j, m)
		{
			if (s[j] == '^')
				p[i][j] = 1;
			else if (s[j] == 'v')
				p[i][j] = 2;
			else if (s[j] == '<')
				p[i][j] = 3;
			else if (s[j] == '>')
				p[i][j] = 4;
			else p[i][j] = 0;
		}
	}
}

bool check(int x, int y, int pp)
{
	int dx, dy;
	if (pp == 1) dx = -1, dy = 0;
	if (pp == 2) dx = 1, dy = 0;
	if (pp == 3) dx = 0, dy = -1;
	if (pp == 4) dx = 0, dy = 1;

	x += dx; y += dy;
	while (x > 0 && x <= n && y > 0 && y <= m)
	{
		if (p[x][y]) return 1;
		x += dx; y += dy;
	}
	return 0;
}

void work()
{
	int ans = 0;
	rep(i, n) rep(j, m) if (p[i][j])
	{
		if (check(i, j, p[i][j])) continue;
		bool flag = 0;
		rep(k, 4) if (check(i, j, k))
			flag = 1;
		++ans;
		if (flag == 0)
		{
			puts("IMPOSSIBLE");
			return;
		}
	}
	printf("%d\n", ans);
}

int main()
{
	int ca;
	scanf("%d", &ca);
	rep(t, ca)
	{
		init();
		printf("Case #%d: ", t);
		work();
	}
	return 0;
}