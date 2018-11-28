#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;
int t,i,j,m;
double c,f,x,n,ans;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        ans=0;
        scanf("%lf%lf%lf",&c,&f,&x);
        n=floor(x/c-2/f);
        if(n<0)n=0;
        m=(int)(n);
        for(j=0;j<m;j++)ans+=c/(2+f*j);
        ans+=x/(2+f*j);
        printf("Case #%d: %.7lf\n",i,ans);
    }
    return 0;
}
