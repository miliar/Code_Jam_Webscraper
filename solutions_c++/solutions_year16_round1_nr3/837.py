#include <stdio.h>
#include <string>
#include <algorithm>
#include <queue>
#include <stdlib.h>
#include <vector>
#include <iostream>
#define mod 1000000007
#define INT_MAX 2147483647
using namespace std;
int t,  n, g[1005], a,ind[1005], cnt[1005], check[1005], mx, ans;
vector<int> two;
int dfs(int i)
{
	check[i] = 1;
	
	if (!check[g[i]])
		return dfs(g[i]) + 1;
	return 1;
}
int main() {
	freopen("C-large.in", "r", stdin);
	freopen("cs.out", "w",stdout);
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		ans = 0;
		printf("Case #%d:", tt);
		scanf("%d", &n);
		memset(g, 0, sizeof(g));
		memset(cnt, 0, sizeof(cnt));
		memset(check, 0, sizeof(check));
		memset(ind, 0, sizeof(ind));
		two.clear();
		queue<int> q;
		for (int i = 1; i <= n; i++)
			scanf("%d", &a), g[i] = a, ind[a]++;
		for (int i = 1; i <= n; i++)
		{
			if (!ind[i])q.push(i);
		}
		while (!q.empty())
		{
			int now = q.front();
			q.pop();
			a = cnt[now] + 1;
			if (cnt[g[now]] < a) cnt[g[now]] = a;
			ind[g[now]]--;
			if (!ind[g[now]]) q.push(g[now]);
		}
		int tmp;
		mx = 0;
		for (int i = 1; i <= n; i++)
		{
			
			if (ind[i]&& !check[i])
			{
				tmp = dfs(i);
				if (tmp == 2)
				{
					tmp += cnt[i] + cnt[g[i]];
					two.push_back(tmp);
				}
				else mx = max(tmp, mx);
			}
		}
		tmp = 0;
		if (two.size()>2)
			tt = tt;
		for (int i = 0; i < two.size(); i++)
			tmp += two[i];
		ans = max(mx, tmp);
		printf(" %d\n", ans);
	}
	return 0;
}

