#include<algorithm>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int T;
int main()
{
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);    
    int i,j,k;
    double p,q,r;
    double t,tt,ttt;
    double C,F,X;
    double LIM,rate;
scanf("%d",&T);
for(int ii=1;ii<=T;ii++)
{
   scanf("%lf %lf %lf",&C,&F,&X);
   LIM=999999999.0;
   p=0.0;
   rate=2.0;
   while(1)
    {
      q=X/rate;
      t=p+q;
      if(t<=LIM)LIM=t;
      else break;
      p+=(C/rate);
      rate+=F;
    }
   printf("Case #%d: ",ii);
   printf("%.7lf",LIM);   
   if(ii<=T-1)printf("\n");  
        
        
}
    
    
    scanf(" ");
    return 0;
}
