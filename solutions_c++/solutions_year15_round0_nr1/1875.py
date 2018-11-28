#include <cstdio>

int T,S,sum;

int main()
{
	scanf("%d",&T);
	for (int t=1;t<=T;++t)
	{
		scanf("%d%*c",&S);
		sum=0;
		int ans=0;
		for (int i=0;i<=S;++i)
		{
			if (sum<i)
			{
				ans+=i-sum;
				sum=i;
			}
			sum+=getchar()-'0';
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
