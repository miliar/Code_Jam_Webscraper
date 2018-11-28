#include <stdio.h>
long long  t,a,b;
int main()
{
	long long i,j,k,count,c,d;
	char x;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%lld",&t);

	for(i=1; i<=t; i++)
	{
		scanf("%lld%c%lld",&a,&x,&b);
		while(a>1 && a%2 == 0 && b%2 == 0)
		{
			a /= 2;
			b /= 2;
		}
		count = 0;
		c = 1;
		while(b%(c*2) == 0)
			c *=2;
		if(b/c >1)
		{
			d = b/c;
			if(a>d && a%d)
				printf("Case #%d: impossible\n",i);
			
			else if(a<d && d%a)
				printf("Case #%d: impossible\n",i);
			else
			{
				while(b>a)
			{
				b/=2;
				count++;
			}
				printf("Case #%lld: %lld\n",t,count);
			}
		}
		else
		{
			while(b>a)
			{
				b/=2;
				count++;
			}
			
			printf("Case #%lld: %lld\n",i,count);
		}
	}
}
