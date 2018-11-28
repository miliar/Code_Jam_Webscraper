#include <iostream>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

const int maxn = 1000;
int n, m;
char a[maxn][maxn];

int check(int x, int y)
{
	if (a[x][y] == '.')
		return 0;
	bool flag = false, tot = false;
	for (int i = 0; i < x; ++i)
		if (a[i][y] != '.')
			flag = true;
	if (flag)
	{
		tot = true;
		if (a[x][y] == '^')
			return 0;
	}
	flag = false;
	for (int i = x+1; i < n; ++i)
		if (a[i][y] != '.')
			flag = true;
	if (flag)
	{
		tot = true;
		if (a[x][y] == 'v')
			return 0;
	}
	flag = false;
	for (int i = 0; i < y; ++i)
		if (a[x][i] != '.')
			flag = true;
	if (flag)
	{
		tot = true;
		if (a[x][y] == '<')
			return 0;
	}
	flag = false;
	for (int i = y+1; i < m; ++i)
		if (a[x][i] != '.')
			flag = true;
	if (flag)
	{
		tot = true;
		if (a[x][y] == '>')
			return 0;
	}
	if (tot)
		return 1;
	return -10001;
}

void solve()
{
	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; ++i)
	{
		scanf("%c", &a[i][0]);
		for (int j = 0; j < m; ++j)
		{
			scanf("%c", &a[i][j]);
		}
	}
	int ans = 0;
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
		{
			ans += check(i, j);
			//cout << check(i, j) << endl;
		}
	if (ans < 0)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", ans);
}

int main()
{
	freopen("a.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}