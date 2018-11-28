#include<stdio.h>
#include<string.h>
long long int a,b,c;
int main()
{
	freopen("A-small-attempt0 (1).in","rt",stdin);
	freopen("output.txt","wt",stdout);
	int t,v;
	scanf("%d",&t);
	for(v=0; v<t; v++)
	{
		scanf("%lld %lld",&a,&b);
		a = 2*a+1;
		c=0;
		for(;b>=0;a+=4)
		{
			b-=a;
			c++;
		}
		printf("Case #%d: %lld\n",v+1,c-1);
	}
}