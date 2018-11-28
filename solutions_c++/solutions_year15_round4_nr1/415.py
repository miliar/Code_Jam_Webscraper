#include <bits/stdc++.h>
using namespace std;


char mp[110][110];
bool v[110];
int low[110], head[110], rea[110], ans, top, st[110], tm;
void tarjan(int i)
{
    v[i]=1;
    top++;
    st[top]=i;
    low[i]=rea[i]=++tm;
    int j=head[i];
    while (j!=0)
    {
        if (v[e[j]]==0) tarjan(e[j]);
        if (v[e[j]]<2) low[i]=min(low[i],low[e[j]]);
        j=next[j];
    }
    if (rea[i]==low[i])
    {
        color++;
        while (st[top+1]!=i)
        {
            col[st[top]]=color;
            v[st[top]]=2;
            top--;
        }
    }
}

int T, R, C;
int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        scanf("%d%d\n", &R, &C);
        for (int i = 0; i < R; ++i)
        {
            for (int j = 0; j < C; ++j)
            {
                scanf("%c", &mp[i][j]);
            }
            scanf("\n");
        }
        for (int i = 0; i < R; ++i)
        {
            for (int j = 0; j < C; ++j)
            {
                dfs(i, j);
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }

    return 0;
}
