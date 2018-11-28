#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

const int MAXM = 1000 + 10;
const int MAXN = 100 + 10;
const int MAXL = 100 + 10;

char s[MAXM][MAXL];
int len[MAXM];
int c[MAXM];

int m, n;
int ans, ans_cnt;
int t[10000][30];

int cnt;

int insert(int x, int tn)
{
	int ret = 0;
	int node = 0;
	for (int i = 0; i < len[x]; ++i)
	{
		int p = s[x][i] - 'A';
		if (t[node][p] == -1)
		{
			++cnt;
			t[node][p] = cnt;
			for (int j = 0; j < 30; ++j)
				t[cnt][j] = -1;
		}
		node = t[node][p];
	}
}

void check()
{
	int r[MAXN];
	for (int i = 0; i < n; ++i)
		r[i] = 0;
	for (int i = 0; i < m; ++i)
		++r[c[i]];
	for (int i = 0; i < n; ++i)
		if (r[i] == 0)
			return;
	int tmp = 0;
	for (int j = 0; j < n; ++j)
	{
		cnt = 0;
		for (int i = 0; i < 30; ++i)
			t[0][i] = -1;
		for (int i = 0; i < m; ++i)
		{
			if (c[i] == j)
				insert(i, c[i]);
		}
		tmp += cnt;
	}
	if (tmp > ans)
	{
		ans = tmp;
		ans_cnt = 1;
	}
	else if (tmp == ans)
		++ans_cnt;
}

void dfs(int x)
{
	if (x == -1)
	{
		check();
		return;
	}
	for (int i = 0; i < n; ++i)
	{
		c[x] = i;
		dfs(x - 1);
	}
}

int main()
{
	int T; 
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt)
	{
		scanf("%d%d", &m, &n);
		for (int i = 0; i < m; ++i)
		{
			scanf("%s", s[i]);
			len[i] = strlen(s[i]);
		}
		ans = 0;
		ans_cnt = 0;
		dfs(m - 1);
		printf("Case #%d: %d %d\n", tt, ans + n, ans_cnt);
	}

	return 0;
}
