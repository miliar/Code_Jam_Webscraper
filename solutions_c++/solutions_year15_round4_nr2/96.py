#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>
#include <bitset>
#include <cmath>

using namespace std;

const long double eps = 1e-16;

long double get_temp(vector <pair<long double, long double> >& a, long double v, long double key) {
	long double sum = 0;
	long double have = 0;
	bool good = false;
	for (int i = 0; i < a.size(); ++i) {
		long double need = v - have;
		if (a[i].second * key < need) {
			sum += a[i].second * a[i].first * key;
			have += a[i].second * key;
		} else {
			sum += need * a[i].first;
			have += need;
			good = true;
			break;
		}
	}
	if (!good) return -1.;
	return sum / v;
}

void solve(int tcase) {
	printf("Case #%d: ", tcase);
	int n;
	scanf("%d", &n);

	long double v, x;
	vector <pair<long double, long double> > cur;
	double vv, xx;
	cin >> vv >> xx;
	v = vv, x = xx;
	long double mn = 10000;
	long double mx = -1;
	for (int i = 0; i < n; ++i) {
		double ca, cb;
		cin >> ca >> cb;
		long double a = ca, b = cb;
		cur.push_back(make_pair(b, a));
		mn = min(mn, b);
		mx = max(mx, b);
	}

	if (mx < x || mn > x) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}

	vector <pair<long double, long double> > cur2;
	sort(cur.begin(), cur.end());
	cur2 = cur;
	reverse(cur2.begin(), cur2.end());

	long double l = 0, r = 1e8;
	//double l = 0, r = 1999998.0926513672;

	for (int i = 0; i < 200; ++i) {
		long double key = (l + r) / 2;
		long double mxtemp = get_temp(cur2, v, key);
		long double mntemp = get_temp(cur, v, key);
		//printf("%.10lf %.10lf\n", (double)l, (double)r);
		//cerr << mxtemp << " " << mntemp << endl;

		if (mxtemp > x - eps && mntemp < x + eps) {
			r = key;
		} else {
			l = key;
		}
	}
	printf("%.10lf\n", (double)((l + r) / 2.));
}

void solve2(int tcase) {
	printf("Case #%d: ", tcase);
	int n;
	scanf("%d", &n);

	double v, x;
	vector <pair<double, double> > cur;
	cin >> v >> x;
	double mn = 10000;
	double mx = -1;
	for (int i = 0; i < n; ++i) {
		double a, b;
		cin >> a >> b;
		cur.push_back(make_pair(b, a));
		mn = min(mn, b);
		mx = max(mx, b);
	}

	if (mx < x - eps || mn > x + eps) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}

	if (n == 1) {
		double R = cur[0].second, C = cur[0].first;
		if (fabs(C - x) > eps) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			printf("%.10lf\n", v / R);
		}
		return;
	}

	double R1 = cur[0].second, C1 = cur[0].first;
	double R2 = cur[1].second, C2 = cur[1].first;

	if (fabs(C1 - C2) < eps) {
		double vol = R1 + R2;
		if (fabs(C1 - x) < eps) {
			printf("%.10lf\n", v / vol);
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
		return;
	}

	double cyval = (x * v - v * C1) / (R2 * C2 - R2 * C1);
	double cxval = (v - cyval * R2) / R1;

	printf("%.10lf\n", max(cxval, cyval));
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("corr2.txt", "w", stdout);

	int t;
	scanf("%d\n", &t);

	for (int i = 1; i <= t; ++i) {
		cerr << i << endl;
		solve(i);
	}


	return 0;
}

