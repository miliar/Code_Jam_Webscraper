#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<string>
#include<cstring>
#include <cmath>
#include<algorithm>
#include<stack>
using namespace std;

int T;
double c;
double f;
double x;
double ans=0;
void solve()
{
    ans=0;
    double n=0;
    n=floor((f*x-2*c)/(c*f));
  //  cout<<n<<endl;
    if(n<0)
    {
        ans=x/2;
        return;
    }
    for(int i=0;i<n;i++)
    {
        ans+=c/(2+i*f);
    }
    ans+=x/(2+n*f);
}
int main()
{
    freopen("B-large.in","r",stdin);
  // freopen("input.txt","r",stdin);
    freopen("b-large.out","w",stdout);
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        solve();
        printf("Case #%d: %.7lf\n",i,ans);
    }
    return 0;
}
