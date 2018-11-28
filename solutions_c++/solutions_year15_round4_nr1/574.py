#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<time.h>
#include<string>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
#include<iostream>
#include<queue>
using namespace std;

struct pr
{
	int x, y, d;
	pr(int xe = 0, int ye = 0, int de = 0)
	{
		x = xe;
		y = ye;
		d = de;
	}
};

char s[105][105];
int a[105][105];

int st[4][2] = {0, 1, 1, 0, 0, -1, -1, 0};

int n, m;
int getdir(int x, int y)
{
	if (s[x][y] == '^')
		return 3;
	if (s[x][y] == '>')
		return 0;
	if (s[x][y] == 'v')
		return 1;
	if (s[x][y] == '<')
		return 2;
	return -1;
}

int follow(int x, int y, int d)
{
	vector<pr> tmp;
	int res = 0;
	pr c = pr(x, y, d);

	while (c.x >= 0 && c.x < n && c.y >= 0 && c.y < m)
	{
		tmp.push_back(c);
		a[c.x][c.y] = 1;
		do
		{
			c.x += st[c.d][0];
			c.y += st[c.d][1];
		} while (c.x >= 0 && c.x < n && c.y >= 0 && c.y < m && s[c.x][c.y] == '.');
		if (c.x >= 0 && c.x < n && c.y >= 0 && c.y < m && a[c.x][c.y] == 1)
			return 0;
		if (c.x >= 0 && c.x < n && c.y >= 0 && c.y < m)
			c.d = getdir(c.x, c.y);
	}

	if (tmp.size() == 1)
		return -1;
	return 1;
}

int check(int x, int y)
{
	int d = getdir(x, y);
	int res = follow(x, y, d);
	if (res != -1)
		return res;
	d = (d+1) % 4;
	res = follow(x, y, d);
	if (res != -1)
		return res + 1;
	d = (d + 1) % 4;
	res = follow(x, y, d);
	if (res != -1)
		return res + 1;
	d = (d + 1) % 4;
	res = follow(x, y, d);
	if (res != -1)
		return res + 1;
	return res;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int TT;
	scanf("%d", &TT);
	for (int T = 0; T < TT; T++)
	{
		printf("Case #%d: ", T+1);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			scanf("%s", s[i]);
		int res = 0;
		memset(a, -1, sizeof(a));
		for (int i = 0; i < n && res != -1; i++)
		{
			for (int j = 0; j < m && res != -1; j++)
			{
				if (s[i][j] != '.' && a[i][j] == -1)
				{
					int t = check(i, j);
					if (t == -1)
						res = -1;
					else
						res += t;
				}
			}
		}
		if (res != -1)
			printf("%d\n", res);
		else
			printf("IMPOSSIBLE\n");
	}

	return 0;
}