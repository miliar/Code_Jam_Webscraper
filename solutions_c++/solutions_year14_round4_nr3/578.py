#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <utility>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <climits>
#include <cassert>
#include <memory>
#include <time.h>
using namespace std;
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long ll;
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
const double EPS = 1e-9;
const double PI  = acos(-1.0);

typedef int Weight;
struct Edge {
  int src, dst;
  Weight weight;
  Edge(int src, int dst, Weight weight) :
    src(src), dst(dst), weight(weight) { }
};
bool operator < (const Edge &e, const Edge &f) {
  return e.weight != f.weight ? e.weight > f.weight : // !!INVERSE!!
    e.src != f.src ? e.src < f.src : e.dst < f.dst;
}
typedef vector<Edge> Edges;
typedef vector<Edges> Graph;

typedef vector<Weight> Array;
typedef vector<Array> Matrix;

#define EACH(a,b,t) for(t::const_iterator a=(b).begin();a!=(b).end();a++)
const int INF=INT_MAX/10;

//#define RESIDUE(s,t) (capacity[s][t]-flow[s][t])
//Weight augment(const Graph &g, const Matrix &capacity, Matrix &flow,
//    const vector<int> &level, vector<bool> &finished, int u, int t, Weight cur) {
//  if (u == t || cur == 0) return cur;
//  if (finished[u]) return 0;
//  finished[u] = true;
//  EACH(e, g[u],Edges) if (level[e->dst] > level[u]) {
//    Weight f = augment(g, capacity, flow, level, finished,
//        e->dst, t, min(cur, RESIDUE(u, e->dst)));
//    if (f > 0) {
//      flow[u][e->dst] += f; flow[e->dst][u] -= f;
//      finished[u] = false;
//      return f;
//    }
//  }
//  return 0;
//}
//Weight maximumFlow(const Graph &g, int s, int t) {
//  int n = g.size();
//  Matrix flow(n, Array(n)), capacity(n, Array(n)); // adj. matrix
//  REP(u,n) EACH(e,g[u],Edges) capacity[e->src][e->dst] += e->weight;
//
//  Weight total = 0;
//  for (bool cont = true; cont; ) {
//    cont = false;
//    vector<int> level(n, -1); level[s] = 0; // make layered network
//    queue<int> Q; Q.push(s);
//    for (int d = n; !Q.empty() && level[Q.front()] < d; ) {
//      int u = Q.front(); Q.pop();
//      if (u == t) d = level[u];
//      EACH(e, g[u],Edges) if (RESIDUE(u,e->dst) > 0 && level[e->dst] == -1)
//        Q.push(e->dst), level[e->dst] = level[u] + 1;
//    }
//    vector<bool> finished(n); // make blocking flows
//    for (Weight f = 1; f > 0; ) {
//      f = augment(g, capacity, flow, level, finished, s, t, INT_MAX/10);
//      if (f == 0) break;
//      total += f; cont = true;
//    }
//  }
//  return total;
//}


//#define RESIDUE(s,t) (capacity[s][t]-flow[s][t])
//Weight maximumFlow(const Graph &g, int s, int t) {
//  int n = g.size();
//  Matrix flow(n, Array(n)), capacity(n, Array(n));
//  REP(u,n) EACH(e,g[u],Edges) capacity[e->src][e->dst] += e->weight;
//
//  Weight total = 0;
//  while (1) {
//    queue<int> Q; Q.push(s);
//    vector<int> prev(n, -1); prev[s] = s;
//    while (!Q.empty() && prev[t] < 0) {
//      int u = Q.front(); Q.pop();
//      EACH(e,g[u],Edges) if (prev[e->dst] < 0 && RESIDUE(u, e->dst) > 0) {
//        prev[e->dst] = u;
//        Q.push(e->dst);
//      }
//    }
//    if (prev[t] < 0) return total; // prev[x] == -1 <=> t-side
//    Weight inc = INT_MAX/10;
//    for (int j = t; prev[j] != j; j = prev[j])
//      inc = min(inc, RESIDUE(prev[j], j));
//    for (int j = t; prev[j] != j; j = prev[j])
//      flow[prev[j]][j] += inc, flow[j][prev[j]] -= inc;
//    total += inc;
//  }
//}



//#define RESIDUE(s,t) (capacity[s][t]-flow[s][t])
//
//#define GLOBAL_RELABELING() { \
//  queue<int> Q; Q.push(t); \
//  fill(ALL(d), INF); d[t] = 0; \
//  while (!Q.empty()) { \
//    int u = Q.front(); Q.pop(); \
//    EACH(e, g[u],Edges) if (RESIDUE(e->dst, u) > 0 && d[u] + 1 < d[e->dst])  \
//      Q.push(e->dst), d[e->dst] = d[u] + 1; \
//  } \
//}
//#define PUSH(u, v) { \
//  Weight delta = min(excess[u], RESIDUE(u, v)); \
//  flow[u][v] += delta; flow[v][w] -= delta; \
//  excess[u] -= delta; excess[v] += delta; }
//Weight maximumFlow(const Graph &g, int s, int t) {
//  int n = g.size(), count = 0;
//  Matrix flow(n, Array(n)), capacity(n, Array(n)); // adj. matrix
//  REP(u,n) EACH(e,g[u],Edges) capacity[e->src][e->dst] += e->weight;
//
//  vector<Weight> excess(n); excess[s] = INF; // initialize step
//  vector<int> d(n);
//  GLOBAL_RELABELING();
//  vector< queue<int> > B(n); B[ d[s] ].push( s );
//
//  for (int b = d[s]; b >= 0; ) {
//    if (B[b].empty()) { --b; continue; }
//    int v = B[b].front(); B[b].pop();
//    if (excess[v] == 0 || v == t) continue;
//
//    EACH(e, g[v],Edges) {
//      int w = e->dst; // e is the current edge of v
//      if (RESIDUE(v,w) > 0 && d[v] == d[w] + 1) { // (w,v) is admissible
//        PUSH(v, w);
//        if (excess[w] > 0 && w != t) B[d[w]].push( w );
//      }
//    }
//    if (excess[v] == 0) continue;
//    d[v] = n;
//    EACH(e, g[v],Edges) if (RESIDUE(v, e->dst) > 0)
//      d[v] = min(d[v], d[e->dst] + 1);
//    if (d[v] < n) B[b = d[v]].push(v);
//
//    if (++count % n == 0) GLOBAL_RELABELING(); // !!HEURISTICS
//  }
//  return excess[t];
//}

struct edge{int to,cap,rev;
edge(int to,int cap,int rev):to(to),cap(cap),rev(rev){}
};
const int MAX_V=500*100*2+10;
vector<edge> G[MAX_V];
bool used[MAX_V];

void add_edge(int from,int to,int cap){
	G[from].push_back(edge(to,cap,G[to].size()));
	G[to].push_back(edge(from,0,G[from].size()-1));
}

int dfs(int v, int t, int f){
	if(v==t)return f;
	used[v]=true;
	for(int i=0;i<G[v].size();i++){
		edge &e=G[v][i];
		if(!used[e.to]&&e.cap>0){
			int d=dfs(e.to,t,min(f,e.cap));
			if(d>0){
				e.cap-=d;
				G[e.to][e.rev].cap+=d;
				return d;
			}
		}
	}
	return 0;
}
int max_flow(int s,int t){
	int flow=0;
	for(;;){
		memset(used,0,sizeof(used));
		int f=dfs(s,t,INF);
		if(f==0)return flow;
		flow+=f;
	}
}

int dy[4]={-1,0,1,0};
int dx[4]={0,-1,0,1};

int get_node_index(int y,int x,int h,int w,int isout){
	return y*w+isout*h*w+x;
}

int main(){
	int num_cases;
	cin>>num_cases;
	REP(test,num_cases){
		REP(i,MAX_V){
			G[i]=vector<edge>();
			used[i]=false;
		}

		int w,h,b;
		cin>>w>>h>>b;
		//Graph g(w*h*2+2);
		vector<set<int>> gm(w*h,set<int>());
		REP(i,b){
			int x0,y0,x1,y1;
			cin>>x0>>y0>>x1>>y1;
			FOR(x,x0,x1+1){
				FOR(y,y0,y1+1){
					REP(d,4){
						int yy=y+dy[d];
						int xx=x+dx[d];
						if(yy>=0&&xx>=0&&yy<h&&xx<w){
							int src=get_node_index(y,x,h,w,0);
							int dst=get_node_index(yy,xx,h,w,0);

							gm[src].insert(dst);
							gm[dst].insert(src);
						}
					}
				}
			}
		}
		REP(y,h){
			REP(x,w){
				REP(d,4){
					int yy=y+dy[d];
					int xx=x+dx[d];
					if(yy>=0&&xx>=0&&yy<h&&xx<w){
						int src0=get_node_index(y,x,h,w,0);
						int src1=get_node_index(y,x,h,w,1);
						int dst=get_node_index(yy,xx,h,w,0);

						if(!EXIST(gm[src0],dst)){
							add_edge(src1,dst,1);
							//g[src1].push_back(Edge(src1,dst,1));
						}
					}
				}
			}
		}
		REP(y,h){
			REP(x,w){
				int in=get_node_index(y,x,h,w,0);
				int out=get_node_index(y,x,h,w,1);

				add_edge(in,out,1);
				//g[in].push_back(Edge(in,out,1));
			}
		}

		REP(x,w){
			add_edge(w*h*2,get_node_index(0,x,h,w,0),1);
			add_edge(get_node_index(h-1,x,h,w,1),w*h*2+1,1);
			//g[w*h*2].push_back(Edge(w*h*2,get_node_index(0,x,h,w,0),1));
			//g[get_node_index(h-1,x,h,w,1)].push_back(Edge(get_node_index(h-1,x,h,w,1),w*h*2+1,1));
		}
		Weight ans=max_flow(w*h*2,w*h*2+1);
		cout<<"Case #"<<test+1<<": "<<ans<<endl;
	}
}