/*
author:arushi
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
	long long int t,n,z,ans,x=0;
	scanf("%lld",&t);
	while(t--)
	{
		x++;
		scanf("%lld",&n);
		int count[10];
		memset(count,0,sizeof(count));
		int i=1,c=0,flag=0;
		int rem;
		z=n;
		while(c!=10 && z!=0)
		{
			n=i*z;;
			while(n>0)
			{
				rem=n%10;
				n=n/10;
				if(count[rem]==0)
				{
					count[rem]=1;
					c++;
				}
				if(c==10)
				{
					flag=1;					
					ans=i*z;
					break;

				}
			}
			if(c==10)
			{
				flag=1;				
				ans=i*z;
				break;
			}
			i++;
		}
		if(flag==0)
			printf("Case #%lld: INSOMNIA\n",x);
		else
			printf("Case #%lld: %lld\n",x,ans);
	}

	return 0;
}