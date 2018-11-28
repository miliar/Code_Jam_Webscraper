#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;
const int N=10010, INF=10000000;
int t, n, x[N], vis[N], res1, res2;

int Find()
{
    for(int i=res1;i>=0;i--)
    {
        if(vis[i]>=1)
            return i;
    }
}

int Solve(int k, int st)
{
    if(k==st)
        return Find();
    int ret=INF;
    int num=Find();
    ret=num;
    for(int j=0;j<=num/2;j++)
    {
        vis[num]--, vis[j]++, vis[num-j]++;
        ret=min(ret, Solve(k, st+1)+1 );
        vis[num]++, vis[j]--, vis[num-j]--;
    }
    return ret;
}

int main()
{
    freopen("r.txt","r",stdin);
    freopen("w.txt","w",stdout);
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>n;
        res1=0;
        memset(vis, 0, sizeof vis);
        for(int j=0;j<n;j++){
            cin>>x[j];
            res1=max(res1, x[j]);
            vis[x[j]]++;
        }
        res2=Solve(res1, 0);
        printf("Case #%d: %d\n",i+1, min(res1, res2) );
    }


    return 0;
}
