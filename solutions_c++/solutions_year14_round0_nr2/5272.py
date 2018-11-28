#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#define rep(i,j,n) for(int i=j;i<n;i++)
#define repd(i,j,n) for(int i=j;i>n;i--)
#define N 1005
using namespace std;
double c,f,x;
int main()
{
// freopen("B-small-attempt0.in","r",stdin);
// freopen("out.txt","w",stdout);
     int T;
     scanf("%d",&T);
     int test=1;
     while(T--)
     {
         scanf("%lf%lf%lf",&c,&f,&x);
         double ans=0;
         double v=2.0;
         while(x/v>c/v+x/(f+v))
         {
             ans+=c/v;
             v+=f;
         }

         ans+=x/v;
         printf("Case #%d: %.7lf\n",test++,ans);
     }
    return 0;
}
