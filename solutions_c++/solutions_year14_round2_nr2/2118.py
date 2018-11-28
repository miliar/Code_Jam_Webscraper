#include<stdio.h>
int main()
{
	int t,x=1;
	scanf("%d",&t);
	while(t--)
	{
		long long  a,b,k,i,j;
		unsigned long long count=0;
		scanf("%lld%lld%lld",&a,&b,&k);
		for(i=0;i<a;i++)
		{
		for(j=0;j<b;j++)
		if((i&j)<k)
		count++;
		}
		printf("Case #%d: %llu\n",x,count);
		x++;
	}
	return 0;
}
