#include<stdio.h>
int main()
{ freopen("B-large.in","r",stdin);
  freopen("out.txt","w",stdout);
   int t,k;
  scanf("%d",&t);
  for(k=1;k<=t;k++)
  {
    double c,f,x,t1=0,t2=0,rate=2,ck1,ck2,t3=0,x1,x2;
    scanf("%lf %lf %lf",&c,&f,&x);
    while(1)
    {
      t1=x/rate;
      t3=t3+t1;
      t2+=c/rate+(x/(rate+f));
      if(t3<=t2)
      {
        printf("Case #%d: %.7lf\n",k,t3);
        break;
      }
      else
      {   t2-=x/(rate+f);
          t3+=c/rate;
          t3=t3-t1;
         rate=rate+f;
      }
    }
  }
  return 0;
}
