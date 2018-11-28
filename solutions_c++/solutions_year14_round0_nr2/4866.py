//b
#include<iostream>
#include<string>
#include<cstring>
#include<sstream>
#include<cstdio>
#include<algorithm>
using namespace std;
double cou(double c,double f,double x,double r)
{
     double p=(x/r);
     double q=(c/r)+((x)/(r+f));
     if(p<q)
        return p;
     else
        return min(p,(c/r)+cou(c,f,x,r+f));
}
int main()
{
    int t,cas=0;
    double c,f,x,an=0,r=2,p,q;
   // freopen("B-small-attempt0.in","r",stdin);
   // freopen("out.txt","w",stdout);
  scanf("%d",&t);
  while(t--)
  {
      cas++;
    scanf("%lf%lf%lf",&c,&f,&x);
    an=0;
    r=2;
    p=x/r;

    an=cou(c,f,x,r);

    printf("Case #%d: %.7lf\n",cas,an);
  }
    return 0;
}
