#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std; 

#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

const int INF = 1<<29;
typedef long long ll;

inline int two(int n) { return 1 << n; }
inline int test(int n, int b) { return n & two(b); }
inline void set_bit(int & n, int b) { n |= two(b); }
inline void unset_bit(int & n, int b) { n &= ~two(b); }
inline int last_bit(int n) { return n & (-n); }
inline int ones(int n) { int res = 0; while(n && ++res) n-=n&(-n); return res; }

template<class T> void chmax(T & a, const T & b) { a = max(a, b); }
template<class T> void chmin(T & a, const T & b) { a = min(a, b); }
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

const int dx[] = {0,1,0,-1}, dy[] = {-1,0,1,0};
const int MAX = 1000;
int W, H, B;

inline int check(int x, int y) { return x >= 0 && x < W && y >= 0 && y < H; }

struct Rect
{
	int x1, y1, x2, y2;
} rects[100];

int board[MAX][MAX];

namespace Dinitz
{
	const int NODES = 2*100*500+7, EDGES = 5*NODES;

	struct Edge
	{
		Edge() { }
		Edge(int s, int d, int cap): source(s), dest(d), residue(cap) { }
		int source, dest, residue;
	};

	int N, M, source, dest;
	int adj[NODES+2*EDGES], work_adj[NODES+2*EDGES], work_edges[NODES+2*EDGES];
	Edge edges[NODES+2*EDGES];

	bool bfs()
	{
		static int dist[NODES], manage[NODES];
		for (int i = 0; i < N; ++i) 
		{
			work_adj[i] = -1;
			dist[i] = N+1;
		}
		int work_M  = 0;
		
		int size = 0;
		manage[size++] = source;
		dist[source] = 0;

		for (int step = 0; step < size && dist[manage[step]]+1 <= dist[dest]; ++step)
			for (int i = adj[manage[step]]; i >= 0; i = adj[i])
			{
				Edge & e = edges[i];
				if (e.residue > 0 && dist[e.source]+1 <= dist[e.dest])
				{
					work_adj[N+work_M] = work_adj[e.source];
					work_edges[N+work_M] = i;
					work_adj[e.source] = N+work_M++;

					if (dist[e.dest] == N+1)
					{
						dist[e.dest] = dist[e.source]+1;
						manage[size++] = e.dest;
					}
				}
			}
		return dist[dest] != N+1;
	}

	int dfs(int node, int fl)
	{
		if (!fl || node == dest) return fl;
		for (int & i = work_adj[node]; i >= 0; i = work_adj[i])
		{
			int ind = work_edges[i], temp;
			if (temp = dfs(edges[ind].dest, min(fl, edges[ind].residue)))
			{
				edges[ind].residue -= temp;
				edges[ind^1].residue += temp;
				return temp;
			}
		}
		return 0;
	}

	void Init(int _N)
	{
		N = _N;
		if (N&1) ++N;
		M = 0;
		for (int i = 0; i < N; ++i) adj[i] = -1;
	}

	void AddEdge(int source, int dest, int cap1, int cap2)
	{
		edges[N+M] = Edge(source, dest, cap1);
		adj[N+M] = adj[source];
		adj[source] = N+M++;

		edges[N+M] = Edge(dest, source, cap2);
		adj[N+M] = adj[dest];
		adj[dest] = N+M++;
	}

	int Flow(int _source, int _dest)
	{
		source = _source;
		dest = _dest;

		int flow = 0, temp;
		while (bfs())
		{
			while (temp = dfs(source, INF))
				flow += temp;
		}
		return flow;
	}
}

int index(int x, int y) { return x * H + y; }

void Solve(int tc)
{
	cin >> W >> H >> B;
	memset(board, 0, sizeof(board));
	REP(i, B)
	{
		cin >> rects[i].x1 >> rects[i].y1 >> rects[i].x2 >> rects[i].y2;
		FOR(x, rects[i].x1, rects[i].x2)
			FOR(y, rects[i].y1, rects[i].y2)
				board[x][y] = 1;
	}

	int N = W*H*2+2, source = N-2, sink = N-1;
	Dinitz::Init(N);
	REP(x, W) REP(y, H)
	{
		int ind1 = index(x, y);
		if (!board[x][y])
			Dinitz::AddEdge(2*ind1, 2*ind1+1, 1, 0);
		REP(d, 4)
		{
			int xx = x+dx[d], yy = y+dy[d];
			if (check(xx, yy))
			{
				int ind2 = index(xx, yy);
				Dinitz::AddEdge(2*ind1+1, 2*ind2, 1, 0);
			}
		}
		if (y == 0)
			Dinitz::AddEdge(source, 2*ind1, 1, 0);
		if (y == H-1)
			Dinitz::AddEdge(2*ind1+1, sink, 1, 0);
	}

	printf("Case #%d: %d\n", tc, Dinitz::Flow(source, sink));
}

int main()
{
	int T;
	scanf("%d\n", &T);
	FOR(tc,1,T) Solve(tc);

	return 0;
}