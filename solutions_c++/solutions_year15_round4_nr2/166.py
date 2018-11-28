#include <cstdio>
#include <algorithm>
#include <vector>

#define FOR(a,b,c) for (int c = (a), _for = (b); c < _for; ++c)
#define REP(n) for (int _rep = 0, _for = (n); _rep < _for; ++_rep)
#define pb push_back
#define x first
#define y second
#define ll long long
#define pii pair < int, int >

using namespace std;

const double ep = 1e-9;

int n;
double v, x, k;
double r[105], c[105];

double F(vector < pair < double, double > > V){
	double R = 0;
	for (auto x : V) R += x.x * x.y;
	return R;
}

bool cmp(pair < double, double > a, pair < double, double > b){return a.y < b.y;}

double F2(vector < pair < double, double > > V, double limit){
	double R = 0;
	for (auto x : V){
		if (x.x * x.y < limit + ep){R += x.x, limit -= x.x * x.y; continue;}
		double t = limit / x.y;
		R += t;
		break;
	} return R;
}

void Solve(){
	scanf("%d%lf%lf", &n, &v, &x);
	FOR(0, n, i) scanf("%lf%lf", r + i, c + i);
	bool ch = true;
	FOR(0, n, i) if (c[i] - ep < x) ch = false;
	if (ch){printf("IMPOSSIBLE\n"); return;}
	ch = true;
	FOR(0, n, i) if (c[i] + ep > x) ch = false;
	if (ch){printf("IMPOSSIBLE\n"); return;}
	FOR(0, n, i) c[i] -= x;
	x = 0;
	vector < pair < double, double > > Vl, Ve, Vm;
	FOR(0, n, i){
		if (c[i] > ep) Vm.pb({r[i], c[i]});
		if (c[i] < -ep) Vl.pb({r[i], -c[i]});
		if (-ep < c[i] && c[i] < ep) Ve.pb({r[i], c[i]});
	}
	double MaxCap = min(F(Vl), F(Vm));
	sort(Vl.begin(), Vl.end(), cmp);
	sort(Vm.begin(), Vm.end(), cmp);
	double Sol = F2(Vl, MaxCap) + F2(Vm, MaxCap);
	for (auto x : Ve) Sol += x.x;
	printf("%.9lf\n", v / Sol);
}

int main(){
	int t;
	scanf("%d", &t);
	FOR(1, t + 1, i){
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}

