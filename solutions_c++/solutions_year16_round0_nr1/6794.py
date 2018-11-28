#include<stdio.h>
int main()
{
	long long t,cs=1;
	scanf("%lld",&t);
	while(t--)
	{
		long long n,l,a[10]={0},c=0,i;
		scanf("%lld",&n);
		for(i=1;i<=10000000;i++)
		{
			l=n*i;
			while(l)	
			{
				if(a[l%10]==0)
				{
					a[l%10]=1;
					c++;
					if(c==10)
					goto label;
				}
				l/=10;
			}
			
		}
		label:;
		printf("Case #%d: ",cs++);
		if(c<10)
		printf("INSOMNIA\n");
		else
		printf("%lld\n",n*i);
		
	}
	return 0;
}
