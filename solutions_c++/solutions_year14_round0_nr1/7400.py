//#define _CRT_SECURE_NO_WARNINGS
#include <cstdlib>
#include <cstdio>

void mofile(), input(int& n,int g[5][5]), solve(), output(int t), dongfile();

int u, v, a[5][5], b[5][5], c[17], count = 0, res= 0;

int main()
{
	mofile(); 
	int test;
	scanf("%d\n", &test);
	for (int i = 1; i <= test; i++)
	{
		input(u, a); input(v, b); solve(); output(i);
	}
}

void mofile()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("a.out", "w", stdout);
}

void input(int& n,int g[5][5])
{
	scanf("%d\n", &n);
	for (int i= 1; i <= 4; i++)
	{
		for (int j = 1; j <= 4; j++)
		{
			scanf("%d", &g[i][j]);
		}
		scanf("\n");
	}
}

void solve()
{
	for (int i = 1; i <= 17; i++)
	{
		c[i] = 0;
	}
	count = 0;
	for (int i = 1; i <= 4; i++)
	{
		c[a[u][i]] = 1;
	}

	for (int i = 1; i <= 4; i++)
	{
		if (c[b[v][i]] == 1)
		{
			count++;
			res = b[v][i];
		}
	}
}

void output(int t)
{
	if (count == 1)
	{
		printf("Case #%d: %d\n", t, res);
	}
	if (count > 1)
	{
		printf("Case #%d: Bad magician!\n", t);
	}
	if (count == 0)
	{
		printf("Case #%d: Volunteer cheated!\n", t);
	}
}