#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
int T,tt;
const int N=110;
int a[110][110],b[110][110][2];
int n,m;
int ar[N];
int lowb(int x){return x&(-x);}
int add(int x,int v)
{
    for(int i=x;i<N;ar[i]+=v,i+=lowb(i));
}
int sum(int i)
{
    int s=0;
    for(;i>0;s+=ar[i],i-=lowb(i));
    return s;
}
int solve()
{
    for(int i=1;i<=n;i++)
    {
        memset(ar,0,sizeof(ar));
        for(int j=1;j<=m;j++)
        {
            int s=sum(a[i][j]);
            if(s!=j-1)b[i][j][0]++;
            add(a[i][j],1);
        }
    }
    for(int i=1;i<=n;i++)
    {
        memset(ar,0,sizeof(ar));
        for(int j=m;j>=1;j--)
        {
            int s=sum(a[i][j]);
            if(s!=m-j)b[i][j][0]++;
            add(a[i][j],1);
        }
    }
    for(int i=1;i<=m;i++)
    {
        memset(ar,0,sizeof(ar));
        for(int j=1;j<=n;j++)
        {
            int s=sum(a[j][i]);
            if(s!=j-1)b[j][i][1]++;
            add(a[j][i],1);
        }
    }
    for(int i=1;i<=m;i++)
    {
        memset(ar,0,sizeof(ar));
        for(int j=n;j>=1;j--)
        {
            int s=sum(a[j][i]);
            if(s!=n-j)b[j][i][1]++;
            add(a[j][i],1);
        }
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            if(!(b[i][j][1]==0||b[i][j][0]==0))return 0;
        }
    }
    return 1;
}
int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("out","w",stdout);
    scanf("%d",&T);
    tt=0;
    while(T--)
    {
        scanf("%d%d",&n,&m);
        memset(b,0,sizeof(b));
        for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
        scanf("%d",&a[i][j]);
        printf("Case #%d: ",++tt);
        printf("%s\n",solve()?"YES":"NO");
    }
    return 0;
}
