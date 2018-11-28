#include <cstdio>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
using namespace std;
int a[10001] = {0};
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int tot;
	scanf("%d", &tot);
	for (int tt = 1; tt <= tot; tt++)
	{
		int n;
		printf("Case #%d: ", tt);
		scanf("%d", &n);
		for (int i = 1; i <= n; i++)
			scanf("%d", &a[i]);
		int ans = 0, m = n;
		for (int i = 1; i <= n; i++)
		{
			int vmax = -1;
			for (int j = 1; j <= m; j++)
			{
				if (vmax == -1 || a[vmax] > a[j])
					vmax = j;
			}
			if ((vmax -1) < (m-vmax))
				ans += (vmax-1);
			else
				ans += (m-vmax);
			for (int j = vmax+1; j <= m; j++)
				a[j-1] = a[j];
			m--;
		}
		printf("%d\n", ans);
	} 
	return 0;
}
