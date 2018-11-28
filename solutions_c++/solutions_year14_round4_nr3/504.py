#include<bits/stdc++.h>
#define MAX   555
#define FOR(i,a,b) for (int i=(a);i<=(b);i=i+1)
#define REP(i,n) for (int i=0;i<(n);i=i+1)
using namespace std;
const int INF=(int)1e9+7;
class DinicFlow {
    private:
    vector<int> dist,head,q,work;
    vector<int> point,capa,flow,next;
    int n,m;
    public:
    DinicFlow() {
        n=0;m=0;
    }
    DinicFlow(int n) {
        this->n=n;m=0;
        dist.assign(n+7,0);
        head.assign(n+7,-1);
        q.assign(n+7,0);
        work.assign(n+7,0);
    }
    void addedge(int u,int v,int c1,int c2) {
        point.push_back(v);capa.push_back(c1);flow.push_back(0);next.push_back(head[u]);head[u]=m++;
        point.push_back(u);capa.push_back(c2);flow.push_back(0);next.push_back(head[v]);head[v]=m++;
    }
    bool bfs(int s,int t) {
        FOR(i,1,n) dist[i]=-1;
        int sz=0;
        q[sz++]=s;dist[s]=0;
        REP(x,sz) {
            int u=q[x];
            for (int i=head[u];i>=0;i=next[i])
                if (dist[point[i]]<0 && flow[i]<capa[i]) {
                    dist[point[i]]=dist[u]+1;
                    q[sz++]=point[i];
                }
        }
        return (dist[t]>=0);
    }
    int dfs(int s,int t,int f) {
        if (s==t) return (f);
        for (int &i=work[s];i>=0;i=next[i])
            if (dist[point[i]]==dist[s]+1 && flow[i]<capa[i]) {
                int d=dfs(point[i],t,min(f,capa[i]-flow[i]));
                if (d>0) {
                    flow[i]+=d;
                    flow[i^1]-=d;
                    return (d);
                }
            }
        return (0);
    }
    int getflow(int s,int t) {
        int totflow=0;
        while (bfs(s,t)) {
            FOR(i,1,n) work[i]=head[i];
            while (true) {
                int d=dfs(s,t,INF);
                if (d<=0) break;
                totflow+=d;
            }
        }
        return (totflow);
    }
};
bool a[MAX][MAX];
int m,n;
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};
void init(void) {
    scanf("%d%d",&m,&n);
    memset(a,0,sizeof a);
    int t;
    scanf("%d",&t);
    REP(zz,t) {
        int x1,y1,x2,y2;
        scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
        FOR(i,x1,x2) FOR(j,y1,y2) a[i][j]=true;
    }
}
bool inside(int x,int y) {
    if (x<0) return (false);
    if (y<0) return (false);
    if (x>=m) return (false);
    if (y>=n) return (false);
    return (!a[x][y]);
}
inline int nid(int x,int y,bool t) {
    return (x*n+y+1+m*n*t);
}
void process(int tc) {
    DinicFlow G=DinicFlow(m*n*2+2);
    int src=2*m*n+1;
    int snk=2*m*n+2;
    REP(i,m) G.addedge(src,nid(i,0,0),1,0);
    REP(i,m) REP(j,n) if (!a[i][j]) G.addedge(nid(i,j,0),nid(i,j,1),1,0);
    REP(i,m) REP(j,n) if (!a[i][j]) REP(k,4) {
        int x=i+dx[k];
        int y=j+dy[k];
        if (inside(x,y)) G.addedge(nid(i,j,1),nid(x,y,0),1,0);
    }
    REP(i,m) G.addedge(nid(i,n-1,1),snk,1,0);
    printf("Case #%d: %d\n",tc,G.getflow(src,snk));
}
int main(void) {
    int tc;
    scanf("%d",&tc);
    FOR(i,1,tc) {
        init();
        process(i);
    }
    return 0;
}
