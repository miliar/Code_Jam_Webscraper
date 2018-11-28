#include<cstdio>

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int n;
	int cas, t;
	scanf("%d", &t);
	for(cas = 1; cas <= t; cas ++)
	{
		scanf("%d", &n);
		int cnt = 0;
		int ans = 0;
		for(int i= 0; i <= n; i ++)
		{
			int d;
			scanf("%1d", &d);
			if(cnt >= i)cnt += d;
			if(cnt < i+1) 
			{
				ans += i + 1 - cnt;
				cnt = i+1;
			}
			//printf("Case #%d: %d\n", cas, ans);
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
