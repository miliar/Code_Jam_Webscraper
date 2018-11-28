#include <cstdio>
#include <cstring>
const int c[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
char a[110][110];
int n,m,vis[110][110][4];
int get(char ch)
{
    if (ch=='^')
        return(0);
    if (ch=='v')
        return(1);
    return(ch=='<'?2:3);
}
bool out(int i,int j,int k)
{
    i+=c[k][0],j+=c[k][1];
    if (i==0 || i>n || j==0 || j>m)
        return(true);
    if (a[i][j]!='.')
        return(false);
    if (vis[i][j][k]!=-1)
        return(vis[i][j][k]);
    vis[i][j][k]=out(i,j,k);
    return(vis[i][j][k]);
}
int work()
{
    memset(vis,-1,sizeof(vis));
    int ans=0;
    for (int i=1;i<=n;i++)
        for (int j=1;j<=m;j++)
        {
            if (a[i][j]=='.')
                continue;
            bool flag=true;
            for (int k=0;k<4;k++)
                if (!out(i,j,k))
                {
                    flag=false;
                    break;
                }
            if (flag)
                return(-1);
            ans+=out(i,j,get(a[i][j]));
        }
    return(ans);
}
int main()
{
    int T;
    scanf("%d",&T);
    while (T--)
    {
        scanf("%d%d",&n,&m);
        for (int i=1;i<=n;i++)
            scanf("%s",a[i]+1);
        static int id=0;
        printf("Case #%d: ",++id);
        int ans=work();
        if (ans==-1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",ans);
    }
    return(0);
}

