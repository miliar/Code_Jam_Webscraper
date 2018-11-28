#include<stdio.h>
#include<string.h>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    double c,f,x;
    int T;
    scanf("%d",&T);
    int cas=1;
    while(T--)
    {
     scanf("%lf%lf%lf",&c,&f,&x);
     printf("Case #%d: ",cas++);
     double ans=0;
     double rat=2,hav=0;
     if(c>=x){printf("%.7lf\n",x/rat);continue;}
     while(hav<x)
     {
         ans+=c/rat;
         hav+=c;
         if((x-hav)/rat<=(x/(rat+f))){ans+=(x-hav)/rat;break;}
         else
         {
             hav-=c;
             rat+=f;
         }
     }
     printf("%.7lf\n",ans);
    }
}
