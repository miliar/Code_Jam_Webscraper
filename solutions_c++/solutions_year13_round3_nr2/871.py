#include<cstdio>
#include<queue>
#include<cstring>
#include<algorithm>
using namespace std;
char s[600];
char di[]={'S','N','E','W'};
int dx[]={0,0,1,-1},dy[]={-1,1,0,0};
char ma[211][211][550];
bool vis[4010][4010];
int ex,ey;
/*struct XX
{
    int x,y,s;
    int cha;
    char s[550];
    bool operator () (const XX &a,const XX &b){
        if(a.cha==b.cha)
        return a.s>b.s;
        return a.cha>b.cha;
    }
};*/
//priority_queue<XX>q;
void dfs(int x,int y,int steps)
{
    if(abs(x)>200||abs(y)>200||steps==501)return ;
    if(vis[x+2010][y+2010])return ;
    vis[x+2010][y+2010]=1;
    if(abs(x)<=100&&abs(y)<=100)
    for(int i=0;i<=steps;i++)
    {
        ma[x+101][y+101][i]=s[i];
    }
    for(int i=0;i<4;i++){
        //if(abs(x+steps*dx[i]-ex)+abs(y+steps*dy[i]-ey)>cha)continue;
        s[steps-1]=di[i];
        s[steps]='\0';
        dfs(x+steps*dx[i],y+steps*dy[i],steps+1);//abs(x+steps*dx[i]-ex)+abs(y+steps*dy[i]-ey)))
        //{
            //printf("%c",di[i]);
            //printf("%d %d\n",x+steps*dx[i],y+steps*dy[i]);
            //s[steps-1]=di[i];
            //return true;
        //}

    }
    //return false;
}
void dfs2(int x,int y,int steps)
{
    if(abs(x)>2000||abs(y)>2000||steps==501)return ;
    if(vis[x+2010][y+2010])return ;
    vis[x+2010][y+2010]=1;
    if(abs(x)<=100&&abs(y)<=100)
    for(int i=0;i<=steps;i++)
    {
        ma[x+101][y+101][i]=s[i];
    }
    for(int i=0;i<4;i++){
        //if(abs(x+steps*dx[i]-ex)+abs(y+steps*dy[i]-ey)>cha)continue;
        s[steps-1]=di[i];
        s[steps]='\0';
        dfs2(x+steps*dx[i],y+steps*dy[i],steps+1);//abs(x+steps*dx[i]-ex)+abs(y+steps*dy[i]-ey)))
        //{
            //printf("%c",di[i]);
            //printf("%d %d\n",x+steps*dx[i],y+steps*dy[i]);
            //s[steps-1]=di[i];
            //return true;
        //}

    }
    //return false;
}
void dfs1(int x,int y,int steps)
{
    if(abs(x)>1000||abs(y)>1000||steps==501)return ;
    if(vis[x+2010][y+2010])return ;
    vis[x+2010][y+2010]=1;
    if(abs(x)<=100&&abs(y)<=100)
    for(int i=0;i<=steps;i++)
    {
        ma[x+101][y+101][i]=s[i];
    }
    for(int i=0;i<4;i++){
        //if(abs(x+steps*dx[i]-ex)+abs(y+steps*dy[i]-ey)>cha)continue;
        s[steps-1]=di[i];
        s[steps]='\0';
        dfs1(x+steps*dx[i],y+steps*dy[i],steps+1);//abs(x+steps*dx[i]-ex)+abs(y+steps*dy[i]-ey)))
        //{
            //printf("%c",di[i]);
            //printf("%d %d\n",x+steps*dx[i],y+steps*dy[i]);
            //s[steps-1]=di[i];
            //return true;
        //}

    }
    //return false;
}
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("text.out","w",stdout);
    int T,ca=1;
    scanf("%d",&T);
    memset(vis,0,sizeof(vis));
    dfs(0,0,1);
    memset(vis,0,sizeof(vis));
    dfs1(0,0,1);
    memset(vis,0,sizeof(vis));
    dfs2(0,0,1);
    while(T--)
    {
        scanf("%d%d",&ex,&ey);
        //while(!q.empty())
        //dfs(0,0,1);
        printf("Case #%d: %s\n",ca++,ma[ex+101][ey+101]);
    }
    return 0;
}
