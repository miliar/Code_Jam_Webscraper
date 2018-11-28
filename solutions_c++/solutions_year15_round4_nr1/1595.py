#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char g[105][105];
bool boun[105][105],vis[105][105],out[4][105][105];
int r,c;
int dx[]={1,-1,0,0};
int dy[]={0,0,1,-1};
char dir[]={'v','^','>','<'};
bool inboun(int a,int b)
{
    return a>=0&&b>=0&&a<r&&b<c;
}
void dfs(int x,int y)
{
    if(vis[x][y])
        return;
    vis[x][y]=true;
    if(g[x][y]!='.')
    {
        boun[x][y]=true;
        return;
    }
    for(int i=0;i<4;i++)
    {
        int a=x+dx[i];
        int b=y+dy[i];
        if(inboun(a,b))
            dfs(a,b);
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    int T;
    cin>>T;
    for (int cas=1;cas<=T;cas++)
    {
        cin>>r>>c;
        for(int i=0;i<r;i++)
            scanf("%s",g[i]);
        memset(boun,0,sizeof(boun));
        memset(vis,0,sizeof(vis));
        memset(out,0,sizeof(out));
        //cout<<r<<" "<<c<<endl;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                //cout<<i<< " "<<j<<" "<<r<<" "<<c<<endl;
                if(g[i][j]!='.')
                {
                    int k;
                    for(k=0;k<4;k++)
                        if(g[i][j]==dir[k])
                            break;
                    int a=i+dx[k];
                    int b=j+dy[k];
                    while(true)
                    {
                        if(!inboun(a,b))
                        {
                            boun[i][j]=true;
                            break;
                        }
                        if(g[a][b]!='.')
                            break;
                        a=a+dx[k];
                        b=b+dy[k];
                    }

                }
                //cout<<i<<" "<<j<<" "<<boun[i][j]<<endl;
            }
        }
        /*for(int i=0;i<c;i++)
        {
            dfs(0,i);
            dfs(r-1,i);
        }*/
        int val,cnt=0,cur;
        bool imp=false;
        for(int i=0;i<r&&!imp;i++)
            for(int j=0;j<c&&!imp;j++)
            {
                if(!boun[i][j])
                    continue;
                for(cur=0;cur<4;cur++)
                {
                     int a=i+dx[cur];
                     int b=j+dy[cur];
                     while(true)
                     {
                         if(!inboun(a,b))
                            break;
                         if(g[a][b]!='.')
                         {
                             cnt++;
                            break;
                         }
                        a=a+dx[cur];
                        b=b+dy[cur];

                     }
                     if(inboun(a,b))
                        break;
                }
                if(cur==4)
                    imp=true;
            }
        if(imp)
            printf("Case #%d: IMPOSSIBLE\n",cas);
        else
            printf("Case #%d: %d\n",cas,cnt);
    }
    return 0;
}
