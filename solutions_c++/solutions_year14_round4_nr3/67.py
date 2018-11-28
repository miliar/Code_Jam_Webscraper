#include<bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)n;i++)
#define all(c) (c).begin(),(c).end()
#define mp make_pair
#define pb push_back
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dbg(x) cerr<<__LINE__<<": "<<#x<<" = "<<(x)<<endl

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
const int inf = (int)1e9;
const double INF = 1e12, EPS = 1e-9;

/*
struct flowGraph{
	struct edge{ int to, cap, rev; };
	
	int n, *level, *iter;
	vector<vector<edge> > G;
	
	flowGraph(int sz) : n(sz){
		G.resize(n);
		iter = new int[n]; level = new int[n];
	}
	~flowGraph(){
		delete iter; delete level;
	}
	
	void add(int s, int t, int cap){
		G[s].pb((edge){t, cap, G[t].size()});
		G[t].pb((edge){s, 0, G[s].size() - 1});
	}
	void bfs(int s){
		rep(i, n) level[i] = -1;
		queue<int> q;
		level[s] = 0;
		q.push(s);
		while(!q.empty()){	
			int v = q.front();
			q.pop();
			rep(i, G[v].size()){
				edge &e = G[v][i];
				if(e.cap > 0 && level[e.to] < 0){
					level[e.to] = level[v] + 1;
					q.push(e.to);
				}
			}
		}
	}
	int dfs(int v, int t, int f){
		if(v == t) return f;
		for(int &i = iter[v]; i < (int)G[v].size(); i++){
			edge &e = G[v][i];
			if(e.cap > 0 && level[v] < level[e.to]){
				int d = dfs(e.to, t, min(f, e.cap));
				if(d > 0){
					e.cap -= d;
					G[e.to][e.rev].cap += d;
					return d;
				}
			}
		}
		return 0;
	}
	int max_flow(int s, int t){
		int flow = 0;
		while(1){
			bfs(s);
			if(level[t] < 0) return flow;
			rep(i, n) iter[i] = 0;
			int f;
			while((f = dfs(s, t, inf)) > 0) flow += f;
		}
	}
};

const int dy[] = {-1, 0, 1, 0}, dx[] = {0, -1, 0, 1};
*/

int w, h, b;
//bool f[100][500];

#define F first
#define S second

void solve(){
	cin >> w >> h >> b;
	vector<pair<pi, pi> > v;
	
	//memset(f, 0, sizeof(f));
	
	rep(i, b){
		int x, y, X, Y;
		cin >> x >> y >> X >> Y;
		//for(int j = x; j <= X; j++) for(int k = y; k <= Y; k++) f[j][k] = 1;
		
		v.pb(mp(mp(x, y), mp(X, Y)));
	}
	bool use[1000] = {};
	int ans = w;
	priority_queue<pi> q;
	
	rep(i, v.size()) q.push(mp(-v[i].F.F, i));
	
	while(!q.empty()){
		int d = -q.top().F, cur = q.top().S; q.pop();
		
		if(use[cur] || d >= w) continue;
		use[cur] = 1;
		//dbg(cur); dbg(d);
		ans = min(ans, d + w - 1 - v[cur].S.F);
		
		rep(i, v.size()) if(!use[i]){
			
			int dx, dy;
			
			if(v[i].S.F < v[cur].F.F || v[cur].S.F < v[i].F.F){
				
				if(v[i].S.F < v[cur].F.F) dx = v[cur].F.F - v[i].S.F - 1;
				else dx = v[i].F.F - v[cur].S.F - 1;
			}
			else dx = 0;
			
			if(v[i].S.S < v[cur].F.S || v[cur].S.S < v[i].F.S){
				
				if(v[i].S.S < v[cur].F.S) dy = v[cur].F.S - v[i].S.S - 1;
				else dy = v[i].F.S - v[cur].S.S - 1;
			}
			else dy = 0;
			
			//cerr<<"cur: "<<cur<<" i: "<<i<<" dx: "<<dx<<" dy: "<<dy<<endl;
			
			q.push(mp(-d - max(dx, dy), i));
		}
	}
	
	/*
	dbg(ans);
	rep(i, w) rep(j, h) cerr<<f[i][j]<<(j==h-1?"\n":" ");
	
	int s = w * h * 2, t = w * h * 2 + 1;
	flowGraph g(w * h * 2 + 2);
	
	rep(i, w) rep(j, h) if(!f[i][j]){
		g.add((i * h + j) * 2, (i * h + j) * 2 + 1, 1);
		
		rep(d, 4){
			int nx = i + dx[d], ny = j + dy[d];
			if(nx < 0 || nx >= w || ny < 0 || ny >= h || f[nx][ny]) continue;
			
			g.add((i * h + j) * 2 + 1, (nx * h + ny) * 2, 1);
		}
	}
	rep(i, w) g.add(s, i * h * 2, 1), g.add((i * h + h - 1) * 2 + 1, t, 1);
	
	int ans_naive = g.max_flow(s, t);
	assert(ans_naive == ans);
	*/
	
	cout << ans << endl;
}

int main(){
	int cs; cin >> cs;
	rep(CS, cs){
		cout << "Case #" << CS + 1 << ": ";
		solve();
	}
	return 0;
}