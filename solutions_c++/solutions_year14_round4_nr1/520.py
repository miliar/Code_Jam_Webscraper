#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 10000 + 10;

int n, m, a[maxn];
bool b[maxn];

void solve()
{
	scanf("%d%d", &n, &m);
	for (int i = 0; i < n; ++i)
		scanf("%d", a + i);
	sort(a, a + n);
	memset(b, 0, sizeof(b));
	int ans = 0;
	for (int i = n - 1; i >= 0; --i)
		if (!b[i])
		{
			for (int j = i - 1; j >= 0; --j)
				if (!b[j] && a[i] + a[j] <= m)
				{
					b[j] = true;
					break;
				}
			++ans;
		}
	printf("%d\n", ans);
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
