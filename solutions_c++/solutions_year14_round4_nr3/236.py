#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(a) (a).begin(),(a).end()
#define INIT(a) memset((a),0,sizeof(a))
#define fs first
#define sc second
#define pb push_back
#define sz size() 
using namespace std;
typedef long long ll;
typedef double D;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<string> vs;

const static int INF = 1e8;
const static D EPS = 1e-8;
const int dy[] = {-1,0,1,0}, dx[] = {0,1,0,-1};

struct edge{int to,cap,rev;};
const int MaxV = 110000;

vector<edge> g[MaxV];
bool used[MaxV];

void add_edge(int from, int to, int cap){
  g[from].pb((edge){to,cap,(int)g[to].sz});
  g[to].pb((edge){from,0,(int)g[from].sz-1});
}

int dfs(int v,int t, int f){
  if(v==t)return f;
  used[v] = true;
  rep(i,g[v].sz){
    edge &e = g[v][i];
    if(!used[e.to] && e.cap>0){
      int d = dfs(e.to, t, min(f,e.cap));
      if(d>0){
	e.cap -=d;
	g[e.to][e.rev].cap += d;
	return d;
      }
    }
  }
  return 0;
}

int max_flow(int s, int t){
  int flow = 0;
  for(;;){
    memset(used,0,sizeof(used));
    int f = dfs(s, t, INF);
    if(f==0)return flow;
    flow += f;
  }
}

int main(){
  int testcase;

  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    int w,h,b;
    cin >> w >> h >> b;

    bool grid[550][110];
    memset(grid,0,sizeof(grid));

    int x0,y0,x1,y1;
    rep(i,b){
      cin >> x0 >> y0 >> x1 >> y1;
      for(int i=y0;i<=y1;i++){
	for(int j=x0;j<=x1;j++){
	  grid[i][j] = true;
	}
      }
    }


    int V = 2*h*w;

    rep(i,V+2)g[i].clear();

    rep(i,h)rep(j,w){
      int node = 2*(i*w+j);
      if(!grid[i][j])add_edge(node, node+1, 1);
    }
    
    rep(i,w){
      add_edge(V,2*i,1);
      add_edge( 2*((h-1)*w+i)+1,V+1,1);
    }

    rep(y,h)rep(x,w){
      int cur = 2*(y*w + x)+1;

      rep(d,4){
	int ny = y+dy[d], nx = x+dx[d];
	if(ny<0 || ny>=h || nx<0 || nx>=w)continue;
	int nxt = 2*(ny*w + nx);
	add_edge(cur,nxt,1);
      }
    }

    cout << "Case #" << casenum << ": " << max_flow(V,V+1) << endl;
  }
}
