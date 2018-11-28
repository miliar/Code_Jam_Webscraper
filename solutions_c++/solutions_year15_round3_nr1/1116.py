#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<limits.h>
#include<vector>
using namespace std;
int main()
{
    freopen("A-large (2).in","r",stdin); freopen("gcj1coutlarge.txt","w",stdout);
	long long int T,t,r,c,k,w,ans,val;
	scanf("%lld",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%lld %lld %lld",&r,&c,&w);
		val=0;
		k=0;
		ans=0;
		while(k<=c)
		{
                   k=k+w;
                   if(k<=c)
                   val++;
                   else
                   break;
                   }
                   
			k=c;
			while(k>0)
			{
				k=k-w;
				if(k>0)
				{
					ans++;
				}
				else
				{
					break;
				}
			}
			ans=ans+w+val*(r-1);
			
		printf("Case #%lld: %lld\n",t,ans);
	}
	return 0;
}
