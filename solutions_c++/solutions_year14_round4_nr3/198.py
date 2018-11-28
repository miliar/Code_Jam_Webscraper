#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

struct DinicFlow{
	struct Edge{
		Edge(int _to,int _cap,int _next) : to(_to), cap(_cap), next(_next) {};
		int to,cap,next;
	};
	int n,s,t,fl;
	vector <int> first,d,q,ptr;
	vector <bool> used;
	vector <Edge> a;
	DinicFlow(int _n,int _s,int _t) : n(_n), s(_s), t(_t) {
		first.resize(n,-1);
	};
	void addEdge(int u,int v,int cap,bool oriented = true) {
		a.push_back(Edge(v,cap,first[u])); first[u]=a.size()-1;
		a.push_back(Edge(u,oriented ? 0 : cap,first[v])); first[v]=a.size()-1;
	}
	bool bfs() {
		d.clear(); d.resize(n,-1);
		d[s]=0; q.clear(); q.push_back(s);
		for(int i=0;i<q.size();++i) {
			int v=q[i];
			for(int e=first[v];e!=-1;e=a[e].next) {
				int u=a[e].to;
				if (d[u]==-1&&a[e].cap) {
					d[u]=d[v]+1;
					q.push_back(u);
				}
			}
		}
		return d[t]!=-1;
	}
	int dfs(int v,int push = 1000000000) {
		if (v==t||push<=0) {
			fl+=push;
			return push;
		}
		int pushed=0;
		for(int e=ptr[v];e!=-1;e=a[e].next) {
			int u=a[e].to; ptr[v]=a[e].next;
			if (d[v]+1==d[u]) {
				if (int val=dfs(u,min(push-pushed,a[e].cap))) {
					pushed+=val;
					a[e].cap-=val;
					a[e^1].cap+=val;
				}
			}
		}
		return pushed;
	}
	int flow() {
		fl=0;
		while(bfs()) {
			ptr=first;
			dfs(s);
		}
		return fl;
	}
};

bool f[505][105];

void doTest() {
  int w, h, b;
  scanf("%d%d%d", &w, &h, &b);
  memset(f, 0, sizeof(f));
  for (int i = 0; i < b; ++i) {
    int x0, y0, x1, y1;
    scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
    if (y1 < y0) swap(y0, y1);
    if (x1 < x0) swap(x0, x1);
    for (int y = y0; y <= y1; ++y) {
      for (int x = x0; x <= x1; ++x) {
        f[y][x] = true;
      }
    }
  }
  int s = 0, t = 2 * w * h + 1;
  DinicFlow flow(2 * w * h + 2, s, t);
  for (int i = 0; i < w; ++i) {
    if (f[0][i] == 0)
      flow.addEdge(s, 1 + i, 1, 1);
    if (f[h - 1][i] == 0)
      flow.addEdge(w * (h - 1) + i + 1 + w * h, t, 1, 1);
  }

  for (int i = 0; i < h; ++i)
    for (int j = 0; j < w; ++j)
      if (f[i][j] == 0)
        flow.addEdge(i * w + j + 1, i * w + j + 1 + w * h, 1, 1);

  int dx[] = {-1, 0, 0, 1},
      dy[] = {0, -1, 1, 0};

  for (int i = 0; i < h; ++i) {
    for (int j = 0; j < w; ++j) {
      if (f[i][j] == 0) {
        for (int t = 0; t < 4; ++t) {
          int ni = i + dx[t], nj = j + dy[t];
          if (ni >= 0 && ni < h && nj >= 0 && nj < w && f[ni][nj] == 0) {
            flow.addEdge(i * w + j + 1 + w * h, ni * w + nj + 1, 1, 1);
          }
        }
      }
    }
  }

  printf("%d\n", flow.flow());
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    doTest();
  }
  return 0;
}