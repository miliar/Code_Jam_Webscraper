#include <stdio.h>
int main()
{
	freopen( "A-large.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	 long long int n,t,i,j,sum,rsv,lol,ld,a[10];
	scanf("%lld",&t);
	for(lol=1;lol<=t;lol++)
	{
		scanf("%lld",&n);
		if(n==0)
		{
			printf("Case #%lld: INSOMNIA\n",lol);continue;
		}
		for(i=0;i<10;i++)
		{
			a[i]=0;
		}
		j=0;
		for(i=1;;i++)
		{
			rsv=i*n;
			while(rsv!=0)
			{
				ld=rsv%10;rsv/=10;
				if(a[ld]==0)
				{
					a[ld]=1;
					for(j=0;j<10;j++)
					{
						if(a[j]==0)
						break;
					}
					if(j==10)
					{
						break;
					}
				}
			}
			if(j==10)break;
		}
		printf("Case #%lld: %lld\n",lol,i*n);
	}
	return 0;
}
		
