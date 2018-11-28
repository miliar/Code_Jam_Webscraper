#include <cstdio>

char str[1010];

int main()
{
	int T, n;
	scanf("%d", &T);
	for (int tt=1; tt<=T; ++tt)
	{
		scanf("%d%s", &n, str);
		int ans=0, sum=0;
		for (int i=0; i<=n; ++i)
		{
			int x=str[i]-'0';
			if (sum<i) ans+=i-sum, sum=i;
			sum+=x;
		}
		printf("Case #%d: %d\n", tt, ans);
	}
	return 0;
}

