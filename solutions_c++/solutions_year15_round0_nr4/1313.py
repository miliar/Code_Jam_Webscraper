#include <bits/stdc++.h>
using namespace std;
int main()
{
	long long a,b,c,d,i,j,l,sum,result,n,m,k,s,t,max1;
    b=0;
	scanf("%lld",&t);
	while(t--)
	{
        scanf("%lld%lld%lld",&a,&n,&m);
        if((n*m)%a)
        {
        	printf("Case #%lld: RICHARD\n",++b);
        	continue;
        }
        else if(a==3)
        {
        	if(n==3||m==3)
        	{
        		if(n==1||m==1)
        		{
        			printf("Case #%lld: RICHARD\n",++b);
                	continue;
        		}
        		else
        		{
        			printf("Case #%lld: GABRIEL\n",++b);
                	continue;
        		}
        	}
        	else
        	{
        		printf("Case #%lld: RICHARD\n",++b);
                continue;
        	}
        	
        }
        else if(a==4)
        {
        	if(n==2&&m==2)
        	{
        		printf("Case #%lld: RICHARD\n",++b);
                continue;
        	}
        	else
        	{
        		if((n==1||m==1)||(n==2||m==2))
        		{
        			printf("Case #%lld: RICHARD\n",++b);
                    continue;
        		}
        		else
        		{
        				printf("Case #%lld: GABRIEL\n",++b);
                    	continue;
        		}
        	}
        }
        else
		printf("Case #%lld: GABRIEL\n",++b);
                
	}
	return 0;
}




