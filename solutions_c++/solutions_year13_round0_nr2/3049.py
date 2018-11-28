#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;
int map[110][110];
int dp[110][100][4],DP[110][110][4];

int dir[4][2]={{1,0},{-1,0},{0,1},{0,-1}};
bool vst[110][110],vst1[110][110];
int n,m;
bool judge(int x,int y)
{

   // cout<<"xx= "<<x<<" yy= "<<y<<endl;
    if(x<1||x>n||y<1||y>m||vst1[x][y])
    {
       // cout<<"NOT"<<endl;
        return 1;
    }
    return 0;
}
int cnt=0;
bool dfs(int x,int y,int mx,int my)
{
   // cout<<"x= "<<x<< "y=  "<<y<<endl;
    if(x==1||y==1||x==n||y==m)return 1;
    int i;
    for(i=0;i<4;i++)
    {
        int tmpx=x+dir[i][0],tmpy=y+dir[i][1];
        if(judge(tmpx,tmpy))continue;



        if(map[tmpx][tmpy]<=map[x][y])
        {

            //if(mx==2&&my==4) cout<<tmpx<<" "<<tmpy<<endl;
            vst1[tmpx][tmpy]=1;
            if(dfs(tmpx,tmpy,mx,my))
            {
                vst[tmpx][tmpy]=1;
                return 1;
            }
        }
    }
    return 0;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cas,ca=0,i,j;
    scanf("%d",&cas);
    while(cas--)
    {
        printf("Case #%d:",++ca);
        scanf("%d%d",&n,&m);
        memset(map,0,sizeof(map));
        for(i=1; i<=n; i++)
        {
            for(j=1; j<=m; j++)
            {
                scanf("%d",&map[i][j]);
            }
        }
        bool f=0;
        int k;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                int tmp=map[i][j],f1=0,f2=0;
                for(k=1;k<=m;k++)
                {
                    if(map[i][k]<=tmp);
                    else break;
                }
                if(k==m+1);
                else f1=1;

                for(k=1;k<=n;k++)
                {
                    if(map[k][j]<=tmp);
                    else break;
                }
                if(k==n+1);
                else f2=1;
                if(f1&&f2)f=1;
                if(f)break;
            }
        }
        if(f)printf(" NO\n");
        else printf(" YES\n");
    }
    return 0;
}
