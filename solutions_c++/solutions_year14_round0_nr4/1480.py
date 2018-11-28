#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 10000;
int n, m, c[maxn];
double a[maxn], b[maxn];

int find(double x)
{
	int tmp = -1;
	for (int i = 0; i < n; ++i)
		if (!c[i])
		{
			if (tmp == -1)
				tmp = i;
			if (b[i] > x)
			{
				tmp = i;
				break;
			}
		}
	c[tmp] = 1;
	return tmp;
}

void solve()
{
	scanf("%d", &n);
	for (int i = 0; i < n; ++i)
		scanf("%lf", a + i);
	for (int i = 0; i < n; ++i)
		scanf("%lf", b + i);
	sort(a, a + n);
	sort(b, b + n);
	int ans = 0, j = 0;
	for (int i = 0; i < n; ++i)
	{
		if (a[i] > b[j])
		{
			++j;
			++ans;
		}
		else
		{
			if (a[i] > b[n - 1 - i + j])
				++ans;
		}
	}
	printf("%d ", ans);
	ans = 0;
	memset(c, 0, sizeof(c));
	for (int i = 0; i < n; ++i)
	{
		int k = find(a[i]);
		if (a[i] > b[k])
			++ans;
	}
	printf("%d\n", ans);
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
