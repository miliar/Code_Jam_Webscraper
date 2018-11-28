#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
#include <sstream>
#include <string>
#include <iostream>

using namespace std;

const int maxn = 8111;
const int inf = 10000;

#define PB push_back

char buf[20005];
map<string, int> g;
int n;
vector< vector<int> > alp;

struct network {
	struct edge {
		int to, cap, next;

		edge() {}

		edge(int a, int b, int c) : to(a), cap(b), next(c) {}
	};

	int dis[maxn], vh[maxn], G[maxn];
	vector<edge> E;

	int S, T, N, flow;

	network() {}
	void reset(int n, int s, int t) {
		N = n, S = s, T = t, flow = 0;
		memset(G, -1, sizeof(G));
		E.clear();
	}

	void add(int st, int ed, int x) {
//printf("%d, %d->%d\n", st, ed, x);
		int tot = (int) E.size();
		E.PB(edge(ed, x, G[st])); G[st] = tot;
		E.PB(edge(st, 0, G[ed])); G[ed] = tot + 1;
	}

	int aug(int u, int c) {
		//cout << u << ' ' << dis[u] << ' ' << c << endl;

		int his = c, mind = N;

		if (u == T) return c;

		for (int i = G[u]; i != -1; i = E[i].next) {
			int v = E[i].to, x = E[i].cap;

			if (!x) continue;
			mind = min(mind, dis[v]);
			if (dis[v] + 1 != dis[u]) continue;

			int tmp = aug(v, min(x, c));
			E[i].cap -= tmp, E[i ^ 1].cap += tmp, c -= tmp;
			if (!c) return his;
		}

		if (c == his) {
			if (!(--vh[dis[u]])) dis[S] = N + 1;
			vh[dis[u] = (mind + 1)]++;
		}

		return his - c;
	}

	int work() {
		memset(dis, 0, sizeof(dis));
		memset(vh, 0, sizeof(vh)); vh[0] = N;
		while (dis[S] <= N) flow += aug(S, inf);

		return flow;
	}
} f;

inline int wrank(const string& x) {
	if (g.find(x) == g.end()) g[x] = ++n;
	return g[x];
}

void load() {
	gets(buf);

	stringstream ss(buf);
    string str;

    int k = (int)alp.size();
    alp.push_back(vector<int>());

    while (ss >> str) {
		alp[k].push_back(wrank(str));
    }
}

void work() {
	int N; g.clear(); alp.clear(); n = 0;

	scanf("%d", &N); gets(buf);
    for (int i = 0; i < N; ++i) load();
/*
	puts("");
    for (int i = 0; i < alp.size(); ++i) {
		for (int j = 0; j < alp[i].size(); ++j) printf("%d ", alp[i][j]);
		puts("");
    }
*/
	int S = 0, T = n + n + 1;
	f.reset(n + n + 2, S, T);
    for (size_t i = 0; i < alp[0].size(); ++i)
		f.add(S, alp[0][i], inf);
	for (size_t i = 0; i < alp[1].size(); ++i)
		f.add(alp[1][i] + n, T, inf);
	for (size_t i = 2; i < alp.size(); ++i)
		for (size_t j = 0; j < alp[i].size(); ++j)
			for (size_t k = 0; k < alp[i].size(); ++k)
				if (alp[i][j] != alp[i][k])
					f.add(n + alp[i][j], alp[i][k], inf);
	for (int i = 1; i <= n; ++i) f.add(i, i + n, 1);

	printf("%d\n", f.work());
}

int main() {
	int T; scanf("%d", &T);

	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		work();
	}

	return 0;
}
