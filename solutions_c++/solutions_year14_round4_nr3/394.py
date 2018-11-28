#include<bits/stdc++.h>
using namespace std;

#define CLR(a,x) memset(a,x,sizeof(a))
#define PB push_back
#define INF 1000000000
#define MOD 1000000007
#define MP make_pair
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define REP(i,a) FOR(i,0,a)
#define LL long long
#define VI vector < int >
#define PII pair < int , int >

vector < int > cap;
vector < int > rcap;
vector < vector < PII > > edge;
void add_edge(int u, int v, int f) {
  edge[u].PB(MP(v,(int)cap.size()));
  edge[v].PB(MP(u,-((int)rcap.size()+1)));
  cap.PB(1);
  rcap.PB(0);
}
int burn;
int vis[500*500];
int dfs(int cur, int sink) {
  if(cur == sink) return 1;
  if(vis[cur]== burn) return 0;
  vis[cur] = burn;
  int sz = (int)edge[cur].size();
  for(int i=0;i<sz;i++) {
    PII nx = edge[cur][i];
    if(nx.second < 0) {
      if(rcap[-nx.second-1]) {
        if(dfs(nx.first, sink)) {
          rcap[-nx.second-1] = 0;
          cap[-nx.second-1] = 1;
          return 1;
        }
      }
    } else {
      if(cap[nx.second]) {
        if(dfs(nx.first, sink)) {
          cap[nx.second] = 0;
          rcap[nx.second] = 1;
          return 1;
        }
      }
    }
  }
  return 0;
}
int w, h;
int isin(int p, int q) {
  return p>=0&&q>=0&&p<h&&q<w;
}
int dx[] = {1,0,-1,0};
int dy[] = {0,1,0,-1};
int avail[500+5][500+5];
int main() {
  int t,n;
  scanf("%d",&t);
  while(t--) {
    scanf("%d%d%d",&w,&h,&n);
    fill(&avail[0][0], &avail[0][0] + sizeof(avail)/sizeof(avail[0][0]), 1);
    for(int i=0;i<n;i++) {
      int x0, y0, x1, y1;
      scanf("%d%d%d%d",&x0,&y0,&x1,&y1);
      for(int x=x0;x<=x1;x++)
        for(int y=y0;y<=y1;y++)
          avail[y][x] = 0;
    }
    int area = w*h;
    int nodes = 2*area + 2;
    cap.clear();
    rcap.clear();
    edge.clear();edge.resize(nodes);
    for(int i=0;i<h;i++) {
      for(int j=0;j<w;j++) {
        if(avail[i][j] == 0) continue;
        for(int dir = 0;dir<4;dir++) {
          int nx = i + dx[dir];
          int ny = j + dy[dir];
          if(!isin(nx,ny))continue;
          add_edge(i*w + j + area, nx*w+ny, 1);
        }
        add_edge(i*w+j, i*w+j+area, 1);
      }
    }
    int source = 2*area;
    int sink = 2*area + 1;
    for(int j=0;j<w;j++) {
      add_edge(source, j, 1);
      add_edge((h-1)*w+j+area, sink, 1);
    }
    int ans = 0;
    burn++;
    while(dfs(source, sink)) {
      burn++;
      ans++;
    }
    int static kase = 1;
    printf("Case #%d: %d\n",kase++, ans);
    fprintf(stderr,"Case #%d: %d\n",kase, ans);
  }
  return 0;
}
