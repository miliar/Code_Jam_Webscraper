#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<stack>
#define oo 105
using namespace std; 
double C,F,X,ans,nowt,nowc,temp;
int main()
{
      int cases,T,i;
      freopen("B-large.in","r",stdin);
      freopen("output.txt","w",stdout);
      scanf("%d",&T);
      for (cases=1;cases<=T;cases++)
      {
              scanf("%lf%lf%lf",&C,&F,&X);
              nowt=0,nowc=2,ans=-1;
              for (i=0;;i++)
              {
                     temp=nowt+X/nowc;
                     if (ans<0 || ans>temp) ans=temp; 
                     nowt+=C/nowc; 
                     nowc+=F;
                     if (nowt>=ans) break;
              }
              printf("Case #%d: %.7lf\n",cases,ans); 
      }
      return 0;
}
