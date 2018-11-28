#include <cstdio>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
using namespace std;
int a[1000001] = {0};
int main()
{
	int tot;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &tot);
	for (int tt = 1; tt <= tot; tt++)
	{
		int n, x;
		printf("Case #%d: ", tt);
		scanf("%d%d", &n, &x);
		for (int i = 1; i <= n; i++)
		{
			scanf("%d", &a[i]);
		}
		
		int ans = 0, j = n;
		if (n == 1) ans = 1;
		else
		{
		sort(a+1, a+n+1);
		for (int i = 1; i <= j;)
		{
			if (i == j){
				ans++;
				break;}
			else
			{
				if (a[i]+a[j] <= x)
				{
					ans++;
					i++;
					j--;
				} else
				{
					ans++;
					j--;
				}
			}
		}
		}
		printf("%d\n", ans);
	}
	return 0;
}
