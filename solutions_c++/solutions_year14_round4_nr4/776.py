#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <set>

#define rep(i,n) for (int n__=n,i=1;i<=n__;i++)
#define repb(i,b,n) for (int n__=n,i=b;i<=n__;i++)
using namespace std;
typedef long long LL;
const int mN=105;

string a[mN];
int n,m;
int fa[mN];
int ans,anst;
set<string> ss[mN];
void count()
{
    rep(i,m)
        ss[i].clear();
    rep(i,n)
    {
        rep(j,a[i].size())
            ss[fa[i]].insert(a[i].substr(0,j));
    }
    int ct=0;
    rep(i,m)
        if (ss[i].empty())
            return;
        else
        {
            ct+=(ss[i].size());
        }
    if (ct>ans)
    {
        ans=ct;
        anst=1;
    }
    else if (ct==ans)
        anst++;
}
void dfs(int x)
{
    if (x>n)
    {
        count();
        return;
    }
    rep(i,m)
    {
        fa[x]=i;
        dfs(x+1);
        fa[x]=0;
    }
}

int main()
{
 freopen("D-small-attempt3.in","r",stdin);
freopen("D-small-attempt3.out","w",stdout);
    int ta;
    cin>>ta;
    rep(tz,ta)
    {
        printf("Case #%d: ",tz);
        cin>>n>>m;
        ans=0;
        anst=0;
        rep(i,n)
            cin>>a[i];
        dfs(1);
        printf("%d %d\n",ans+m,anst);
    }

    return 0;
}
