#include<bits/stdc++.h>
using namespace std;
const int Maxn=200;
int N,M;
int id[Maxn][Maxn];
char s[Maxn][Maxn];
int dir[4][2]={{-1,0},{1,0},{0,-1},{0,1}};
int gofrom(int x,int y,int di)
{
    x+=dir[di][0],y+=dir[di][1];
    for(;x<=N&&x>=1&&y>=1&&y<=M&&id[x][y]==-1;)
    {
        x+=dir[di][0],y+=dir[di][1];
        if(id[x][y]!=-1)di=id[x][y];
    }
    if(x<=N&&x>=1&&y>=1&&y<=M)return 1;
    return -1;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int _,cs=1;scanf("%d",&_);
    while(_--)
    {
        scanf("%d%d",&N,&M);
        memset(id,-1,sizeof(id));
        for(int i=1;i<=N;i++)
        {
            scanf("%s",s[i]+1);
            for(int j=1;j<=M;j++)
            {
                if(s[i][j]=='^')id[i][j]=0;
                if(s[i][j]=='v')id[i][j]=1;
                if(s[i][j]=='<')id[i][j]=2;
                if(s[i][j]=='>')id[i][j]=3;
            }
        }
        bool flag=1;
        int ans=0;
        for(int i=1;i<=N;i++)
            for(int j=1;j<=M;j++)
            if(id[i][j]!=-1)
            {
                int rep=gofrom(i,j,id[i][j]);
                if(rep==-1)
                {
                    bool tf=0;
                    for(int k=0;k<4;k++)
                        if(gofrom(i,j,k)!=-1)
                            tf=1;
                    if(!tf)flag=0;
                    else ans++;
                }
            }
        printf("Case #%d: ",cs++);
        if(!flag)puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
}
