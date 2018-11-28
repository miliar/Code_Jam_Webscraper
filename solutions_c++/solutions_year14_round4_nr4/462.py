#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <string>
using namespace std;

const int maxn = 10000 + 10;

int n, m, tot, ans;
string a[maxn];
set<string> vis[maxn];
int p[maxn], b[maxn];

void calc()
{
	for (int i = 0; i < n; ++i)
	{
		vis[i].clear();
		if (!b[i])
			return;
	}
	for (int i = 0; i < m; ++i)
		for (int j = 0; j < a[i].size(); ++j)
			vis[p[i]].insert(a[i].substr(0, j + 1));
	int tmp = n;
	for (int i = 0; i < n; ++i)
		tmp += vis[i].size();
	if (ans < tmp)
	{
		ans = tmp;
		tot = 0;
	}
	if (ans == tmp)
		++tot;
}

void search(int cur)
{
	if (cur == m)
	{
		calc();
		return;
	}
	for (int i = 0; i < n; ++i)
	{
		p[cur] = i;
		++b[i];
		search(cur + 1);
		--b[i];
	}
}

void solve()
{
	ans = 0, tot = 0;
	scanf("%d%d", &m, &n);
	for (int i = 0; i < m; ++i)
		cin >> a[i];
	search(0);
	printf("%d %d\n", ans, tot);
}

int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
