#include <bits/stdc++.h>
using namespace std;


#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair


typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;

struct maxflow {
	static const int INF = 1<<29;

	struct edge {
		int u, v, cap, flow;
		int rem() { return cap - flow; }
	};

	int n;
	vi *adj;
	vector<edge> e;

	maxflow(int n): n(n) {
		adj = new vi[n];
		e.clear();
	}

	void addEdge(int u, int v, int cap) {
		adj[u].pb(si(e)); e.pb((edge){u,v,cap,0});
		adj[v].pb(si(e)); e.pb((edge){v,u,0,0});
	}

	int *dist, *pre, *cap;
	int flow(int s, int t) {
		dist = new int[n];
		pre = new int[n];
		cap = new int[n];

		int res = 0;
		for (;;) {
			fill(dist, dist+n, (int)INF); dist[s] = 0;
			fill(pre, pre+n, -1);
			fill(cap, cap+n, 0); cap[s] = INF;

			queue<int> q; q.push(s);
			while (!q.empty()) {
				int u = q.front(); q.pop();
				if (u == t) break;

				forn(i,si(adj[u])) {
					edge E = e[adj[u][i]];
					if (E.rem() > 0 && dist[E.v] == INF) {
						dist[E.v] = dist[u] + 1;
						pre[E.v] = adj[u][i];
						cap[E.v] = min(cap[u], E.rem());
						q.push(E.v);
					}
				}
			}
			if (pre[t] == -1) break;
			res += cap[t];
			for (int v = t; v != s; ) {
				int u = e[pre[v]].u;
				e[pre[v]].flow += cap[t];
				e[pre[v]^1].flow -= cap[t];
				v = u;
			}
		}

		return res;
	}
};

maxflow F(0);
const int di[] = {0,1,0,-1}, dj[] = {1,0,-1,0};


const int MAXN = 500 + 50;

int m,n;
bool block[MAXN][MAXN];

int main() {
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);

        int ncas; cin >> ncas;
        forn(cas, ncas) {
        	cout << "Case #" << cas+1 << ": ";

        	int b; cin >> n >> m >> b;
        	fill(block[0], block[MAXN], false);
        	forn(_,b) {
        		int x0,y0,x1,y1; cin >> x0 >> y0 >> x1 >> y1;
        		forsn(j,x0,x1+1) forsn(i,y0,y1+1) block[i][j] = true;
        	}

        	int N = 2*m*n;
        	int s = N++, t = s+1;

        	F = maxflow(N+2);
        	forn(j,n) {
        		if (!block[0][j]) F.addEdge(s,2*j,1);
        		if (!block[m-1][j]) F.addEdge(2*((m-1)*n+j)+1, t,1);
        	}

        	forn(i,m) forn(j,n) if (!block[i][j]) {
        		int u = i*n+j;
        		F.addEdge(2*u, 2*u+1,1);

        		forn(d,4) {
        			int ni = i + di[d], nj = j + dj[d];
        			if (ni < 0 || ni >= m || nj < 0 || nj >= n || block[ni][nj]) continue;

        			int v = ni*n + nj;
        			F.addEdge(2*u+1, 2*v, 1);
        		}
        	}
        	cout << F.flow(s,t) << endl;   
        }

        return 0;
}
