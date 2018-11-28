#include <cstdio>
#include <algorithm>

using namespace std;

int n, m, a[111][111], r[111], c[111], ttt;

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.txt", "w", stdout);
	scanf("%d", &ttt);
	for (int it = 1; it <= ttt; it++)
	{
		scanf("%d%d", &n, &m);
		printf("Case #%d: ", it);
		memset(r, 0, sizeof(r));
		memset(c, 0, sizeof(c));
		memset(a, 0, sizeof(a));
		for (int i = 1; i<=n; i++)
			for (int j = 1; j<=m; j++) 
			{
				scanf("%d", &a[i][j]);
				r[i] = max(r[i], a[i][j]);
				c[j] = max(c[j], a[i][j]);
			}
		bool ok = true;
		for (int i = 1; i<=n; i++) 
			for (int j = 1; j<=m; j++)
				if (min(r[i], c[j]) != a[i][j])
				{
					ok = false;
					break;
				}
	        if (ok) printf("YES\n"); else printf("NO\n");
	}
	return 0;
}