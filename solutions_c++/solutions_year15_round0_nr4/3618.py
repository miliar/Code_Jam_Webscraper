#include<bits/stdc++.h>

int main()
{
  int t,c,x,n,r;
  scanf("%d",&t);
  n=t;
  
  char ch='r';
  
  while(t--)
    {
      ch='r';
      
      scanf("%d %d %d",&x,&r,&c);
      if(x==1)
	ch='g';
      else if(x==2)
	{
	  if(r==2 || r==4)
	    ch='g';
	  else if(r==1 || r==3)
	    {
	      if(c==2 || c==4)
		ch='g';
	    }
	}
      else if(x==3)
	{
	  if( (r==2 && c==3) || (r==3 && c==2) || (r==3 && c==3) || (r==3 && c==4) || (r==4 && c==3) ) 
	    ch='g';
	}
      else if(x==4)
	{
	  if((r==4 && c==4) || (r==3 && c==4) || (r==4 && c==3))
	    ch='g';
	}
      if(ch=='g')
	printf("Case #%d: GABRIEL\n",n-t);
      else
	printf("Case #%d: RICHARD\n",n-t);

    }
  return 0;
  
}
