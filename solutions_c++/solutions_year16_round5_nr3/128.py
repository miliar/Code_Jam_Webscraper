#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

const int N = 1000 + 10;
const long double INF = 1e10;
const int D = 50;

int n;
long double s;
long double x[N], y[N], z[N], vx[N], vy[N], vz[N];
long double mind[N][N], mint[N][N];
long double lastActive[N];
int deg[N];
int in[N];

struct Event
{
	long double t;
	int opt;
	int u, v;
	Event() {}
	Event(long double t, int opt, int u, int v) : t(t), opt(opt), u(u), v(v) {}
	int operator < (const Event& that) const {
		return t < that.t;
	}
};

vector<Event> vec;

long double sqr(long double x)
{
	return x * x;
}

long double calcDist(int u, int v, long double t)
{
	return sqrt(sqr((x[u] + vx[u] * t) - (x[v] + vx[v] * t)) 
	+ sqr((y[u] + vy[u] * t) - (y[v] + vy[v] * t)) 
	+ sqr((z[u] + vz[u] * t) - (z[v] + vz[v] * t)));
}

long double searchIt(long double l, long double r, int u, int v, long double x)
{
	long double fl = calcDist(u, v, l) - x;
	for(int i = 0; i < D; ++ i) {
		long double mid = (l + r) * 0.5;
		long double fmid = calcDist(u, v, mid) - x;
		if (fl * fmid > 0) {
			l = mid;
		} else {
			r = mid;
		}
	}
	return r;
}

void go(int u, long double t, long double lim)
{
	vector<int> que;
	que.push_back(u);
	for(int i = 0; i < que.size(); ++ i) {
		int u = que[i];
		for(int j = 0; j < n; ++ j) {
			if (in[j]) continue;
			if (calcDist(u, j, t) < lim) {
				in[j] = true;
				que.push_back(j);
			}
		}
	}
}

bool checkOk(double lim)
{
	vec.clear();
	for(int i = 0; i < n; ++ i) {
		for(int j = i + 1; j < n; ++ j) {
			if (mind[i][j] >= lim) continue;
			if (calcDist(i, j, INF) < lim) {
				vec.push_back(Event(0, 1, i, j));
			} else {
				if (calcDist(i, j, 0) >= lim) {
					vec.push_back(Event(searchIt(0, mint[i][j], i, j, lim), 1, i, j));
				} else {
					vec.push_back(Event(0, 1, i, j));
				}
				vec.push_back(Event(searchIt(mint[i][j], INF, i, j, lim), -1, i, j));
			}
		}
	}
	for(int i = 0; i < n; ++ i) {
		lastActive[i] = 0;
		deg[i] = 0;
		in[i] = false;
	}
	in[0] = true;
	sort(vec.begin(), vec.end());
	for(int i = 0; i < vec.size(); ++ i) {
		int u = vec[i].u, v = vec[i].v;
		if (vec[i].opt < 0) {
			if (--deg[u] == 0) lastActive[u] = vec[i].t;
			if (--deg[v] == 0) lastActive[v] = vec[i].t;
		} else {
			if (deg[u] == 0 && vec[i].t - lastActive[u] > s) in[u] = false;
			if (deg[v] == 0 && vec[i].t - lastActive[v] > s) in[v] = false;
			deg[u] ++; deg[v] ++;
			if (in[u] && ! in[v]) {
				go(v, vec[i].t, lim);
			}
			if (in[v] && ! in[u]) {
				in[u] = true;
				go(u, vec[i].t, lim);
			}
		}
		if (in[1]) return true;
	}
	return false;
}

void solve()
{
	cin >> n >> s;
	for(int i = 0; i < n; ++ i) {
		cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
	}
	for(int i = 0; i < n; ++ i) {
		for(int j = i + 1; j < n; ++ j) {
			long double l = 0, r = 1e5;
			for(int k = 0; k < D * 2; ++ k) {
				long double midl = l + (r - l) / 3;
				long double midr = midl + (r - l) / 3;
				long double fl = calcDist(i, j, midl), fr = calcDist(i, j, midr);
				if (fl < fr) {
					r = midr;
				} else {
					l = midl;
				}
			}
			mint[i][j] = r;
			mind[i][j] = calcDist(i, j, r);
		}
	}
	long double l = 0, r = 1e5;
	for(int i = 0; i < D; ++ i) {
		long double mid = (l + r) * 0.5;
		if (checkOk(mid)) {
			r = mid;
		} else {
			l = mid;
		}
	}
	printf("%.12f\n", (double)r);
}

int main()
{
	//freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	//freopen("C-small-attempt1.in", "r", stdin); freopen("C-small-attempt1.out", "w", stdout);
	//freopen("C-small-attempt2.in", "r", stdin); freopen("C-small-attempt2.out", "w", stdout);
	freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
		printf("Case #%d: ", i + 1);
		cerr << "Start: " << i << endl;
		solve();
	}
	return 0;
}
