#include <cstdio>
int T,n,ans,now,cas,i,ch;

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &n);
		ans = now = 0;
		for (i=0; i<=n; ++i)
		{
			for (ch=getchar(); ch<=32; ch=getchar());
			if (ch > 48)
			{
				if (now < i) ans += i-now, now = i;
				now += ch-48;
			}
		}
		printf("Case #%d: %d\n", ++cas, ans);
	}
	return 0;
}
			
