#include <stdio.h>
int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	long long int n,t,i,sum,rsv,lol;
	char a[1010];
	scanf("%lld",&t);
	for(lol=1;lol<=t;lol++)
	{
		scanf("%lld%s",&n,&a);
		sum=0;rsv=0;
		for(i=0;i<=n;i++)
		{
			if(sum<i&&a[i]>'0')
			{
				rsv=rsv+i-sum;
				sum=i;
			}
			sum=sum+a[i]-'0';
//			printf("%lld%lld\n",rsv,sum);
		}
		printf("Case #%lld: %lld\n",lol,rsv);
	}
}
		
