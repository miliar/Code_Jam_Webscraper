#include<stdio.h>
int main()
{
  int t,m;
  scanf("%d",&t);
  m=t;
  while(t>0)
  {
     int x,r,c;
     scanf("%d %d %d",&x,&r,&c);
     if(x==1)
      printf("Case #%d: GABRIEL\n",m-t+1);
     else if(x==2)
      {
        if(((r*c)%2==0))
          printf("Case #%d: GABRIEL\n",m-t+1);
        else
          printf("Case #%d: RICHARD\n",m-t+1);
     }
    else if(x==3)
    {
      if(((r*c)%3==0) && ((r*c)!=3))
          printf("Case #%d: GABRIEL\n",m-t+1);
        else
          printf("Case #%d: RICHARD\n",m-t+1);
    }
    else if(x==4)
    {
      if(((r*c)==12) || ((r*c)==16))
        printf("Case #%d: GABRIEL\n",m-t+1);
      else
        printf("Case #%d: RICHARD\n",m-t+1);
    }
   t--;
 }
  return 0;
}
