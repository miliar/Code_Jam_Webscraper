#include<stdio.h>

double ans[105];

double cookie()
{
   double c,f,x,p,t,min,tx,tf=0.0;
   scanf("%lf%lf%lf",&c,&f,&x);
   p=2.0;
   for(int i=0;i<=x;i++)
   {
     if(i>0)
     { 
       tf+=c/p;
       p+=f;
     }
     tx=x/p;
     t=tx+tf;
     if(t<min||i==0)
      min=t;
   }
   return min;
}

int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
     ans[i]=cookie();
    for(int i=1;i<=n;i++)
     printf("Case #%d: %.7lf\n",i,ans[i]);
    scanf(" ");
    return 0;
}
