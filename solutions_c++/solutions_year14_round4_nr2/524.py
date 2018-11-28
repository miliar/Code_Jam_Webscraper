#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 10000 + 10;

int n, m, a[maxn], p[maxn], pos;
int pre[maxn], suf[maxn];

bool cmp(int p, int q)
{
	return a[p] < a[q];
}

void solve()
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
	{
		scanf("%d", a + i);
		p[i] = i;
	}
	sort(p, p + n, cmp);
	for (int i = 0; i < n; ++i)
		a[p[i]] = i;
	pos = p[n - 1];
	pre[0] = suf[n - 1] = 0;
	for (int i = 1; i < n; ++i)
	{
		pre[i] = 0;
		for (int j = 0; j < i; ++j)
			if (a[i] < a[j])
				++pre[i];
	}
	for (int i = n - 2; i >= 0; --i)
	{
		suf[i] = 0;
		for (int j = n - 1; j > i; --j)
			if (a[i] < a[j])
				++suf[i];
	}
	/*int ans = suf[0] + pos;
	if (ans > pre[n - 1] + (n - 1 - pos))
		ans = pre[n - 1] + (n - 1 - pos);
	for (int i = 1; i < n - 1; ++i)
	{
		int tmp;
		if (pos > i)
			tmp = pos - i + pre[i - 1] + suf[i];
		else
			tmp = i - pos + pre[i] + suf[i + 1];
		if (ans > tmp)
			ans = tmp;
	}*/
	int ans = 0;
	for (int i = 0; i < n; ++i)
		if (pre[p[i]] < suf[p[i]])
			ans += pre[p[i]];
		else
			ans += suf[p[i]];
	printf("%d\n", ans);
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
