#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
struct node
{
    double r,c;
}wator[110];
int T,t,n,m;
double eps=1e-14;
int dcmp(double x)
{
    return (x>eps)-(x<-eps);
}
bool cmp(node a,node b)
{
    return dcmp(a.c-b.c)<0;
}
double V,X;
bool solve(double num)
{
    int i;
    double minn=0,maxn=0,V2,V3,ret;
    V2=V;
    for(i=1;i<=n;i++)
    {
        ret=min(num*wator[i].r,V2);
        minn+=ret*wator[i].c;
        V2-=ret;
    }
    V3=V;
    for(i=n;i>=1;i--)
    {
        ret=min(num*wator[i].r,V3);
        maxn+=ret*wator[i].c;
        V3-=ret;
    }
    minn/=V;
    maxn/=V;
    if(dcmp(V2)!=0 || dcmp(V3)!=0)
      return false;
    if(dcmp(X-minn)>=0 && dcmp(maxn-X)>=0)
      return true;
    return false;
}
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B.txt","w",stdout);
    int i,j,k;
    double l,r,mi;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        scanf("%lf%lf",&V,&X);
        for(i=1;i<=n;i++)
           scanf("%lf%lf",&wator[i].r,&wator[i].c);
        sort(wator+1,wator+1+n,cmp);
        //printf("Case %d --%d %d\n",t,dcmp(X-wator[1].c),dcmp(wator[n].c-X));
        if(dcmp(X-wator[1].c)==-1 || dcmp(wator[n].c-X)==-1)
        {

            printf("Case #%d: IMPOSSIBLE\n",t);
            continue;
        }
        l=0;r=1e9;
        while(r-l>1e-9)
        {
            mi=(l+r)/2;
            if(solve(mi))
              r=mi;
            else
              l=mi;
        }
        printf("Case #%d: %.8f\n",t,l);
    }
}
