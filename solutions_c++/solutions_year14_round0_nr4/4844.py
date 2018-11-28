#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
typedef long long ll;
int n,m;
double a[2200],b[2200];
bool f[2200];
int cc[2200];
bool ok[22];
int ans1,ans2;
void slove()
{
    int mx1=0,mx2=0;
    memset(f,true,sizeof f);
    for (int i=1; i<=n; i++)
    {
        int ii=cc[i]-1;
        int j;
        for (j=0; j<n; j++)
        if (b[j]>a[ii] && f[j]) break;
        if (j<n)
        {
            f[j]=false;
        }
        else
        {
            for (j=0; j<n; j++)
            if (f[j])
            {
                f[j]=false;
                mx1++;
                break;
            }
        }
    }
    memset(f,true,sizeof f);
    for (int i=1; i<=n; i++)
    {
        int ii=cc[i]-1;
        int j=n-1;
        while(!f[j] && j>=0) j--;
        if (a[ii]>b[j])
        {
            mx2++;
        }
        f[j]=false;
    }
    ans1=max(ans1,mx1);
    ans2=max(ans2,mx2);

}
void dfs(int i)
{
    for (int j=1; j<=n; j++)
    {
        if (ok[j])
        {
            cc[i]=j;
            ok[j]=false;
            if (i==n) slove();
            else dfs(i+1);
            ok[j]=true;
        }
    }
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tt;
    scanf("%d",&tt);
    for (int ii=1; ii<=tt; ii++)
    {
        scanf("%d",&n);
        for (int i=0; i<n; i++)
        scanf("%lf",&a[i]);
        for (int i=0; i<n; i++)
        scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        memset(f,true,sizeof f);
        memset(ok,true,sizeof ok);
        ans1=ans2=0;
        dfs(1);
        printf("Case #%d: %d %d\n",ii,ans2,ans1);
    }
    return 0;
}
