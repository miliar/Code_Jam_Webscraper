#include <iostream>
#include<stdio.h>
#include<cstdio>
using namespace std;
int main (void)
{
   int T,l;
  double X,F,C,x=0.0,u=0.0,v=0.0,k=0.0,t=0.0;
   
    freopen ("B-large.in","r",stdin);
    freopen("B2-output.txt","w",stdout);
    scanf("%d", &T);
   for(l=1;l<=T;l++)
    {
    x=0.0;
	u=0.0;
	v=0.0;
	k=0.0;
	t=0.0;
   scanf("%lf",&C);
   scanf("%lf",&F);
   scanf("%lf",&X);
   while(u>=v)
   {
   	u=X/(2+(x*F));
   	v=((C/(2+(x*F)))+(X/(2+((x+1)*F))));
   	x=x+1.0;
   }
   x=x-1.0;
    while(t<x)
   {
   	k=k+(C/(2+(t*F)));
   	t=t+1.0;
   }
  
   printf("Case #%d: ",l);
   printf("%.7lf",(u+k));
   printf("\n");
    }
return(0);
}
