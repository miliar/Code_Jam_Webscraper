#include <cstdio>
#include <cstring>
int T,n,i,x,s[1011],min,ans,cas;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &n);
		for (i=1; i<=n; ++i) scanf("%d", &s[i]);
		ans = 1000000;
		for (min=1; min<=1000; ++min)
		{
			x = 0;
			for (i=1; i<=n; ++i) x += (s[i]-1)/min;
			if (x+min < ans) ans = x+min;
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
	return 0;
}
			
