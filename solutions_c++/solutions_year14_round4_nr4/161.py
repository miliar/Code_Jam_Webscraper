#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;


char str[10][1005];

int m, n;

int val[1005];

int tree[5][90][30];
int treesz[5];


void addStr(int x, int s)
{
	int v = 0;
	for (int i = 0; str[s][i] != 0; i++)
	{
		char cur = str[s][i] - 'A';
		if (tree[x][v][cur] == -1)
			tree[x][v][cur] = treesz[x]++;
		v = tree[x][v][cur];
	}
}

int ans = -1;
int anscnt = 0;

void upd()
{
	memset(tree, -1, sizeof tree);
	memset(treesz, 0, sizeof treesz);
	for (int i = 0; i < n; i++)
		treesz[i] = 1;

	for (int i = 0; i < m; i++)
	{
		addStr(val[i], i);
	}
	int curans = 0;
	for (int i = 0; i < n; i++)
	{
		curans += treesz[i];
		if (treesz[i] == 1)
			return;
	}
	if (ans < curans)
	{
		ans = curans;
		anscnt = 0;
	}
	if (curans == ans)
		anscnt++;
}

void gen(int i)
{
	if (i == m)
	{
		upd();
		return;
	}
	for (int j = 0; j < n; j++)
	{
		val[i] = j;
		gen(i + 1);
	}
}


void solve()
{
	scanf("%d%d", &m, &n);
	for (int i = 0; i < m; i++)
	{
		scanf("%s", str[i] );
	}
	gen(0);

	printf("%d %d", ans, anscnt);

	ans = -1;
	anscnt = 0;
}


int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		fprintf(stderr, "Case #%d: ", i);
		solve();
		printf("\n");
		fprintf(stderr, "OK\n");
	}


	return 0;
}