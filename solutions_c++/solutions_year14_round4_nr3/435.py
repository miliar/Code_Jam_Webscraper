#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>
#include <set>
#include <utility>

#define ALL(v) v.begin(), v.end()

using namespace std;
typedef long long ll;

template< typename T > T next() {  T tmp; cin >> tmp; return tmp; }
int w, h;

bool in(int x, int l, int r) {
	return l <= x && x <= r;
}
typedef map< int, int > :: iterator mit;

vector< mit > ptr;
vector< map<int, int> > flow;
vector< map<int, int> > cap;
vector< vector< int > > edges;
vector< int > queue;
vector< int > d;
int S;
int T;
int V;


const int INF = 1000000000;

bool bfs() {
	int head = 0;
	int tail = 0;	
	queue[tail++] = S;
	fill(d.begin(), d.end(), -1);
	d[S] = 0;
	while (head < tail) {
		int v = queue[head++];
		for (mit it = cap[v].begin(); it != cap[v].end(); ++it) {
			//cerr << v << " " << it -> first << "\n"; cerr.flush();
			int to = it -> first;
			if (d[to] == -1 && flow[v][to] < cap[v][to]) {
				queue[tail++] = to;
				d[to] = d[v] + 1;
			}
		}
	}
	return d[T] != -1;
}

int dfs (int v, int flw) {
	if (!flw)  	return 0;
	if (v == T)  	return flw;
	for (; ptr[v] != cap[v].end(); ++ptr[v]) {
		int to = ptr[v] -> first;
		if (d[to] != d[v] + 1)  continue;
		int pushed = dfs(to, min(flw, cap[v][to] - flow[v][to]));
		if (pushed) {
			flow[v][to] += pushed;
			flow[to][v] -= pushed;
			return pushed;
		}
	}
	return 0;
}

int dinic() {
	int flow = 0;
	while (true) {
		//cerr << "Iter\n"; cerr.flush();
		if (!bfs())  {
		//	cerr << "Break\n"; cerr.flush();
			break;
		}
		ptr.clear();
		for (int i = 0; i < V; ++i) {
			ptr.push_back(cap[i].begin());			
		}		
		while (int pushed = dfs(S, INF)) {
			flow += pushed;
		}			
	}
	return flow;
}

void solve() {
	w = next< int >();
	h = next< int >();
	vector< vector< int > > f(w, vector< int >(h, 0));

	int b = next< int >();
	for (int i = 0; i < b; ++i) {
		int x0 = next< int >();
		int y0 = next< int >();
		int x1 = next< int >();
		int y1 = next< int >();
		for (int dx = x0; dx <= x1; ++dx) {
			for (int dy = y0; dy <= y1; ++dy) {
				f[dx][dy] = 1;
			}
		}
	}
	V = 2 * w * h + 2;
	flow = std::vector< std::map<int, int > >(V);
	cap = std::vector< std::map<int, int > >(V);
	edges = std::vector< std::vector< int > >(V);
	queue = std::vector< int >(2 * V);
	d = std::vector< int >(V);
	S = V - 1;
	T = V - 2;

	for (int i = 0; i < w; ++i) {
		for (int j = 0; j < h; ++j) {
			if (j < h - 1 && f[i][j] == 0 && f[i][j + 1] == 0) {
				int u = i * h + j;
				int v = i * h + j + 1;			
				cap[2 * u + 1][2 * v] = 1;
				cap[2 * v][2 * u + 1] = 0;
				cap[2 * v + 1][2 * u] = 1;
				cap[2 * u][2 * v + 1] = 0;
			}
			if (i < w - 1 && f[i][j] == 0 && f[i + 1][j] == 0) {
				int u = i * h + j;
				int v = (i + 1) * h + j;			
				cap[2 * u + 1][2 * v] = 1;
				cap[2 * v][2 * u + 1] = 0;
				cap[2 * v + 1][2 * u] = 1;
				cap[2 * u][2 * v + 1] = 0;
			}
			int w = i * h + j;
			cap[2 * w][2 * w + 1] = 1;
			cap[2 * w + 1][2 * w] = 0;
		}
	}
	for (int i = 0; i < w; ++i) {
		cap[S][2 * i * h] = 1;
		cap[2 * i * h][S] = 0;

		cap[2 * (i * h + h - 1) + 1][T] = 1;
		cap[T][2 * (i * h + h - 1) + 1] = 0;
	}

	for (int i = 0; i < V; ++i) {

	}

	cout << dinic() << endl;
}

int main() {

//  freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);

  int test = next< int >();
  for (int i = 1; i <= test; ++i) {
  	cerr << i << endl; cerr.flush();
    printf("Case #%d: ", i);
    solve();
  }

  return 0;
}

 