#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cstdlib>
#include <cmath>
#include <cstring>
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

const double eps = 1e-10;
const int INF = 0x3f3f3f3f;
const int LEN = 110;
vector<pdd> lar, sam;
double V, T;
double ts, vs, tl, vl;
int n;

void solve() {
	vl = tl = vs = ts = 0;
	for(int i=0; i<lar.size(); i++) {
		vl += lar[i].first;
		tl += lar[i].first * lar[i].second;
	}
	if(vl > eps) tl /= vl;
	for(int i=0; i<sam.size(); i++) {
		vs += sam[i].first;
		ts += sam[i].first * sam[i].second;
	}
	if(vs > eps) ts /= vs;
}

double J(double val) {
	return ((val*ts)+((V-val)*tl))/V;
}

double calc() {
	double v0 = (T*V-V*tl)/(ts-tl);
	double v1 = (T*V-V*ts)/(tl-ts);
	double ret = max(v0 / vs, v1 / vl);
	return ret;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("outB.txt", "w", stdout);

	int TT, kase = 1;
	double tv, tt;
	cin >> TT;
	while(TT --) {
		sam.clear();
		lar.clear();
		scanf("%d%lf%lf", &n, &V, &T);
		int fg = 0;
		for(int i=0; i<n; i++) {
			scanf("%lf%lf", &tv, &tt);
			if(fg && fabs(tt - T) > eps) continue;
			if(fabs(tt - T) < eps && i == 1) {
				if(fg == 0){
					sam.clear(); lar.clear();
				}
			}
			if(fabs(tt - T) < eps) fg = 1;
			if(tt <= T + eps) sam.PB(MP(tv, tt));
			else lar.PB(MP(tv, tt));
		}
		solve();
	//	cout << vl << ' ' << tl << ' ' << vs << ' ' << ts << endl;
		cout << "Case #" << kase ++ << ": ";
		if(vl < eps){
			if(fabs(ts - T) < eps) printf("%.8lf\n", V/vs);
			else cout << "IMPOSSIBLE" << endl;
		}else if(vs < eps) {
			cout << "IMPOSSIBLE" << endl;
		}else {
			double ans = calc();
			printf("%.10lf\n", ans);
		}
	}
	return 0;
}
