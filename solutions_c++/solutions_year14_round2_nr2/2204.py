#include<stdio.h>
#include<math.h>
#include<stdlib.h>
int main()
{
	long long int a,b,k,t;
	
	scanf("%lld",&t);
	for(long long int x=1;x<=t;x++)
	{
		scanf("%lld %lld %lld",&a,&b,&k);
		long long temp=0,count=0;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				temp=i&j;
			
				if(temp<k)
				{
					count++;
				}	
			}
		}
		printf("Case #%lld: %lld\n",x,count);
	}	
}