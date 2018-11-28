#include<stdio.h>
int main()
{
    freopen("inl2.in","r",stdin);
    freopen("outl2.txt","w",stdout);
    int t,cases=1;
    double c,f,x,rate,t1,t2,waste;
    scanf("%d",&t);
    while(t--)
    {
              scanf("%lf%lf%lf",&c,&f,&x);
              
              rate = 2 + f;
              waste = c/2.0;
              t1 = x/2.0;
              t2 = waste + x/rate;
              while(t1>t2)
              {
                          
                          t1 = t2;
                          waste += c/rate;
                          rate+=f;
                          t2 = waste + x/rate;
                          
                          
              }
              printf("Case #%d: %.7lf\n",cases++,t1);
    }
}
