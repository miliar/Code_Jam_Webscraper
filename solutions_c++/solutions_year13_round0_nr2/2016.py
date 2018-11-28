#include <cstdio>
#include <algorithm>

using namespace std;

int a[1000][1000];

int main(void)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t)
	{
		int n, m;
		scanf("%d%d", &n, &m);
		int h[1000], v[1000];
		for (int i = 0; i < max(n, m); ++i)
		{
			h[i] = v[i] = -1000;
		}
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				scanf("%d", &a[i][j]);
				h[i] = max(h[i], a[i][j]);
				v[j] = max(v[j], a[i][j]);
			}
		}
		bool flag = true;
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				flag &= a[i][j] == min(h[i], v[j]);
			}
		}
		if (flag)
		{
			printf("Case #%d: YES\n", t + 1);
		}
		else
		{
			printf("Case #%d: NO\n", t + 1);
		}
	}
	return 0;
}