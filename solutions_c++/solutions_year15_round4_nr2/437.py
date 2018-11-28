#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
using namespace std;
#define ll long long
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define VI vector<int>
#define all(s) (s).begin(),(s).end()
#define L(s) (int)(s).size()
#define inf 1000000000
#define pdd pair<double, double>


inline double fabs(double x) {
	return (x > 0) ? x : -x;
}
pdd a[111];
double V, T;
int n, t;
const double eps = 1e-8;
int main() {

	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for(int tc = 1; tc <= t; ++tc) {
		cin >> n >> V >> T;
		for(int i = 0; i < n; ++i) {
			cin >> a[i].y >> a[i].x;
		}
		sort(a, a + n);

		int m = 0;
		for(int i = 1; i < n; ++i) {
			if (fabs(a[i].x - a[m].x) < eps) {
				a[m].y += a[i].y;
			} else {
				++m;
				a[m] = a[i];
			}
		}
		n = m + 1;

		if (a[0].x > T + eps || a[n - 1].x < T - eps) {
			cout << "Case #" << tc << ": IMPOSSIBLE\n";
			continue;
		}

		if (fabs(a[0].x - T) < eps) {
			printf("Case #%d: %0.15f\n", tc, V / a[0].y);
			continue;
		}

		if (fabs(a[n - 1].x - T) < eps) {
			printf("Case #%d: %0.15f\n", tc, V / a[n - 1].y);
			continue;
		}

		double ans = 1e100;
		for(int st = 0; st < n; ++st) {
			if (a[st].x - T > eps) {
				double cur_v = a[st].y;
				double cur_t = a[st].x;

				double tot_time = 0;
				for(int i = st - 1; i >= 0; --i) {

					double mix_v = a[i].y;
					double mix_t = a[i].x;

					for(int j = i - 1; j >= 0; --j) {
						mix_t = (mix_v * mix_t + a[j].x * a[j].y) / (mix_v + a[j].y);
						mix_v += a[j].y;
					}

					double need = a[i].x;
					if (a[i].x < T) {
						need = T;
					}

					double req = (cur_v * need - cur_v * cur_t) / (mix_v * mix_t - mix_v * need);

					cur_t = (cur_v * cur_t + mix_v * mix_t * req) / (cur_v + mix_v * req);
					cur_v += mix_v * req;
					tot_time += req;

					if (fabs(cur_t - T) < eps) {
						break;
					}
				}
				tot_time = max(tot_time, 1.0);
				//cerr << st + 1 << " " << tot_time * V / cur_v << endl;
				ans = min(ans, tot_time * V / cur_v);
			}
		}
		printf("Case #%d: %0.15f\n", tc, ans);
	}
}

