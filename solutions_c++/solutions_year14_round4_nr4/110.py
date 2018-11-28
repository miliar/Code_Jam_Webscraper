#include <cstdio>
#include <vector>
#include <string>
#include <set>
using namespace std;
string a[10];
vector <int> b[10];
int n,m,ans,cnt;
int calc(int x)
{
    if (b[x].empty())
        return(0);
    set <string> s;
    for (int i=0;i<b[x].size();i++)
    {
        int y=b[x][i];
        for (int j=1;j<=a[y].size();j++)
            s.insert(a[y].substr(0,j));
    }
    return(s.size()+1);
}
void dfs(int dep)
{
    if (dep==n+1)
    {
        int sum=0;
        for (int i=1;i<=m;i++)
            sum+=calc(i);
        if (sum>ans)
            ans=sum,cnt=0;
        if (sum==ans)
            cnt++;
        return;
    }
    for (int i=1;i<=m;i++)
    {
        b[i].push_back(dep);
        dfs(dep+1);
        b[i].pop_back();
    }
}
int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d%d",&n,&m);
        for (int i=1;i<=n;i++)
        {
            char buf[20];
            scanf("%s",buf);
            a[i]=buf;
        }
        ans=-1;
        dfs(1);
        static int id=0;
        printf("Case #%d: %d %d\n",++id,ans,cnt);
    }
    return(0);
}

