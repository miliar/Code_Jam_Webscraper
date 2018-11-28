#include <cstdio>
#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for (int i=int(a);i<=int(b);++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define PB push_back

struct point {
	double x, y, z;
} p[1010];

struct edge {
	int u, v;
	double w;
} e[1000010];

int fa[1010];

double distance(const point& p1, const point& p2) {
	return sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y) + (p1.z-p2.z)*(p1.z-p2.z));
}

int find(int v) {
	if (fa[v] == v) return v;
	return fa[v] = find(fa[v]);
}

bool merge(int u, int v) {
	int fu = find(u), fv = find(v);
	fa[fv] = fu;
	return (fu != fv);
}

bool edgeComp(edge& e1, edge& e2) {
	return e1.w < e2.w;
}

int main() {
	int tN;
	cin >> tN;
	FOR(cN, 1, tN) {
		int n, s;
		cin >> n >> s;
		REP(i, n) scanf("%lf%lf%lf%d%d%d", &p[i].x, &p[i].y, &p[i].z, &s, &s, &s);
		int m = 0;
		REP(i, n)
		FOR(j, i+1, n-1) {
			e[m].u = i;
			e[m].v = j;
			e[m].w = distance(p[i], p[j]);
			++m;
		}
		sort(e, e+m, edgeComp);
		// printf("m = %d\n", m);
		double ans = 0;
		int k = 0;
		REP(i, n) fa[i] = i;
		while (find(0) != find(1) && k < m) {
			ans = max(ans, e[k].w);
			merge(e[k].u, e[k].v);
			++k;
		}
		printf("Case #%d: %.6lf\n", cN, ans);
	}
}
