#include <bits/stdc++.h>

using namespace std;

int dx[4]={-1,1,0,0},dy[4]={0,0,-1,1},vis[10];

char str[110][110];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--) {
        int n,m,nd;
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;i++)
            scanf("%s",str[i]+1);
        printf("Case #%d: ",++cas);
        int flag=0,ans=0;
        for(int i=1;i<=n;i++) {
            for(int j=1;j<=m;j++) {
                if(str[i][j]=='.')
                    continue;
                memset(vis,0,sizeof(vis));
                for(int d=0;d<4;d++) {
                    int nx=i,ny=j;
                    nx+=dx[d];
                    ny+=dy[d];
                    while(nx>=1&&ny>=1&&nx<=n&&ny<=m) {
                        if(str[nx][ny]!='.') {
                            vis[d]=1;
                            break;
                        }
                        nx+=dx[d];
                        ny+=dy[d];
                    }
                }
                if(str[i][j]=='^')
                    nd=0;
                if(str[i][j]=='v')
                    nd=1;
                if(str[i][j]=='<')
                    nd=2;
                if(str[i][j]=='>')
                    nd=3;
                if(vis[nd])
                    continue;
                flag=1;
                for(int d=0;d<4;d++) {
                    if(vis[d]==1) {
                        flag=0;
                        ans++;
                        break;
                    }
                }
                if(flag==1)
                    break;
            }
        }
        if(flag==1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",ans);
    }
    return 0;
}
