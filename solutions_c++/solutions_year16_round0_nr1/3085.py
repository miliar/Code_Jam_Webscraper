#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
int vis[20];
int main()
{
	int i, j, ncase, tt = 0;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &ncase);
	while (ncase--)
	{
		long long a;
		int tot = 0, flag = 0;
		memset(vis, 0, sizeof(vis));
		scanf("%lld", &a);
		for (i = 0; i<1000000; i++)
		{
			long long x = a*(i + 1);
			while (x)
			{
				int aa = x % 10;
				if (!vis[aa])
					vis[aa]++, tot++;
				x /= 10;
			}
			if (tot >= 10)
			{
				flag = 1;
				break;
			}
		}
		if (flag)
			printf("Case #%d: %lld\n", ++tt, a*(i + 1));
		else
			printf("Case #%d: INSOMNIA\n", ++tt);
	}
	return 0;
}
