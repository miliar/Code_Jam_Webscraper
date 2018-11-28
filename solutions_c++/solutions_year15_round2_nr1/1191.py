#include<cstdio>
#include<queue>
#include<cstring>
using namespace std;
struct node
{
    int v,d;
};
int rvs(int x)
{
    int ret=0;
    while(x)
    {
        ret=ret*10+x%10;
        x/=10;
    }
    return ret;
}
int T,n,cas=1;
bool vis[1000010];
int bfs()
{
    queue<node> q;
    q.push((node){1,1});
    memset(vis,0,sizeof vis);vis[1]=1;
    while(!q.empty())
    {
        node x=q.front();q.pop();
      //  printf("x;%d v:%d d:%d\n",x,x.v,x.d);
        int tmp=rvs(x.v);
        if(x.v+1==n) return x.d+1;
        if(rvs(x.v)==n) return x.d+1;
        if(!vis[x.v+1])
        {
        //    printf("xx:%d\n",x.v+1);
            q.push((node){x.v+1,x.d+1});
            vis[x.v+1]=1;
        }
        if(vis[tmp]==0&&tmp>x.v)
        {
          //  printf("xxx:%d\n",tmp+1);
            q.push((node){tmp,x.d+1});
            vis[tmp]=1;
        }
    }
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("outaaaaaaaaa.txt","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        scanf("%lld",&n);
        printf("Case #%d: %d\n",cas++,n<=20?n:bfs());
    }
    return 0;
}
