#include <bits/stdc++.h>
using namespace std;
//min-cost max-flow implementation nicked from the internet
typedef unsigned long long      ui64;
typedef long long               i64;
typedef    vector<int>             VI;
typedef	vector<bool>            VB;
typedef	vector<VI>              VVI;
typedef	vector<string>          VS;
typedef	pair<int,int>           PII;
typedef map<string,int>         MSI;
typedef set<int>                SI;
typedef set<string>             SS;
typedef complex<double>         CD;
typedef vector< CD >            VCD;
typedef map<int,int>            MII;
typedef	pair<double,double>     PDD;
 
#define PB                      push_back
#define MP                      make_pair
#define X                       first
#define Y                       second
#define FOR(i, a, b)            for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b)           for(int i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b)             memset(a, b, sizeof(a))
#define SZ(a)                   int((a).size())
#define ALL(a)                  (a).begin(), (a).end()
#define RALL(a)                 (a).rbegin(), (a).rend()
 
#ifdef _DEBUG
#define eprintf(...) fprintf (stderr, __VA_ARGS__)
#else
#define eprintf(...) assert (true)
#endif
 
const double PI = acos(-1.0);
 
typedef int FLOW;
typedef int COST;
const COST INF = 1000000000;
const FLOW FLOW_INF = 1000000000;
const int MAXN = 10000;
struct Edge {
	int b, c, u, f, back;
};
 
class MCMF {
private:
	int s, t, n;
	vector<Edge> g[MAXN];
	int *from, *from_edge, *d, *phi, *state, *q;
	bool *used;
 
public:
	MCMF(int _s, int _t, int _n) {
		s = _s;
		t = _t;
		n = _n;
		from = new int[n];
		from_edge = new int[n];
		d = new int[n];
		state = new int[n];
		q = new int[n];
		phi = new int[n];
		FOR(i,0,n)
			phi[i] = 0;
		used = new bool[n];
	}
	void addEdge(int a, int b, int c, int u) {
		Edge e1 = {b,c,u,0,SZ(g[b])};
		Edge e2 = {a,-c,0,0,SZ(g[a])};
		g[a].PB(e1);
		g[b].PB(e2);
	}
 
	void levit() {
		int qh, qt;
		qh = 0, qt = 0;
 
		FOR(i,0,n) state[i] = 2, d[i] = INF;
		memset(from,-1,sizeof(from));
 
		state[s] = 1;
		q[qh++] = s;
		d[s] = 0;
		while(qh!=qt) {
			int v = q[qt++];
			qt %= n;
			state[v] = 0;
			FOR(i,0,SZ(g[v])) if(g[v][i].f < g[v][i].u && d[g[v][i].b] > d[v] + g[v][i].c) {
				int to = g[v][i].b;
				d[to] = d[v] + g[v][i].c;
				from[to] = v;
				from_edge[to] = i;
				if(state[to]==1)
					continue;
				if(state[to]==0) {
					qt--;if(qt==-1) qt = n-1;q[qt] = to;
					state[to] = 1;
				}
				else {
					state[to] = 1;
					q[qh++] = to;
					qh %= n;
				}
			}
		}
	}
 
	void dijkstra() {
		memset(used,true,sizeof(used));
		used[s] = false;
		FOR(i,0,n)
			d[i] = INF;
 
		d[s] = 0;
 
		while(true) {
			int v = -1;
			for(int i=0;i<n;i++) {
				if(!used[i] && (v==-1 || d[v] > d[i]))
					v = i;
			}
			if(v==-1)
				break;
			used[v] = true;
			FOR(i,0,SZ(g[v])) if(g[v][i].f < g[v][i].u) {
				int to = g[v][i].b;
				if( d[to] > d[v] + g[v][i].c + phi[v] - phi[to] ) {
					d[to] = d[v] + g[v][i].c + phi[v] - phi[to];
					from[to] = v;
					from_edge[to] = i;
					used[to] = false;
				}
			}
		}
	}
 
	pair<FLOW,COST> minCostMaxFlow() {
		FLOW flow = 0;
		COST cost = 0;
		while(true) {
			//levit();
			dijkstra();
			for (int i = 0; i < n; i++)
				phi[i] += d[i];
			if(d[t]==INF)
				break;
			int it = t;
			FLOW addflow = FLOW_INF;
			while(it!=s) {
				addflow = min(addflow, g[from[it]][from_edge[it]].u - g[from[it]][from_edge[it]].f);
				it = from[it];
			}
			it = t;
			while(it!=s) {
				g[from[it]][from_edge[it]].f += addflow;
				g[it][g[from[it]][from_edge[it]].back].f -= addflow;
				cost += g[from[it]][from_edge[it]].c * addflow;
 
				it = from[it];
			}
			flow += addflow;
		}
		return MP(flow, cost);
	}
};
//
string board[105];
int ind[105][105];
int main()
{
	// freopen("a_input.txt", "r", stdin);
	freopen("a_small.in", "r", stdin);
	freopen("a_small.out", "w", stdout);
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	for (int case_num = 1; case_num <= t; ++case_num)
	{
		int r,c;
		cin>>r>>c;
		for (int i = 0; i < r; ++i)
		{
			cin>>board[i];
		}
		int src = 0;
		int ctr = 1;
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
			{
				if(board[i][j] != '.')
					ind[i][j] = ctr++;
				// cout<<ind[i][j]<<" ";
			}
			// cout<<"\n";
		}
		int s1_count = ctr-1;
		int outside = 2*s1_count+1;
		int sink = outside+1;
		// cout<<s1_count<<" "<<outside<<" "<<sink<<"\n";
		MCMF curr_graph(src,sink,sink+1);
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
			{
				if(board[i][j] != '.')
				{
					// cout<<"\n";
					curr_graph.addEdge(src,ind[i][j],0,1);
					curr_graph.addEdge(ind[i][j]+s1_count,sink,0,10000);
					//up
					int temp = i-1;
					while(temp >= 0 && board[temp][j]=='.')
						temp--;
					if(temp < 0)
					{
						if(board[i][j] == '^')
							curr_graph.addEdge(ind[i][j],outside,0,1);
						else
							curr_graph.addEdge(ind[i][j],outside,1,1);
					}
					else
					{
						if(board[i][j] == '^')
							curr_graph.addEdge(ind[i][j],ind[temp][j]+s1_count,0,1);
						else
							curr_graph.addEdge(ind[i][j],ind[temp][j]+s1_count,1,1);
					}
					//down
					temp = i+1;
					while(temp < r && board[temp][j] == '.')
						temp++;
					if(temp >= r)
					{
						if(board[i][j] == 'v')
							curr_graph.addEdge(ind[i][j],outside,0,1);
						else
							curr_graph.addEdge(ind[i][j],outside,1,1);
					}
					else
					{
						if(board[i][j] == 'v')
							curr_graph.addEdge(ind[i][j],ind[temp][j]+s1_count,0,1);
						else
							curr_graph.addEdge(ind[i][j],ind[temp][j]+s1_count,1,1);
					}
					//left
					temp = j-1;
					while(temp >= 0 && board[i][temp] == '.')
						temp--;
					if(temp < 0)
					{
						if(board[i][j] == '<')
							curr_graph.addEdge(ind[i][j],outside,0,1);
						else
							curr_graph.addEdge(ind[i][j],outside,1,1);
					}
					else
					{
						if(board[i][j] == '<')
							curr_graph.addEdge(ind[i][j],ind[i][temp]+s1_count,0,1);
						else
							curr_graph.addEdge(ind[i][j],ind[i][temp]+s1_count,1,1);
					}
					//right
					temp = j+1;
					while(temp < c && board[i][temp] == '.')
						temp++;
					if(temp >= c)
					{
						if(board[i][j] == '>')
							curr_graph.addEdge(ind[i][j],outside,0,1);
						else
							curr_graph.addEdge(ind[i][j],outside,1,1);
					}
					else
					{
						if(board[i][j] == '>')
							curr_graph.addEdge(ind[i][j],ind[i][temp]+s1_count,0,1);
						else
							curr_graph.addEdge(ind[i][j],ind[i][temp]+s1_count,1,1);
					}
				}
			}
		}
		curr_graph.addEdge(outside,sink,100000,1);
		pair<FLOW,COST> ans = curr_graph.minCostMaxFlow();
		if(ans.second >= 100000)
			cout<<"Case #"<<case_num<<": IMPOSSIBLE\n";
		else
			cout<<"Case #"<<case_num<<": "<<ans.second<<"\n";
	}
	return 0;
}