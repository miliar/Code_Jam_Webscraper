#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define pb push_back
#define mp make_pair

double tim(double v, double r) {
	return v / r;
}
int main() {
	int tc;
	cin >> tc;
	for (int t = 0; t < tc; t++) {
		int n;
		double v, x;
		// R C
		cin >> n >> v >> x;
		vector<pair<double, double>> vv(n);
		bool smaller = false, bigger = false;
		FOR(i, 0, n) {
			cin >> vv[i].first >> vv[i].second;
			if (vv[i].second >= x) bigger = true;
			if (vv[i].second <= x) smaller = true;
		}
		if (!smaller || !bigger) {
			printf("Case #%d: IMPOSSIBLE\n", t+1);
			continue;
		}
		if (n == 1) {
			if (x == vv[0].second) {
				printf("Case #%d: %.8f\n", t+1, tim(v, vv[0].first));
			} else {
				printf("Case #%d: IMPOSSIBLE\n", t+1);
			}
		} else {
			if (fabs(vv[1].second - vv[0].second)  <= 1e-8) {

				printf("Case #%d: %.8f\n", t+1, tim(v, vv[1].first + vv[0].first));
				continue;
			}
			double v1 = v * (x - vv[0].second) / (vv[1].second - vv[0].second);
			double v0 = v - v1;
			if (v1 < 0 || v1 > v || v0 < 0 || v0 > v) {
				printf("Case #%d: IMPOSSIBLE\n", t+1);
			} else {
//				std::cerr << "Using v1 = " << v1 << ", v0 = " << v0 << endl;
				printf("Case #%d: %.8f\n", t+1, max(tim(v1, vv[1].first), tim(v0, vv[0].first)));
			}
		}
	}
	return 0;
}
