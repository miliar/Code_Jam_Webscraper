#include<iostream>
#include<stdio.h>
//#include<algorithm>
//#include<math.h> 
//#include<string.h>
using namespace std;
long long T,TT,t,r,i,j,k,ans;
double temp,temp2;
double getsum(double a)
{
     double a1,a2;
     a1=(2*r+2*a-1)*a;
     return a1; 
}
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    scanf("%lld",&T);
    TT=T;
    while (T--)
    {
          scanf("%lld%lld",&r,&t);
          long long left=1,right=t/r,mid;
          ans=0;
          while (true)
          {
                mid=(right+left)/2;
                temp=getsum(mid);
                temp2=getsum(mid+1);
                if (temp<=t&&temp2>t){ans=mid;break;}
                if (temp>t){right=mid-1;continue;}
                if (temp<t){left=mid+1;continue;}
          }
          printf("Case #%lld: %lld\n",TT-T,ans);
    }
    return 0;
}
