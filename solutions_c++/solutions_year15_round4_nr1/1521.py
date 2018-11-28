#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn=110;
char str[maxn][maxn];
int n,m;
int dir[4][2]={{0,1},{-1,0},{0,-1},{1,0}};
int giveDir(char c)
{
    if(c=='>')  return 0;
    if(c=='^')  return 1;
    if(c=='<')  return 2;
    if(c=='v')  return 3;
    return -1;
}
int indeg[maxn][maxn],rn[maxn],rm[maxn];
bool finds(int i,int j,int d)
{
    if(i>=n||i<0||j>=m||j<0)    return false;
    if(str[i][j]!='.')  return true;
    return finds(i+dir[d][0],j+dir[d][1],d);
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            scanf("%s",str[i]);
        memset(indeg,0,sizeof(indeg));
        memset(rn,0,sizeof(rn));
        memset(rm,0,sizeof(rm));
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(str[i][j]!='.')
                    ++rn[i],++rm[j];
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                if(str[i][j]=='.')  continue;
                int d=giveDir(str[i][j]);
                if(finds(i+dir[d][0],j+dir[d][1],d))
                    ++indeg[i][j];
            }
        int ans=0;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                if(ans==-1) break;
                if(str[i][j]=='.')  continue;
                if(indeg[i][j]==0)
                {
                    if(rn[i]<=1&&rm[j]<=1)  ans=-1;
                    else    ++ans;
                }
            }
        printf("Case #%d: ",cas++);
        if(ans==-1) printf("IMPOSSIBLE\n");
        else    printf("%d\n",ans);
    }
    return 0;
}
