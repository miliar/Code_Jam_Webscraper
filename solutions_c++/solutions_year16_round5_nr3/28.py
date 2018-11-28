#include <bits/stdc++.h>
using namespace std;

bool debug = false;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<pii> vpii;
typedef map<string, int> msi;
typedef set<string> ss;
typedef set<pii> spii;

const double pi = 2.0*acos(0.0);

int CASES;

void init() {
	assert(scanf("%d", &CASES) == 1);
}

int dprintf(const char *err, ...) { 
	if (debug) {
		va_list pvar;
		va_start(pvar, err);
		return vfprintf(stderr, err, pvar);
	}
	return 0;
}

struct point {
	double x, y, z;
	point(double x=0, double y=0, double z=0): x(x), y(y), z(z) {}
	point operator-(const point &p) { return point(x-p.x, y-p.y, z-p.z); }
	double dot(point p) { return x*p.x + y*p.y + z*p.z; }
	double dist2() { return dot(*this); }
};

struct Ast {
	point P, V;
	Ast(point P=point(), point V=point()): P(P), V(V) {}
	Ast operator-(const Ast &a) {
		return Ast(P-a.P, V-a.V);
	}
};

const double oo = 1e50;
const double eps = 1e-10;

int N, S;
Ast ast[2000];

bool poss(double maxd) {
	//	debug = true;
	//	debug = fabs(maxd-2.1875) < eps;
	dprintf("check poss %lf\n", maxd);
	double maxd2 = maxd*maxd;
	pdd reach[1100][1100];
	vector<pdd> good[1100];
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < i; ++j) {
			reach[i][j] = pdd(1, 0);
			Ast Q = ast[i]-ast[j];
			double A = Q.V.dist2();
			double B = 2*Q.P.dot(Q.V);
			double C = Q.P.dist2() - maxd2;
			dprintf("reach %d %d: %lf %lf %lf, %lf %lf %lf\n",
					i, j,
					Q.P.x, Q.P.y, Q.P.z,
					Q.V.x, Q.V.y, Q.V.z);
			dprintf("reach %d %d: A %lf B %lf C %lf\n",
					i, j, A, B, C);
			if (fabs(A) < eps) {
				if (C < eps)
					reach[i][j] = pdd(-oo, oo);
			} else {
				double disc = B*B-4*A*C;
				if (disc > -eps) {
					if (disc < eps)
						reach[i][j] = pdd(-B/(2*A)-eps, -B/(2*A)+eps);
					else {
						reach[i][j] = pdd((-B-sqrt(disc))/(2*A), (-B+sqrt(disc))/(2*A));
					}
				}
			}
			if (reach[i][j].first < 0) reach[i][j].first = 0;
			reach[j][i] = reach[i][j];
			dprintf("reach %d %d = (%lf %lf)\n", i, j, reach[i][j].first, reach[i][j].second);
		}
	}

	double dist[1010][1010];

	for (int i = 0; i < N; ++i) {
		vector<pdd> g;
		for (int j = 0; j < N; ++j) {
			if (i != j && reach[i][j].first <= reach[i][j].second) 
				g.push_back(reach[i][j]);
		}
		if (i == 0) g.push_back(pdd(-1, 0));
		sort(g.begin(), g.end());
		if (!g.empty()) {
			good[i].push_back(pdd(g.front().first, g.front().second+S));
			for (size_t k = 0; k < g.size(); ++k) {
				if (g[k].first < good[i].back().second) {
					good[i].back().second = max(good[i].back().second, g[k].second+S);
				} else {
					good[i].push_back(pdd(g[k].first, g[k].second+S));
				}
			}
		}
		for (size_t k = 0; k < good[i].size(); ++k) {
			dprintf("good %d: (%lf %lf)\n", i, good[i][k].first, good[i][k].second);
			dist[i][k] = oo;
		}
	}

	if (good[0].empty() || good[0].front().first > 0) return false;

	dist[0][0] = 0;
	set<pair<double, pii>> Q;
	Q.insert(make_pair(0, pii(0, 0)));
	while (!Q.empty()) {
		double t = Q.begin()->first;
		int u = Q.begin()->second.first;
		const auto &Phase = good[u][Q.begin()->second.second];
		dprintf("vis %d %lf\n", u, t);
		Q.erase(Q.begin());
		
		if (u == 1) return true;
		for (int v = 0; v < N; ++v) {
			if (v == u) continue;
			const auto &R = reach[u][v];
			if (R.second < R.first || R.first > Phase.second || R.second < t) continue;
			double nt = max(R.first, t);
			dprintf("may lead to %d nt %lf\n", v, nt);
			for (int k = 0; k < good[v].size(); ++k) {
				if (good[v][k].first <= nt && good[v][k].second >= nt) {
					if (nt < dist[v][k]) {
						Q.erase(make_pair(dist[v][k], pii(v, k)));
						Q.insert(make_pair(dist[v][k]=nt, pii(v, k)));
					}
					break;
				}
			}
		}
	}
	return false;
	
}

void solve(int P) {
	scanf("%d%d", &N, &S);
	for (int i = 0; i < N; ++i) {
		scanf("%lf%lf%lf%lf%lf%lf",
			  &ast[i].P.x, 
			  &ast[i].P.y,
			  &ast[i].P.z, 
			  &ast[i].V.x, 
			  &ast[i].V.y,
			  &ast[i].V.z);
	}
	double lo = 0, hi = sqrt((ast[0]-ast[1]).P.dist2())+eps;
	while (hi-lo > 1e-9) {
		double m = (lo+hi)/2;
		(poss(m) ? hi : lo) = m;
	}
	printf("Case #%d: %.9lf\n", P, hi);
}

int main(void) {
	init();
	for (int i = 1; i <= CASES; ++i) {
		solve(i);
		fflush(stdout);
		fflush(stderr);
	}
	return 0;
}
