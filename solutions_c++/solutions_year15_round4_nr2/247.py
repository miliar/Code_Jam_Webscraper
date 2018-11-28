#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

const int N = 111;
const double eps = 1e-10;

int n;
double v, x;
pair<double, double> item[N];

bool solve(double time) {
	double lower = 0, upper = 0;
	double vol = 0;
	for (int i = 1; i <= n; i++) {
		if (item[i].second * time + vol < v) {
			double tmp = item[i].second * time;
			lower = (lower * vol + item[i].first * tmp) / (vol + tmp);
			vol += tmp;
		} else {
			lower = (lower * vol + item[i].first * (v - vol)) / v;
			vol = v;
		}
	}

	if (vol + eps < v) {
		return false;
	}

	vol = 0;
	for (int i = n; i >= 1; i--) {
		if (item[i].second * time + vol < v) {
			double tmp = item[i].second * time;
			upper = (upper * vol + item[i].first * tmp) / (vol + tmp);
			vol += tmp;
		} else {
			upper = (upper * vol + item[i].first * (v - vol)) / v;
			vol = v;
		}	
	}

	if (vol + eps < v) {
		return false;
	}

	if (lower <= x + eps && x <= upper + eps) {
		return true;
	} else {
		return false;
	}
}

int main() {
	int test;
	scanf("%d", &test);
	while (test--) {
		static int testCount = 0;
		printf("Case #%d: ", ++testCount);
		scanf("%d %lf %lf", &n, &v, &x);
		bool upper = false, lower = false;
		for (int i = 1; i <= n; i++) {
			scanf("%lf %lf", &item[i].second, &item[i].first);
			if (item[i].first > x - eps) {
				upper = true;
			}
			if (item[i].first < x + eps) {
				lower = true;
			}
		}
		sort(item + 1, item + n + 1);
		if (!lower || !upper) {
			puts("IMPOSSIBLE");
		} else {
			double l = 0, r = 1e10;
			for (int i = 0; i < 200; i++) {
				double mid = (l + r) / 2;
				if (solve(mid)) {
					r = mid;
				} else {
					l = mid;
				}
			}
			//if (l >= 1e9 - eps) {
			//	puts("IMPOSSIBLE");
			//} else {
				printf("%.10f\n", (double)l);
			//}
		}
	}
	return 0;
}