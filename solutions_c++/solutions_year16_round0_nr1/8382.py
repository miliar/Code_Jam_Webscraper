#include <iostream>
#include <map>
#include <string>
#include <bits/stdc++.h>

#define llu long long unsigned int
#define lld long long int
#define FOR(i,N) for(i=0;i<(N);i++)


using namespace std;
int main ()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	long long int n,t,i,ar[20],ans,j,re,ses,total,cas=1;
	scanf("%lld",&t);
	while(t--)
	{
	    scanf("%lld",&n);
	    if(n==0)
	    {printf("Case #%lld: INSOMNIA\n",cas++);}
	    else
	    {ans=n;
	    for(i=1;i<100000;)
	    {re=ans=i*n;
	        for(ans;ans>0;)
	        {
	            ses=ans%10;
	            ans=ans/10;
	            ar[ses]=1;
	        }
	        for(j=0,total=0;j<=9;j++)
	        {
	            total=total+ar[j];
	        }
	        if(total==10)
	        {i=-1;
	        total=0;
	        for(j=0;j<=9;j++)
	        ar[j]=0;
	            break;
	        }
	        else
	        {i++;
	        }

	    }printf("Case #%lld: %lld\n",cas++,re);}
	}
  return 0;
}


