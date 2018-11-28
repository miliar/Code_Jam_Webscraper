/* by Ashar Fuadi (fushar) */

#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for (int i = 0, _n = (int)n; i < _n; i++)
#define FOR(i,a,b) for (int i = (int)a, _b = (int)b; i <= _b; i++)
#define RESET(c,v) memset(c, v, sizeof(c))
#define FOREACH(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

#define pb push_back
#define mp make_pair

int T;
int W, H, B;
bool occ[100][500];

inline int in(int x)
{
	return 2*x;
}

inline int out(int x)
{
	return 2*x + 1;
}

inline int id(int x, int y)
{
	return x*H + y;
}

struct edge
{
	int x, y, cap, cost;
	edge(int _x, int _y, int _cap, int _cost = 0) :
		x(_x), y(_y), cap(_cap), cost(_cost) {}
};

class network_flow
{
private:
	int V;
	vector<vector<int> > adj;
	vector<edge> edges;
	
public:
	network_flow(int V);
	void add_edge(int x, int y, int cap, int cost = 0);
	int max_flow(int source, int sink);
	pair<int, int> min_cost_flow(int source, int sink);
};

network_flow::network_flow(int V)
{
	this->V = V;
	adj.resize(V);
}

void network_flow::add_edge(int x, int y, int cap, int cost)
{
	adj[x].pb(edges.size());
	edges.pb(edge(x, y, cap, cost));
	
	adj[y].pb(edges.size());
	edges.pb(edge(y, x, 0, -cost));
}

int network_flow::max_flow(int source, int sink)
{
	vector<int> par(V), dist(V), pot(V);
	
	int flow = 0;
	while (true)
	{
		queue<int> q;
		REP(u, V)
			par[u] = -1;
		q.push(source);
		while (!q.empty() && par[sink] == -1)
		{
			int u = q.front();
			q.pop();
			FOREACH(i, adj[u])
			{
				int e = *i;
				int v = edges[e].y, cap = edges[e].cap;
				if (par[v] == -1 && cap > 0)
				{
					q.push(v);
					par[v] = e;
				}
			}
		}
		
		if (par[sink] == -1)
			break;
		
		int bot = INT_MAX;
		for (int u = sink; u != source; u = edges[par[u]].x)
			bot = min(bot, edges[par[u]].cap);
		for (int u = sink; u != source; u = edges[par[u]].x)
		{
			edges[par[u]].cap -= bot;
			edges[par[u]^1].cap += bot;
		}
		flow += bot;
	}
	return flow;
}

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

int main()
{
	scanf("%d", &T);
	REP(tc, T)
	{
		scanf("%d %d %d", &W, &H, &B);
		RESET(occ, false);
		REP(i, B)
		{
			int x0, y0, x1, y1;
			scanf("%d %d %d %d", &x0, &y0, &x1, &y1);
			FOR(x, x0, x1) FOR(y, y0, y1)
				occ[x][y] = true;
		}
		
		network_flow nf(2 * W * H + 2);
		
		REP(x, W) REP(y, H) if (!occ[x][y])
		{
			REP(i, 4)
			{
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || nx >= W || ny < 0 || ny >= H)
					continue;
				if (occ[nx][ny])
					continue;
				
				nf.add_edge(out(id(x, y)), in(id(nx, ny)), 1);
			}
			
			nf.add_edge(in(id(x, y)), out(id(x, y)), 1);
			
			if (y == 0)
				nf.add_edge(2*W*H, in(id(x, y)), 1);
			if (y == H-1)
				nf.add_edge(out(id(x, y)), 2*W*H+1, 1);
		}
		
		printf("Case #%d: %d\n", tc+1, nf.max_flow(2*W*H, 2*W*H+1));
		fflush(stdout);
	}
}
