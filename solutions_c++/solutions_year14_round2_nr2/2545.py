#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,x=0;
	long long int a,b,k,c;
	scanf("%d",&t);
	while(t--)
	{
		c=0;
		x++;
		scanf("%lld %lld %lld",&a,&b,&k);
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if((i&j)<k)
					c++;
			}
		}
		printf("Case #%d: %lld\n",x,c);
		
	}
	return 0;
	

}