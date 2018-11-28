#include <bits/stdc++.h>
using namespace std;

#define debug(args...) fprintf(stderr,args)

typedef long long lint;
typedef pair<int,int> pii;
typedef pair<lint,lint> pll;

const int INF = 0x3f3f3f3f;
const lint LINF = 0x3f3f3f3f3f3f3f3fll;
const int MAXH = 510;

bool blocked[MAXH][MAXH];

typedef int FTYPE;      // define as needed

const int MAXV = 2*MAXH*MAXH;
const FTYPE FINF = INF; // infinite flow

struct Edge {
    int to;    
    FTYPE cap;
    Edge(int t, FTYPE c) { to = t; cap = c; }
};

vector<int> adj[MAXV];
vector<Edge> edge;
int ptr[MAXV], dinic_dist[MAXV];

// Inserts an edge u->v with capacity c
inline void add_edge(int u,int v,FTYPE c) {
    adj[u].push_back(edge.size());
    edge.push_back(Edge(v,c));
    adj[v].push_back(edge.size());
    edge.push_back(Edge(u,0)); // modify to Edge(u,c) if graph is non-directed
}

bool dinic_bfs(int _s,int _t) {
    memset(dinic_dist,-1,sizeof(dinic_dist));
    dinic_dist[_s] = 0;
    queue<int> q;
    q.push(_s);
    while(!q.empty() && dinic_dist[_t] == -1) {
        int v = q.front();
        q.pop();
        for(size_t a=0;a<adj[v].size();++a) {
            int ind = adj[v][a];
            int nxt = edge[ind].to;
            if(dinic_dist[nxt] == -1 && edge[ind].cap) {
                dinic_dist[nxt] = dinic_dist[v] + 1;
                q.push(nxt);
            }
        }
    }
    return dinic_dist[_t] != -1;
}

FTYPE dinic_dfs(int v,int _t,FTYPE flow) {
    if(v == _t) return flow;
    for(int &a = ptr[v];a<(int)adj[v].size();++a) {
        int ind = adj[v][a];
        int nxt = edge[ind].to;
        if(dinic_dist[nxt] == dinic_dist[v] + 1 && edge[ind].cap) {
            FTYPE got = dinic_dfs(nxt,_t,min(flow,edge[ind].cap));
            if(got) {
                edge[ind].cap -= got;
                edge[ind^1].cap += got;
                return got;
            }
        }
    }
    return 0;
}

FTYPE dinic(int _s,int _t) {
    FTYPE ret = 0, got;
    while(dinic_bfs(_s,_t)) {
        memset(ptr,0,sizeof(ptr));
        while((got = dinic_dfs(_s,_t,FINF))) ret += got;
    }
    return ret;
}

// Clears dinic structure
inline void dinic_clear() {
    for(int a=0;a<MAXV;++a) adj[a].clear();
    edge.clear();
}

int w,h,n;

inline int ind(int l,int c) {
    return w*l+c;
}

int main() {
    int tt=1,T;
    for(scanf("%d",&T);tt<=T;++tt) {
        dinic_clear();
        scanf("%d%d%d",&w,&h,&n);
        memset(blocked,0,sizeof(blocked));
        for(int a=0;a<n;++a) {
            int x0,y0,x1,y1;
            scanf("%d%d%d%d",&x0,&y0,&x1,&y1);
            for(int l=y0;l<=y1;++l)
                for(int c=x0;c<=x1;++c)
                    blocked[l][c] = 1;
        }
        for(int l=0;l<h;++l) {
            for(int c=0;c<w;++c) {
                if(blocked[l][c]) continue;
                add_edge(2*ind(l,c), 2*ind(l,c)+1, 1);
                if(c+1 < w && !blocked[l][c+1]) {
                    add_edge(2*ind(l,c)+1, 2*ind(l,c+1), 1);
                    add_edge(2*ind(l,c+1)+1, 2*ind(l,c), 1);
                }
                if(l+1 < h && !blocked[l+1][c]) {
                    add_edge(2*ind(l,c)+1, 2*ind(l+1,c), 1);
                    add_edge(2*ind(l+1,c)+1, 2*ind(l,c), 1);
                }
            }
        }
        int s = 2*w*h, t = 2*w*h+1;
        for(int a=0;a<w;++a) {
            add_edge(s,2*ind(0,a), 1);
            add_edge(2*ind(h-1,a)+1,t,1);
        }
        printf("Case #%d: %d\n",tt,dinic(s,t));        
    }        
    return 0;
}
