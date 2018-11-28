#include <stdio.h>
#include <string.h>
int map[110][110],m,n;
int vis[110][110];
int cr(int x)
{
    for(int i=0;i<m;i++)
    if(map[x][i]!=1)return 0;
    return 1;
}
int cw(int x)
{
    for(int i=0;i<n;i++)
    if(map[i][x]!=1)return 0;
    return 1;
}
int main()
{
    //freopen("answer.out","w",stdout);
    int T,u=0,ct;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&m);
        memset(map,0,sizeof(map));
        memset(vis,0,sizeof(vis));
        printf("Case #%d: ",++u);
        ct=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                scanf("%d",&map[i][j]);
            }
        }
        for(int i=0;i<n;i++)
        {
            if(cr(i))
            for(int j=0;j<m;j++)vis[i][j]=1;
        }
        for(int i=0;i<m;i++)
        {
            if(cw(i))
            for(int j=0;j<n;j++)vis[j][i]=1;
        }
        int f=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if(map[i][j]==1&&vis[i][j]==0){f=1;break;}
            }
        }
        if(f)printf("NO\n");
        else printf("YES\n");

    }

    return 0;
}
