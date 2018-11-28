#include<bits/stdc++.h>
char a[2000];
int shy[2000];
typedef long long ll;


int main()
{

  int smax,n,i,j,t;
  ll count=0,newp=0;
  
  scanf("%d",&t);
  n=t;
  
  while(t--)
    {
      count=0;
      newp=0;
      
      scanf("%d",&smax);
      scanf("%s",a);
      for(i=0;i<=smax;i++)
	shy[i]=(int)(a[i]-'0');
      
      
      count=shy[0];
      
      for(i=1;i<=smax;i++)
	{
	  if(shy[i]!=0)
	    {

	      if(i>count)
		{

		  newp+=i-count;
		  count+=newp+shy[i];
		  		  
		}
	      else
		count+=shy[i];
	           
	    }
	}
      printf("Case #%d: %lld\n",n-t,newp);
    }
  
  return 0;
}
  
	  



    
