#include<stdio.h>
#include<string.h>
int N,M,R;
int A[51][51];
int flag;
int X[8]={-1,-1,-1,0,0,1,1,1};
int Y[8]={-1,0,1,-1,1,-1,0,1};
int count(int x,int y)
{
    int k,cnt=0;
    for(k=0;k<8;k++) if(A[x+X[k]][y+Y[k]]) cnt++;
    return cnt;
}
struct QUE
{
    int x,y;
}que[5001];
int head,tail;
bool V[101][101];
bool bfs(int sx,int sy)
{
    memset(V,0,sizeof(V));
    head=tail=0;
    que[tail].x=sx; que[tail++].y=sy;
    V[sx][sy]=1;
    int x,y,i,j,k;
    while(head!=tail)
    {
        x=que[head].x; y=que[head++].y;
        for(k=0;k<8;k++)
        {
            if(!(1<=x+X[k]&&x+X[k]<=N&&1<=y+Y[k]&&y+Y[k]<=M)) continue;
            if(V[x+X[k]][y+Y[k]]) continue;
            if(A[x+X[k]][y+Y[k]]) continue;
            V[x+X[k]][y+Y[k]]=1;
            if(!count(x+X[k],y+Y[k]))
            {
                que[tail].x=x+X[k];
                que[tail++].y=y+Y[k];
            }
        }
    }
    for(i=1;i<=N;i++)
    {
        for(j=1;j<=M;j++)
        {
            if(A[i][j]) continue;
            if(!V[i][j]) return false;
        }
    }
    for(i=1;i<=N;i++)
    {
        for(j=1;j<=M;j++)
        {
            if(i==sx&&j==sy) printf("c");
            else if(A[i][j]) printf("*");
            else printf(".");
        }
        printf("\n");
    }
    return true;
}
void check()
{
    int i,j;
    for(i=1;i<=N;i++)
    {
        for(j=1;j<=M;j++)
        {
            if(A[i][j]) continue;
            if(count(i,j)==0)
            {
                if(bfs(i,j))
                {
                    flag=1;
                }
               return; 
            }
        }
    }
}
void dfs(int x,int y,int c,int n)
{
    if(flag) return;
    if(x==N+1)
    {
        if(c==R) check();
        return;
    }
    if(y==M+1)
    {
        dfs(x+1,1,c,n);
        return;
    }
    if(c+(N*M-n)<R) return;
    if(c+1<=R)
    {
        A[x][y]=1;
        dfs(x,y+1,c+1,n+1);
        A[x][y]=0;
    }
    if(flag) return;
    dfs(x,y+1,c,n+1);
}
int main()
{
    int T,t,i,j,k;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        flag=0;
        memset(A,0,sizeof(A));
        scanf("%d %d %d",&N,&M,&R);
        printf("Case #%d:\n",t);
        if(R==N*M-1)
        {
            for(i=1;i<=N;i++)
            {
                for(j=1;j<=M;j++)
                {
                    if(i==1&&j==1) printf("c");
                    else printf("*");
                }
                printf("\n");
            }
            continue;
        }
        dfs(1,1,0,0);
        if(!flag) printf("Impossible\n");
    }
}
