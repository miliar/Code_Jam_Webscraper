#include <stdio.h>
#include <string>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <iostream>
#define mod 1000000007
#define INT_MAX 2147483647
using namespace std;
int t, low[55], col[55], check[105], n;
int list[105][55], ans [55][55];
vector<pair<int, int> > cnt[50];

bool func(int i)
{
	if (i == n)return true;
	int now = 30000, tmp = 0, a, b;
	bool l = true;
	a = b = -1;
	for (int j = 0; j < cnt[i].size() && tmp<2; j++)
	{
		if (cnt[i][j].first <= now &&!check[cnt[i][j].second])
		{
			now = cnt[i][j].first;
			tmp++;
			if(a<0)a = cnt[i][j].second;
			else b = cnt[i][j].second;
			
		}
	}
	check[a] = 1;
	if (b >= 0) check[b] = 1;
	low[i] = a;
	col[i] = b;
	for (int j = 0; j < n; j++)
	{
		if (j < i && (ans[i][j] != list[a][j]&&ans[i][j] >0))
		{
			l = false;
			break;
		}
		if (j < i &&ans[i][j]) ans[i][j] = list[a][j];
		if (j >= i) ans[i][j] = list[a][j];
	}
	if (l)
	{
		if (b>=0)
		{
			
			for (int j = 0; j < n; j++)
			{
				if (j < i && (ans[j][i] != list[b][j] && ans[j][i] > 0))
				{
					l = false;
					break;
				}
				if (j < i &&ans[j][i]) ans[j][i] = list[b][j];
				if (j >= i) ans[j][i] = list[b][j];
			}
		}
		if (l && func(i + 1)) return true;
	}

	low[i] = b;
	col[i] = a;
	l = true;
	for (int j = 0; j < n; j++)
	{
		if (j >= i) ans[i][j] = ans[j][i] = -1;
	}
	if (b >= 0)
	{
		for (int j = 0; j < n; j++)
		{
			if (j < i && (ans[i][j] != list[b][j] && ans[i][j] > 0))
			{
				l = false;
				break;
			}
			if (j < i &&ans[i][j]) ans[i][j] = list[b][j];
			if (j >= i) ans[i][j] = list[b][j];

		}
	}
	if (l)
	{
		for (int j = 0; j < n; j++)
		{
			if (j < i && (ans[j][i] != list[a][j] && ans[j][i] > 0))
			{
				l = false;
				break;
			}
			if (j < i &&ans[j][i]) ans[j][i] = list[a][j];
			if (j >= i) ans[j][i] = list[a][j];
		}
		if (l&&func(i + 1)) return true;
	}
	for (int j = 0; j < n; j++)
	{
		if (j >= i) ans[i][j] = ans[j][i] = -1;
	}

	check[a] = 0;
	if (b >= 0) check[b] = 0;
	low[i] = col[i] = -1;
	return false;

}


int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("bs.out", "w",stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		printf("Case #%d:", tt);
		scanf("%d", &n);
		for (int i = 0; i < n; i++) cnt[i].clear();
		for (int i = 0; i < 2*n-1; i++)
		{
			for (int j = 0; j < n; j++)
			{
				scanf("%d", list[i] + j);
				cnt[j].push_back({ list[i][j], i });
			}
		}
		memset(low, -1, sizeof(low));
		memset(ans, -1, sizeof(ans));
		memset(col, -1, sizeof(col));
		memset(check, 0, sizeof(check));
		for (int i = 0; i < n; i++) sort(cnt[i].begin(), cnt[i].end());
		func(0);
		for (int i = 0; i < n; i++)
		{
			if (low[i] < 0)
			{
				for (int j = 0; j < n; j++)
					printf(" %d", ans[i][j]);
				break;
			}
			if (col[i] < 0)
			{
				for (int j = 0; j < n; j++)
					printf(" %d", ans[j][i]);
				break;
			}
		}
		printf("\n");
	}
	return 0;
}
