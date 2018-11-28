#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
const int N=103;
int a[N][N];
bool used[N][N];
int n,m;
int dfs(int x,int y,int offx,int offy)
{
    int num=0;
    if(x<1 || x>n || y<1 || y>m)return 0;
    if(a[x][y]!=1)return 0;
    num=dfs(x+offx,y+offy,offx,offy)+1;
    return num;
}
int main()
{
    int T;
    bool isok;
   // freopen("in.txt","r",stdin);

    //freopen("B-small-attempt3.in","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>T;
    for(int cas=1; cas<=T; cas++)
    {
        cin>>n>>m;
        isok=true;
        memset(used,false,sizeof(used));
        for(int i=1; i<=n; i++)
            for(int j=1; j<=m; j++)
                cin>>a[i][j];
        for(int i=1;i<=n && isok;i++)
          for(int j=1;j<=m && isok;j++)
          {
              if(a[i][j]==1)
              {
                  int sum1=dfs(i,j,0,-1)+dfs(i,j+1,0,1);
                  int sum2=dfs(i,j,-1,0)+dfs(i+1,j,1,0);
                  if(!(sum1==m || sum2==n))isok=false;
              }
          }
        printf("Case #%d: ",cas);
        if(isok)printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
