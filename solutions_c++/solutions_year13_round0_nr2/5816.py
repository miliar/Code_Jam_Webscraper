#include <cstdio>
#include <cstdlib>
using namespace std;
int T, n, m, x[110], y[110], a[110][110], w;
bool flag;
int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= 100; i++) x[i] = y[i] = 0;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
			{
				scanf("%d", &a[i][j]);
				if (a[i][j] > x[i]) x[i] = a[i][j];
				if (a[i][j] > y[j]) y[j] = a[i][j];
			}
		flag = 0;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				if (x[i] != a[i][j] && y[j] != a[i][j]) flag = 1;
		printf("Case #%d: ", ++w);
		if (flag) printf("NO\n");
		else printf("YES\n");
	}
	return 0;
}
