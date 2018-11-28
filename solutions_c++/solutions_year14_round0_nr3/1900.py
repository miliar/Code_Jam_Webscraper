#include <cstdio>
#include <cstring>

const int MAXN = 55;

char a[MAXN][MAXN];

int r, c, m;
void output()
{
	for (int i = 0 ; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
			printf("%c", a[i][j]);
		puts("");
	}

}

bool f = false;

int dx[] = {-1,-1,-1,0,0,1,1,1};
int dy[] = {-1,0, 1, -1, 1, -1, 0, 1};
int p[MAXN][MAXN];

void go(int i, int j)
{
	for (int k = 0; k < 8; ++k)
	{
		int x = i + dx[k], y = j + dy[k];
		if (x < 0 || x == r || y < 0 || y == c)
			continue;
		if (p[x][y] == 0)
		{
			p[x][y] = -1;
			go(x, y);
		}
		p[x][y] = -1;
	}
}

void check()
{
	memset(p, 0, sizeof(p));
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j)
			if (a[i][j] == '.')
			{
				for (int k = 0; k < 8; ++k)
				{
					int x = i + dx[k], y = j + dy[k];
					if (x < 0 || x == r || y < 0 || y == c)
						continue;
					if (a[x][y] == '*')
						++p[i][j];
				}
			}
			else p[i][j] = -1;
	int rr = -1, cc;
	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
			if (p[i][j] == 0)
			{
				p[i][j] = -1;
				rr = i; cc = j;
				go(i, j);
				break;
			}
		if (rr != -1)
			break;
	}
	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j)
			if (p[i][j] != -1)
				return;
	a[rr][cc] = 'c';
	output();
	f = true;
}

void dfs(int x, int y, int rest)
{
	if (f)
		return;
	if (rest == 0)
	{
		check(); return;
	}
	if (y == c)
	{
		y = 0;
		x += 1;
	}
	if (x == r)
	{
		return;
	}
	a[x][y] = '.';
	dfs(x, y + 1, rest - 1);
	a[x][y] = '*';
	dfs(x, y + 1, rest);
}

int main()
{
	int T;
	scanf("%d", &T);


	for (int t = 1; t <= T; ++t)
	{
		scanf("%d%d%d", &r, &c, &m);

		printf("Case #%d:\n", t);
		memset(a, '*', sizeof(a));
		if (r * c - m == 1)
		{
			a[0][0] = 'c';
			output();
		}
		else {
			f = false;
			dfs(0, 0, r * c - m);
			if (!f)
				puts("Impossible");
		}
	}

	return 0;
}
