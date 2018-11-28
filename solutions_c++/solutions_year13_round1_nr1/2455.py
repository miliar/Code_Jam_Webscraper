#include <stdio.h>

int main()
{
    int i,T,m,n,x;
    scanf("%d",&T);
    long long r,t;
    for(i=0;i<T;i++)
    {
              scanf("%lld",&r);
              scanf("%lld",&t);
              double b= t;
              m=1;
              n=0;
              x=0;

              do
              {
              b -= (2*r+m+n);
              m+=2;
              n+=2;
              x++;
              }while(b>0);
              if(b<0)
                     x--;
printf("Case #%d: %d\n",i+1,x);
}
return 0;
}
