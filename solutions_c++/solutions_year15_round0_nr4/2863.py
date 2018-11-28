#include<stdio.h>
#include<math.h>
int main()
{
freopen("input.txt","r",stdin);
freopen("output1.txt","w",stdout);

    long long int t,j=1,i,changes,count,x=0,r=0,c=0;
    scanf("%lld",&t);

    while(t--)
    {
    
    scanf("%lld%lld%lld",&x,&r,&c);
   
    changes=x-1;
   
	 count=r*c;
     
	    
	   if((count%x)!=0)
	    {
	    printf("Case #%lld: RICHARD\n",j);
	    j++;
	    }
	    
	    else	
	    {
		    if(changes>r || changes>c)
		    {
		    printf("Case #%lld: RICHARD\n",j);
		    j++;	
		    }
		    else
		    {
		    printf("Case #%lld: GABRIEL\n",j);
		    j++;
		    }
	    }
    }
    return 0;
    }
