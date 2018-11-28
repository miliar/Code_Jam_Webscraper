#include <bits/stdc++.h>

using namespace std;

int n, m;

char tab[105][105];

bool sciana(int x, int y)
{
	int dx = 0, dy = 0;
	if(tab[x][y] == '^')
		dx = -1;
	else if(tab[x][y] == 'v')
		dx = 1;
	else if(tab[x][y] == '<')
		dy = -1;
	else if(tab[x][y] == '>')
		dy = 1;
	for(int i = 1; ; i++)
	{
		int xx = x + dx * i;
		int yy = y + dy * i;
		if(xx < 1 || xx > n || yy < 1 || yy > m)
			return true;
		if(tab[xx][yy] != '.')
			return false;
	}
}

void przyp()
{
	scanf("%d%d", &n, &m);
	for(int i = 1; i <= n; i++)
		for(int j = 1; j <= m; j++)
			scanf(" %c", &tab[i][j]);
	int wyn = 0;
	for(int i = 1; i <= n; i++)
	{
		for(int j = 1; j <= m; j++)
		{
			char c = tab[i][j];
			if(c == '.')
				continue;
			tab[i][j] = '^';
			int l = 0;
			if(sciana(i, j))
				l++;
			tab[i][j] = 'v';
			if(sciana(i, j))
				l++;
			tab[i][j] = '<';
			if(sciana(i, j))
				l++;
			tab[i][j] = '>';
			if(sciana(i, j))
				l++;
			tab[i][j] = c;
			if(sciana(i, j))
			{
				wyn++;
				if(l == 4)
				{
					printf("IMPOSSIBLE\n");
					return;
				}
			}
		}
	}
	printf("%d\n", wyn);
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		przyp();
	}
	return 0;
}
