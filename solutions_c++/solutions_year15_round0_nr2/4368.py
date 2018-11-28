#include <stdio.h>
#include <string.h>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#define PI acos(-1.0)
#define M 1000005  //10^6
#define eps 1e-8
#define LL long long
#define moo 1000000007
#define INF -999999999
using namespace std;
int a[1500];
int ans;
int n;
void dfs(int x,int y,int now,int la,int fa)
{

    if(x==0)
    {
        //cout<<ans<<ends<<y<<ends<<a[now]<<ends<<fa<<endl;
        ans=min(ans,y+max(a[now],fa));
        return ;
    }
    if(now==0)
    {
        return ;
    }
    for(int i=1;i<=x;i++)
    {
        int t=(a[now]+i)/(i+1);
       // cout<<y<<ends<<i<<ends<<la<<ends<<t<<endl;
        if(t>la)
            continue;
        if(now==n)
            dfs(x-i,y,now-1,t,t);
        else
            dfs(x-i,y,now-1,t,fa);
    }
}
int main()
{
    //freopen("3.in","r",stdin);
    //freopen("1.out","w",stdout);
    int T;
    scanf("%d",&T);
    int dd=T;
    while(T--)
    {
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
            scanf("%d",&a[i]);

        sort(a+1,a+n+1);
        ans=a[n];
        a[0]=0;
        for(int i=a[n];i>=0;i--)
        {
            dfs(i,i,n,a[n],a[n]);
        }

        cout<<"Case #"<<dd-T<<": ";
        cout<<ans<<endl;
    }
}
