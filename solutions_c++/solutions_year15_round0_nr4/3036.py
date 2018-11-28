#include<bits/stdc++.h>
using namespace std;
#define ll long long
 
int main()
{
	ll x,r,c;
	ll t,j;
    FILE *fp,*fp1;
	
	fp=freopen("D-small-attempt6.in","r",stdin);
	fp1=freopen("out1.text","w+",stdout);

    scanf("%lld",&t);
    
    for(j=1;j<=t;j++)
    {
    	scanf("%lld %lld %lld",&x,&r,&c);
    	ll temp;
		if(r>c)
		{
			temp=r;
			r=c;
			c=temp;
		}
		
		if(x==1)
    	{	   
    	    	printf("Case #%lld: GABRIEL\n",j);
		}
		else if(x==2)
		{
			if(x>(r*c))
			    printf("Case #%lld: RICHARD\n",j);
	        else if(((r*c)%2)==0)
	            printf("Case #%lld: GABRIEL\n",j);
	        else
				printf("Case #%lld: RICHARD\n",j);
		}
		else if(x==3)
		{
			 	if(x>=(r*c))
			       printf("Case #%lld: RICHARD\n",j);
			    else if((r*c)%3)
				   printf("Case #%lld: RICHARD\n",j);
	             else 
				 {
				 
		               printf("Case #%lld: GABRIEL\n",j);
	     		    
				 } 
		}
		else 
		{
			if(c==4)
			{
				if(r>=3)
		               printf("Case #%lld: GABRIEL\n",j);
	     		 else 
	                 printf("Case #%lld: RICHARD\n",j);			   
	    		 
			}
			else
			 printf("Case #%lld: RICHARD\n",j);			   
		}
	}
	fclose(stdin);
    fclose(stdout);
	return 0;
}
