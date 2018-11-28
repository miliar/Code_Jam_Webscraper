#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <algorithm>

using namespace std;

int vis[100][500],num,v2[100][500];
int w,h,n,X0,X1,Y0,Y1;

const int MaxN=(50000+5)*2;
const int MaxM=MaxN*10;
const int INF=(1<<29)-1;

typedef struct tNode{
    int v,f;
    tNode *nxt,*rev;
} Edge;

Edge E[MaxN],mem[MaxM*2];
Edge *Cur[MaxN];
int M,S,T,N,eCnt;
int gap[MaxN],d[MaxN];
int flow,aug;
bool done;

void Init(int SS,int TT,int NN){
    S=SS,T=TT,N=NN;
    eCnt=0;
    for(int i=0; i<N; i++) E[i].nxt=NULL;
}

void Add_edge(int u,int v,int f){
    Edge *p=&mem[eCnt++],*q=&mem[eCnt++];
    p->v=v,p->f=f,p->rev=q;
    p->nxt=E[u].nxt,E[u].nxt=p;
    q->v=u,q->f=0,q->rev=p;
    q->nxt=E[v].nxt,E[v].nxt=q;
}

void Sap(int u){
    if(u==T){
        done=true;
        flow+=aug;
        return ;
    }
    Edge *p=NULL;
    int augOri=aug;
    for(p=Cur[u]; p!=NULL; p=p->nxt){
        if(p->f<=0) continue;
        if(d[p->v]+1==d[u]){
            Cur[u]=p;
            aug=min(aug,p->f);
            Sap(p->v);
            if(d[S]>=N) return ;
            if(done) break;
            aug=augOri;
        }
    }
    if(done) p->f-=aug,p->rev->f+=aug;
    else{
        if(!(--gap[d[u]])) d[S]=N;
        int minD=N;
        Cur[u]=E[u].nxt;
        for(p=Cur[u]; p!=NULL; p=p->nxt)
            if(p->f>0) minD=min(minD,d[p->v]);
        d[u]=minD+1;
        gap[d[u]]++;
    }
}

int Maxflow(){
    for(int i=0; i<N; i++){
        gap[i]=d[i]=0;
        Cur[i]=E[i].nxt;
    }
    gap[0]=N;
    flow=0;
    while(d[S]<N){
        aug=INF;
        done=false;
        Sap(S);
    }
    return flow;
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("c-ans.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        scanf("%d%d%d",&w,&h,&n);
        for(int i=0;i<w;i++)
            for(int j=0;j<h;j++)
                vis[i][j]=1;
        for(int i=0;i<n;i++){
            scanf("%d%d%d%d",&X0,&Y0,&X1,&Y1);
            for(int j=X0;j<=X1;j++)
                for(int k=Y0;k<=Y1;k++)
                    vis[j][k]=0;
        }
        num=2;
        for(int i=0;i<w;i++)
            for(int j=0;j<h;j++)
                if(vis[i][j]){
                    vis[i][j]=num++;
                    v2[i][j]=num++;
                }
        Init(0,1,num);
        for(int i=0;i<w;i++){
            if(vis[i][0])Add_edge(0,vis[i][0],1);
            if(vis[i][h-1])Add_edge(v2[i][h-1],1,1);
        }
        for(int i=0;i<w;i++)
            for(int j=0;j<h;j++){
                if(!vis[i][j])continue;
                if(i&&vis[i-1][j])Add_edge(v2[i-1][j],vis[i][j],1);
                if(i+1<w&&vis[i+1][j])Add_edge(v2[i+1][j],vis[i][j],1);
                if(j&&vis[i][j-1])Add_edge(v2[i][j-1],vis[i][j],1);
                if(j+1<h&&vis[i][j+1])Add_edge(v2[i][j+1],vis[i][j],1);
                Add_edge(vis[i][j],v2[i][j],1);
            }
        printf("Case #%d: %d\n",cas,Maxflow());
    }
    return 0;
}
