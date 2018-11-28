#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;
int t, ct, w, h, n;
struct Edge{
    int from, to, cap, flow;
    Edge(){}
    Edge(int from, int to, int cap, int flow):from(from),to(to),cap(cap),flow(flow){}
};
#define N 1000010
#define pb push_back
vector<Edge> G;
vector<int> V[N];
void add(int from, int to, int cap){
    G.pb(Edge(from,to,cap,0));
    G.pb(Edge(to,from,0,0));
    int x = G.size();
    V[from].pb(x-2);
    V[to].pb(x-1);
}
bool B[510][510];
int id[510][510];
int xl[4]={-1,1,0,0};
int yl[4]={0,0,-1,1};
int tar;
const int inf = 0x7fffffff;
int d[N], cur[N];
bool bfs(){
    memset(d,-1,sizeof(d));
    d[0]=0;
    queue<int> Q;
    Q.push(0);
    while(!Q.empty()){
        int x=Q.front(); Q.pop();
        for(int i=0; i<V[x].size(); i++){
            Edge& e = G[V[x][i]];
            if(d[e.to]==-1 && e.cap>e.flow){
                d[e.to]=d[x]+1;
                Q.push(e.to);
            }
        }
    }
    return d[tar]!=-1;
}
int dfs(int x, int v){
    if(x==tar || v==0)  return v;
    int flow=0, f;
    for(int &i =cur[x]; i<V[x].size(); i++){
        int j=V[x][i];
        Edge& e = G[j];
        if(d[e.to]==d[x]+1 && (f=dfs(e.to, min(v, e.cap-e.flow)))>0){
            v-=f;
            flow+=f;
            e.flow+=f;
            G[j^1].flow-=f;
            if(!v)  break;
        }
    }
    return flow;
}
int max_flow(){
    int flow=0;
    while(bfs()){
        memset(cur,0,sizeof(cur));
        flow += dfs(0, inf);
    }
    return flow;
}
int main(){
    freopen("C-small-attempt4.in", "r", stdin);
    freopen("C-small-attempt4.out", "w", stdout);
    scanf("%d", &t);
    for(ct=1; ct<=t; ct++){
        scanf("%d %d %d", &w, &h, &n);
        memset(B,0,sizeof(B));
        int x1, y1, x2, y2;
        while(n--){
            scanf("%d %d %d %d", &y1, &x1, &y2, &x2);
            for(int i=x1; i<=x2; i++){
                for(int j=y1; j<=y2; j++)   B[i][j]=1;
            }
        }
        tar = 0;
        for(int i=0; i<h; i++){
            for(int j=0; j<w; j++){
                if(!B[i][j]){
                    id[i][j] = ++tar;
                }
            }
        }
        tar = tar*2+1;
        for(int i=0; i<=tar; i++)   V[i].clear();
        G.clear();
        for(int i=0; i<h; i++){
            for(int j=0; j<w; j++){
                if(!B[i][j]){
                    add(id[i][j]*2, id[i][j]*2+1, 1);
                    for(int k=0; k<4; k++){
                        int a = i+xl[k];
                        int b = j+yl[k];
                        if(a<0 || a>=h || b<0 || b>=w)  continue;
                        if(B[a][b]) continue;
                        add(id[a][b]*2+1, id[i][j]*2, 1);
                        add(id[i][j]*2+1, id[a][b]*2, 1);
                    }
                }
            }
        }
        for(int j=0; j<w; j++){
            if(!B[0][j])    add(0, id[0][j]*2, 1);
            if(!B[h-1][j])  add(id[h-1][j]*2+1, tar, 1);
        }
        printf("Case #%d: %d\n", ct, max_flow());
    }
    return 0;
}
