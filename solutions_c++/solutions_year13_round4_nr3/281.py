#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<cmath>
#include<algorithm>
#define ll long long
using namespace std;

const ll MOD=1000002013;
const int N =100001;
bool had[N];
int a[N],b[N];
int c[N];
int n;
bool ok(int n)
{
    int t=1;
    for(int i=1;i<n;++i)
    if(c[i]<c[n])
    t=max(t,a[i]+1);
    if(t==a[n])
    return true;
    return false;
}
bool F(int n)
{
    for(int i=n-1;i>=1;--i)
    {
        int t=1;
        for(int j=i+1;j<=n;++j)
        if(c[j]<c[i])
        t=max(t,b[j]+1);
        if(t!=b[i])
        return false;
    }
    return true;
}
bool dfs(int x)
{
    for(int i=1;i<=n;++i)
    {
        if(!had[i])
        {
            c[x]=i;
            if(x==n)
            {
                if(ok(x)&&F(x))
                return true;
                return false;
            }
            if(ok(x))
            {
                had[i]=true;
                if(dfs(x+1))
                return true;
                had[i]=false;
            }
        }
    }
    return false;
}
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int T;
    cin>>T;
    for(int w=1;w<=T;++w)
    {
        printf("Case #%d:",w);
        cin>>n;
        for(int i=1;i<=n;++i)
        cin>>a[i];
        for(int i=1;i<=n;++i)
        cin>>b[i];
        memset(had,false,sizeof(had));
        dfs(1);
        for(int i=1;i<=n;++i)
        cout<<" "<<c[i];
        cout<<endl;
    }
    return 0;
}
