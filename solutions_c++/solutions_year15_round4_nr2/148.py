#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <limits>
#include <ctime>
#include <cassert>
#include <map>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <stack>
#include <queue>
#include <numeric>
#include <iterator>
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> Pii;
typedef pair<ll, ll> Pll;

#define FOR(i,n) for(int i = 0; i < (n); i++)
#define sz(c) ((int)(c).size())
#define ten(x) ((int)1e##x)

#pragma comment(linker,"/STACK:36777216")

template<class T> void chmax(T& l, const T r){ l = max(l, r); }
template<class T> void chmin(T& l, const T r){ l = min(l, r); }

const double EPS = 1e-8;

typedef pair<double, double> Pdd;

double solve(){
	int n; double v, x; cin >> n >> v >> x;
	map<double, double> base;
	FOR(i, n){
		double nv, nx; cin >> nv >> nx;
		base[nx] += nv;
	}
	vector<Pdd> vd;
	for (auto& kv : base) {
		vd.emplace_back(kv.second , kv.first);
	}
	n = sz(vd);
	int lower = 0, upper = 0;
	FOR(i, n){
		if (vd[i].second < x + EPS) lower++;
		if (vd[i].second > x - EPS) upper++;
	}
	if (lower == 0 || upper == 0) return -1;
	sort(vd.begin(), vd.end(), [](const Pdd& l, const Pdd& r) {
		return l.second < r.second;
	});

	//if (n == 1) {
	//	return v / vd[0].first;
	//}
	//if (n == 2) {
	//	if (abs(vd[1].second - vd[0].second) < EPS) {
	//		return max(v / vd[0].first, v / vd[1].first);
	//	}
	//	double t = (vd[1].second - x) / (vd[1].second - vd[0].second);
	//	double v0 = t * v;
	//	double v1 = v - v0;
	//	double ans = max(v0 / vd[0].first, v1 / vd[1].first);
	//	return ans;
	//}

	double vx = v * x;
	double l = 0, r = 1e11;
	FOR(i, 100){
		double md = (l + r) / 2;

		double low_tmp = 0,rem = v;
		FOR(i, n){
			double use = min(rem, vd[i].first * md);
			rem -= use;
			low_tmp += use * vd[i].second;
		}
		if (rem > EPS) {
			l = md;
			continue;
		}

		double high_tmp = 0;
		rem = v;
		for (int i = n - 1; i >= 0; i--) {
			double use = min(rem, vd[i].first * md);
			rem -= use;
			high_tmp += use * vd[i].second;
		}

		if (low_tmp <= vx && vx <= high_tmp) {
			r = md;
		} else {
			l = md;
		}
	}

	return l;
}

int main(){
	int t; cin >> t;
	FOR(i, t){
		printf("Case #%d: ", i + 1);
		double ans = solve();
		if (ans < -EPS) {
			puts("IMPOSSIBLE");
		} else {
			printf("%.15lf\n", ans);
		}
	}

	return 0;
}
