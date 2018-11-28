#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define szz 3010

#define sz 2010*2010
#define inf 0x7fffffff
struct node{int s,t,v,nxt;}e[sz*4];
int hd[sz],dis[sz],cur[sz],que[sz],cnt;
void insert(int s,int t,int v){
    //printf("%d %d %d\n",s,t,v);
    e[cnt].s=s,e[cnt].t=t,e[cnt].v=v,e[cnt].nxt=hd[s],hd[s]=cnt++;
    e[cnt].s=t,e[cnt].t=s,e[cnt].v=0,e[cnt].nxt=hd[t],hd[t]=cnt++;
}
bool bfs(int s,int t,int n){
    int head=0,tail=0,i;
    memset(dis,-1,sizeof(dis[0])*(n+1)),dis[s]=0;
    que[tail++]=s;
    while(head<tail){
        for(i=hd[que[head++]];i!=-1;i=e[i].nxt)
            if(e[i].v>0&&dis[e[i].t]==-1){
                dis[e[i].t]=dis[e[i].s]+1;
                if(e[i].t==t)return 1;
                que[tail++]=e[i].t;
            }
    }
    return 0;
}
int dinic(int s,int t,int n){
    int i,mf=0,tp;
    while(bfs(s,t,n)){
        for(i=0;i<n;i++)cur[i]=hd[i];
        int u=s,tail=0;
        while(cur[s]!=-1){
            if(u!=t&&cur[u]!=-1&&e[cur[u]].v>0&&dis[u]+1==dis[e[cur[u]].t]){
                que[tail++]=cur[u];u=e[cur[u]].t;
            }
            else if(u==t){
                for(tp=inf,i=tail-1;i>=0;i--)tp=min(tp,e[que[i]].v);
                for(mf+=tp,i=tail-1;i>=0;i--){
                    e[que[i]].v-=tp;e[que[i]^1].v+=tp;
                    if(e[que[i]].v==0)tail=i;
                }
                u=e[que[tail]].s;
            }
            else {
                while(u!=s&&cur[u]==-1)u=e[que[--tail]].s;
                cur[u]=e[cur[u]].nxt;
            }
        }
    }
    return mf;
}




int x[2][szz],y[2][szz];
int plot[szz][szz];

int w,h,b,all;
int gid(int x,int y,int t)
{
    //printf("gid%d %d %d\n",x,y,t);
    return x*h+y+all*t;
}

int main()
{
    int ti;scanf("%d",&ti);
    for(int ca=1; ca<=ti; ca++)
    {
        scanf("%d%d%d",&w,&h,&b);
        vector<int>s;
        for(int i=0; i<b; i++)
        {
            scanf("%d%d%d%d",&x[0][i],&y[0][i],&x[1][i],&y[1][i]);
            x[1][i]++;
            y[1][i]++;
            s.push_back(y[0][i]);
            s.push_back(y[1][i]);
        }
        s.push_back(0);
        s.push_back(h);
        s.push_back(h+1);
        sort(s.begin(),s.end());
        s.resize(unique(s.begin(),s.end()) - s.begin());

        for(int i=0;i<b; i++)
        {
            y[0][i]=*lower_bound(s.begin(),s.end(),y[0][i]);
            y[1][i]=*lower_bound(s.begin(),s.end(),y[1][i]);
        }
        h = *lower_bound(s.begin(),s.end(),h);

        memset(plot,0,sizeof(plot));

        //printf("%d\n",b);
        for(int z=0;z<b;z++)
        {
            //printf("%d %d %d %d\n",x[0][z],y[0][z],x[1][z],y[1][z]);
            for(int i=x[0][z];i<x[1][z];i++)
            for(int j=y[0][z];j<y[1][z];j++)
            {
                plot[i][j] = 1;
            }
        }
        /*
        for(int j=h-1;j>=0;j--)
        {

            for(int i=0;i<w;i++)
            {
                printf(plot[i][j]==1?"#":".");
            }
            printf("\n");
        }
        //*/

        memset(hd,-1,sizeof(hd)),cnt=0;

        //w=1000;
        //h=1000;

        all = h*w;
        int f = all*2 + 1;
        int t = all*2 + 2;
        for(int i=0;i<w;i++)
        for(int j=0;j<h;j++)
        {
            if(plot[i][j])continue;
            //printf("%d %d\n",i,j);
            //printf("%d %d\n",gid(i,j,0),gid(i,j,1));
            insert(gid(i,j,0),gid(i,j,1),1);
            if(j == 0)
                insert(f,gid(i,j,0),1);
            else
                insert(gid(i,j,1),gid(i,j-1,0),1);
            if(j == h-1)
                insert(gid(i,j,1),t,1);
            else
                insert(gid(i,j,1),gid(i,j+1,0),1);
            if(i > 0)
                insert(gid(i,j,1),gid(i-1,j,0),1);
            if(i < w-1)
                insert(gid(i,j,1),gid(i+1,j,0),1);
        }
        //printf("%d ",t+2);
        int ans = dinic(f,t,t+1);
        printf("Case #%d: %d\n",ca,ans);
    }
}
