#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int T,ca=0,n,m;
  scanf("%d",&T);
  while(T--)
  {
   scanf("%d",&n);
   printf("Case #%d: ", ++ca);
   if (n==1){
    double x,v,x1,r1;
    scanf("%lf%lf%lf%lf",&v,&x,&r1,&x1);
    if (fabs(x1-x)>1e-10) 
      puts("IMPOSSIBLE");
    else printf("%.10f\n", v/r1);
  }
   if (n==2){
    double x,v,x1,r1,x2,r2;
    scanf("%lf%lf%lf%lf%lf%lf",&v,&x,&r1,&x1,&r2,&x2);
    if (((x1-x)>1e-10&&(x2-x)>1e-10)||((x1-x)<1e-10*(-1)&&(x2-x)<(1e-10)*(-1)))
      {puts("IMPOSSIBLE");continue;}
    if (fabs(x1-x)<1e-10&&fabs(x2-x)<1e-10) {
      printf("%.10f\n",v/(r1+r2) );
      continue;
    }
    if (x1>x2) {
      swap(x1,x2);
      swap(r1,r2);
    }
    double mi=0,ma=v;
    while(ma-mi>1e-12)
    {
      double mid=(ma+mi)/2;
      double tmp=mid*x1+(v-mid)*x2;
      if (tmp<v*x) ma=mid;
      else mi=mid;
    }
    printf("%.10f\n", max(ma/r1,(v- ma)/r2));
  }
  }
}