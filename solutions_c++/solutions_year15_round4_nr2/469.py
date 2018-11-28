#include <iostream>
#include <iomanip>

#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)
#include <algorithm>

using namespace std;

typedef pair<double, double> pdd;
const double eps = 1e-6;
#define R second
#define C first

double solve() {
	double v, x;
	pdd p[200];
	int n;
	cin >> n >> v >> x;
	REP(i, n) cin >> p[i].R >> p[i].C;
	double constant = 0;
	REP(i, n) {
		if (abs(p[i].C - x) < eps) {
			constant += p[i].R;
		}
	}
	if (constant > eps) {
		return v / constant;
	}
	sort(p, p+n);
	if (p[0].C > x == p[1].C > x) {
		return -1;
	}
	if (n == 1) return -1;
	auto d1 = abs(p[0].C - x);
	auto d2 = abs(p[1].C - x);
	auto s = d1 + d2;
	return max(d2 / s * v / p[0].R, d1 / s * v / p[1].R);
	return -1;
}

int main() {
	int t;
	cin >> t;
	REP(i, t) {
		cout << "Case #" << i + 1 << ": ";
		auto s = solve();
		if (s < -0.5) {
			cout << "IMPOSSIBLE";
		} else {
			cout << fixed  << setprecision(10) << s;
		}
		cout << endl;
	}
}