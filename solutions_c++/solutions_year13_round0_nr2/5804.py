#include <cstdio>
#include <cstring>
int a[12][12],n,m;
bool vis[12][12];
bool check_line(int x)
{
    int i;
    bool flag=true;
    for (i=0; i<m; ++i)
        if (a[x][i]!=1)
            flag=false;
    if (!flag)
        return false;
    for (i=0; i<m; ++i)
        vis[x][i]=true;
    return true;
}
bool check_row(int y)
{
    int i;
    bool flag=true;
    for (i=0; i<n; ++i)
        if (a[i][y]!=1)
            flag=false;
    if (!flag)
        return false;
    for (i=0; i<n; ++i)
        vis[i][y]=true;
    return true;
}
bool check(int x,int y)
{
    if (check_line(x) || check_row(y))
        return true;
    return false;
}
int main()
{
    int i,j,T;
    scanf("%d",&T);
    for (int kcase=1; kcase<=T; ++kcase)
    {
        scanf("%d%d",&n,&m);
        for (i=0; i<n; ++i)
            for (j=0; j<m; ++j)
                scanf("%d",&a[i][j]);
        memset(vis,0,sizeof(vis));
        bool flag=true;
        for (i=0; i<n && flag; ++i)
            for (j=0; j<m && flag; ++j)
                if (a[i][j]==1 && !vis[i][j])
                    if (!check(i,j))
                        flag=false;
        if (flag)
            printf("Case #%d: YES\n",kcase);
        else
            printf("Case #%d: NO\n",kcase);
    }
    return 0;
}
