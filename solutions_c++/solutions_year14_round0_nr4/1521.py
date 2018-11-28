#include <cstdio>
#include <cstring>
#include <algorithm>
#include<vector>
#include<iostream>
#include<cmath>
#define ll long long
using namespace std;

const int N = 1010;

double a[N], b[N];
bool vis[N];
int n;

void solve()
{
    scanf("%d", &n);
    for(int i=1;i<=n;i++)
        scanf("%lf", &a[i]);
    for(int j=1;j<=n;j++)
        scanf("%lf", &b[j]);
    int ans1=0, ans2=0;
    sort(a+1, a+n+1);sort(b+1, b+n+1);
    int p=n;
    for(int i=n;i>=1;i--)
    {
        while(p>=1&&a[i]<b[p])
            p--;
        if(p>=1)
        {
            ans1++;p--;
        }
    }
    memset(vis, 0, sizeof(vis));
    for(int i=1;i<=n;i++)
    {
        int find=0;
        for(int j=1;j<=n;j++)
            if(!vis[j] && b[j]>a[i])
            {
                vis[j]=true;find=1;break;
            }
        if(find)continue;
        ans2++;
        for(int j=1;j<=n;j++)
            if(!vis[j])
            {
                vis[j]=true;break;
            }
    }
    printf("%d %d\n", ans1, ans2);
}

int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    int t;
    scanf("%d", &t);
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
