#include <bits/stdc++.h>
using namespace std;
int main()
{
	long long a,b,c,d,i,j,l,sum,count,n,m,k,s,t;
	char str[1005];
	a=0;
	scanf("%lld",&t);
	while(t--)
	{
		scanf("%lld %s",&n,str);
		sum=0;
		count=0;
		sum+=str[0]-48;
		for(i=1;i<=n;i++)
		{
			
			if(str[i]!='0')
			{
				if(sum<i)
    			{
	    			count+=(i-sum);
		    		sum+=(i-sum);
			    }
     			sum+=str[i]-48;
			}
			
			
		}
		printf("Case #%lld: %lld\n",++a,count);
	}
	return 0;
}




