#include <cstdio>
#include <queue>
#include <vector>
#include <cstring>

#define pb push_back

using namespace std;

const int INF=0x7FFFFFFF;
int n, dist[2005], match[2005];
vector <int> fixed[2005];

bool bfs()
{
    int i, u, v;
    queue <int> que;
    for (i=1;i<=n;i++)
        if (!match[i])
        {
            dist[i]=0;
            que.push(i);
        }
        else
            dist[i]=INF;
    dist[0]=INF;
    for (;!que.empty();)
    {
        u=que.front();
        que.pop();
        for (i=0;i<fixed[u].size();i++)
        {
            v=fixed[u][i];
            if (dist[match[v]]==INF)
            {
                dist[match[v]]=dist[u]+1;
                if (match[v])
                    que.push(match[v]);
            }
        }
    }
    return (dist[0]!=INF);
}

bool dfs(int u)
{
    int i, v;
    for (i=0;i<fixed[u].size();i++)
    {
        v=fixed[u][i];
        if (dist[match[v]]==dist[u]+1 && (!match[v] || dfs(match[v])))
        {
            match[v]=u;
            match[u]=v;
            return 1;
        }
    }
    dist[u]=INF;
    return 0;
}

int matching()
{
    int i, res=0;
    for (;bfs();)
        for (i=1;i<=n;i++)
            if (!match[i] && dfs(i))
                res++;
    return res;
}

int main(void)
{
    int t, i, j, k, tc=0, res[2];
    double p[2][1005];
    for (scanf("%d", &t);t--;)
    {
        scanf("%d", &n);
        for (i=0;i<2;i++)
            for (j=0;j<n;j++)
                scanf("%lf", &p[i][j]);
        for (i=0;i<2;i++)
        {
            memset(match, 0, sizeof(match));
            for (j=0;j<n;j++)
            {
                fixed[j+1].clear();
                for (k=0;k<n;k++)
                    if (p[i][j]>p[!i][k])
                        fixed[j+1].pb(n+k+1);
            }
            res[i]=matching();
        }
        printf("Case #%d: %d %d\n", ++tc, res[0], n-res[1]);
    }
    return 0;
}
