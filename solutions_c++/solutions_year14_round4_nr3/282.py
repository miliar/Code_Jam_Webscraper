#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cmath>
#include <ctime>

using namespace std;
FILE* in; FILE* out;

// Dinitz Algorithm

const int MAX_NODES = 16777216;
const int MAX_EDGES = 67108864;
const int INF = 1000000001;

struct Edge
{
	int next, to, cap;
	Edge(int next_ = 0, int to_ = 0, int cap_ = 0)
		{next = next_; to = to_; cap = cap_;}
};

int source, sink;
Edge edges[MAX_EDGES]; int numEdges;
int vis[MAX_NODES], dist[MAX_NODES], first[MAX_NODES];

int recurse(int node, int flow)
{
	if (node == sink) return flow;
	for (int idx = first[node]; idx != -1; idx = edges[idx].next)
	{
		if (!vis[edges[idx].to] && edges[idx].cap > 0 && dist[node] == dist[edges[idx].to] + 1)
		{
			int ret = recurse(edges[idx].to, min(flow, edges[idx].cap));
			if (ret) {edges[idx].cap -= ret; edges[idx ^ 1].cap += ret; return ret;}
		}
	}
	vis[node] = 1;
	return 0;
}

int dinitz(int source_, int sink_)
{
	source = source_; sink = sink_;
	
	int flow = 0;
	while (1)
	{
		// BFS
		int cur = 0;
		queue <int> q;

		for (int i=0; i<MAX_NODES; i++) dist[i] = MAX_NODES;
		q.push(sink); dist[sink] = 0;
		
		while (!q.empty())
		{
			cur = q.front(); q.pop();
			for (int idx = first[cur]; idx != -1; idx = edges[idx].next)
			{
				if (edges[idx ^ 1].cap > 0 && dist[edges[idx].to] == MAX_NODES)
				{
					dist[edges[idx].to] = dist[cur] + 1;
					q.push(edges[idx].to);
					if (edges[idx].to == source) {cur = source; break;}
				}
			}
			if (cur == source) break;
		}
		if (cur != source) break;
		
		// DFS
		int flag = 0;
		memset(vis, 0, sizeof(vis));
		while(1)
		{
			int add = recurse(source, INF);
			if (add == 0) break;
			flow += add; flag = 1;
		}
		if (!flag) break;
	}
	return flow;
}

inline void addEdge(int from, int to, int cap)
{
	if (!numEdges) memset(first, -1, sizeof(first));
	edges[numEdges].to = to; edges[numEdges].cap = cap;
	edges[numEdges].next = first[from]; first[from] = numEdges++;
	
	edges[numEdges].to = from; edges[numEdges].cap = 0;
	edges[numEdges].next = first[to]; first[to] = numEdges++;
}

// End of Dinitz Algorithm

const int MAX = 4096;

struct Point {
    int row, col;
};

int n, m, k;
bool a[MAX][MAX];
vector < pair <Point, Point> > houses;
int dir[4][2] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };

int eval() {
    for (int i = 0; i < (int)houses.size(); i++) {
        for (int row = houses[i].first.row; row <= houses[i].second.row; row++) {
            for (int col = houses[i].first.col; col <= houses[i].second.col; col++) {
                a[row][col] = false;
            }
        }
    }
    
    numEdges = 0;
    int source = n * m * 2 + 0;
    int sink = n * m * 2 + 1;
    for (int i = 0; i < n; i++) {
        addEdge(source, i * m + 0, 1);
        addEdge(n * m + i * m + m - 1, sink, 1);
    }
    for (int row = 0; row < n; row++) {
        for (int col = 0; col < m; col++) {
            addEdge(row * m + col, n * m + row * m + col, 1);
            if (a[row][col]) {
                for (int i = 0; i < 4; i++) {
                    int nrow = row + dir[i][0]; if (nrow < 0 || nrow >= n) continue;
                    int ncol = col + dir[i][1]; if (ncol < 0 || ncol >= m) continue;
                    if (a[nrow][ncol]) {
                        addEdge(n * m + row * m + col, nrow * m + ncol, 1);
                    }
                }
            }
        }
    }
    return dinitz(source, sink);
}

void solveTest(int test) {
    houses.clear();
    fscanf(in, "%d %d %d", &n, &m, &k);
    for (int i = 0; i < k; i++) {
        Point p1, p2;
        fscanf(in, "%d %d %d %d", &p1.row, &p1.col, &p2.row, &p2.col);
        houses.push_back(make_pair(p1, p2));
    }
    for (int i = 0; i < MAX; i++)
        for (int c = 0; c < MAX; c++)
            a[i][c] = false;
    for (int i = 0; i < n; i++)
        for (int c = 0; c < m; c++)
            a[i][c] = true;
    
    fprintf(out, "%d\n", eval());
}

int main(void) {
	unsigned sTime = clock();
	in = fopen("DontBreakTheNile.in", "rt");
	out = fopen("DontBreakTheNile.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++) {
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		solveTest(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n",
        (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	return 0;
}
