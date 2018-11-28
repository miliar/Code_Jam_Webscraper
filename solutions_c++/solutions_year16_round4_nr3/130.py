#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 200;
int n, k, r, c, Find;
int pa[N][2], a[N][N], f[N];

void init()
{
	scanf("%d%d", &r, &c);
	for (int i = 1; i <= r + c; ++ i)
		scanf("%d%d", &pa[i][0], &pa[i][1]);
}

int get(int u)
{
	if (f[u] != u) f[u] = get(f[u]);
	return f[u];
}

void add(int u, int v)
{
	f[get(u)] = get(v);
}

int ch(int num, int ref)
{
	return (num - 1) * 4 + ref + 2 * (r + c);
}

bool check()
{
	int nn = r * c * 4 + 2 * (r + c);
	for (int i = 1; i <= nn; ++ i) f[i] = i;
	for (int i = 1; i <= r; ++ i)
		for (int j = 1; j <= c; ++ j)
		{
			int bln = (i - 1) * c + j;
			if (j > 1) add(ch(bln - 1, 3), ch(bln, 1));
			if (i > 1) add(ch(bln - c, 4), ch(bln, 2));
			if (a[i][j] == 0) add(ch(bln, 1), ch(bln, 2)), add(ch(bln, 3), ch(bln, 4));
			else add(ch(bln, 1), ch(bln, 4)), add(ch(bln, 2), ch(bln, 3));
		}
	for (int i = 1; i <= c; ++ i)
	{
		add(i, ch(i, 2));
		add(c + r + c - i + 1, ch((r - 1) * c + i, 4));
	}
	for (int i = 1; i <= r; ++ i)
	{
		add(c + r + c + r - i + 1, ch((i - 1) * c + 1, 1));
		add(c + i, ch(i * c, 3));
	}
	for (int i = 1; i <= r + c; ++ i)
	{
		if (get(pa[i][0]) != get(pa[i][1])) return 0;
	}
	return 1;
}

void dfs(int x, int y)
{
	if (x > r)
	{
		if (check()) Find = 1;
		return;
	}
	if (y > c)
	{
		dfs(x + 1, 1);
		return;
	}
	a[x][y] = 0;
	dfs(x, y + 1);
	if (Find) return;
	a[x][y] = 1;
	dfs(x, y + 1);
	if (Find) return;
}

int main()
{
	//freopen("3.in", "r", stdin);
	//freopen("3.out", "w", stdout);
	int T, Case = 0;
	scanf("%d", &T);
	while (T --)
	{
		init();
		Find = 0;
		dfs(1, 1);
		printf("Case #%d:\n", ++ Case);
		if (!Find)
			puts("IMPOSSIBLE");
		else 
		{
			for (int i = 1; i <= r; ++ i)
			{
				for (int j = 1; j <= c; ++ j)
				{
					if (a[i][j] == 0) printf("/");
					else printf("\\");
				}
				puts("");
			}
		}
	}		
}