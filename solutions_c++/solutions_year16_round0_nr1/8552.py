#include<bits/stdc++.h>
using namespace std;
int main() 
{
	long long int t,n,i,val,d,a[11],x,j,n1,count,k;
	memset(a,0,sizeof(a));
	scanf("%lld",&t);
	for(i=1;i<=t;i++)
	{
	    count=1;
	    //flag=0;
	    scanf("%lld",&n);
	    n1=n;
	    if(n==0)
	    {
	        printf("case #%lld: INSOMNIA\n",i);
	    }
	    else
	    {
	    	val=n1;
	    	 while(n1>0)
	        		{
	            		x=n1%10;
	            		n1=n1/10;
	            		a[x]=1;
	        		}
	        		//cout<<"printnig "<<a[0]<<endl;	
	        		j=0;
	        while(j<=9)
	        {
	        		
	        		if(a[j]==0)
	        		{
	        			count++;
	        			n1=n*count;
	        			val=n1;
	        			//printf("\nyaha hai mera n1==%d count==%d",n1,count);
	        			j=0;
					}
					else
					{
						j++;
					}
					 while(n1>0)
	        		{
	            		x=n1%10;
	            		n1=n1/10;
	            		a[x]=1;
	        		}
			}
	        printf("case #%lld: %lld\n",i,val);
	        count=0;
	        memset(a,0,sizeof(a));
		}
 	}
 	return 0;
}