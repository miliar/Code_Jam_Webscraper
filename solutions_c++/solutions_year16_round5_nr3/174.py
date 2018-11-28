#include <bits/stdc++.h>

using namespace std;

const int maxn = 1010;

int T, N, S;
double x[maxn], y[maxn], z[maxn];
double vx[maxn], vy[maxn], vz[maxn];
int fa[maxn];

struct Edge {
	int u, v;
	double d;
	Edge() {}
	Edge(int _u, int _v, double _d) { u = _u, v = _v, d = _d; }
	bool operator < (const Edge &e) const {
		return d < e.d;
	}
};

int t;
Edge e[maxn*maxn];

double sqr(double x) { return x*x; }

int find(int x) { return x == fa[x] ? x : fa[x] = find(fa[x]); }

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C.out", "w", stdout);
	scanf("%d", &T);
	for(int cas = 1; cas <= T; cas ++) {
		scanf("%d%d", &N, &S);
		for(int i = 0; i < N; i ++) {
			scanf("%lf%lf%lf%lf%lf%lf", &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
			fa[i] = i;
		}
		t = 0;
		for(int i = 0; i < N; i ++) for(int j = 0; j < N; j ++) if(i != j) {
			e[t ++] = Edge(i, j, sqrt(sqr(x[i]-x[j]) + sqr(y[i]-y[j]) + sqr(z[i]-z[j])));
		}
		sort(e, e+t);
		
		double res = 0;
		for(int i = 0; i < t; i ++) {
			int u = find(e[i].u), v = find(e[i].v);
			fa[u] = v;
			if(find(0) == find(1)) {
				res = e[i].d;
				break;
			}
		}
		printf("Case #%d: %.10f\n", cas, res);
	}
	return 0;
}
