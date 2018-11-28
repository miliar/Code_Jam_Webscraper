#include <iostream>
#include <cstdio>
#include <cstring>
#include <string.h>
#include <memory>
#include <map>
#include <queue>
#include <algorithm>
#include <string>
#include <stdlib.h>
#include "sstream"

using namespace std;

double eps = 1e-10;

string s;

int test, n, m;

struct node {
public:
	double r, c;
} a[10000];

bool cmp(struct node &a, struct node &b) {
	return a.c < b.c;
	
};

double v, x;

int cap(double x) {
	if (x < -eps) return -1;
	if (x > eps)return 1;
	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> test;
	for (int tt = 1; tt <= test; tt++) {
		scanf("%d%lf%lf", &n, &v, &x);
		double maxc = 0;
		for (int i = 0; i < n; i++) {
			scanf("%lf%lf", &a[i].r, &a[i].c);
		}
		sort(a, a + n, cmp);
		if (a[0].c > x || a[n-1].c < x) {
			printf("Case #%d: IMPOSSIBLE\n", tt);
		} else {
			double ll = 0, rr = v / a[n - 1].r + 0.1;
			if (v / a[0].r + 0.1 > rr) 
				rr = v / a[0].r + 0.1;
			// cout << ll << ' ' << rr << endl;
			while (ll + 1e-6 < rr) {

				double mid = (ll + rr) / 2;
				// printf("%.8lf, %.8lf, %.8lf\n", ll, rr, mid);
				double a1 = 0, a2 = 0;
				//chech low
				double s = 0;
				double s1 = 0;
				for (int i = 0; i < n; i++) {
					s1 = s;
					s += a[i].r * mid;
					if (cap(s - v) != -1) {
						a1 = (a1 * s1 + (v - s1) * a[i].c) / v;
						// printf("%.8lf\n", a1);
						break;
					}

					a1 = (a1 * s1 + mid * a[i].r * a[i].c) / s;
					// printf("%.8lf\n", a1);
				}
				// cout << s << endl;
				// printf("%.8lf\n", s);
				if (s < v) { ll = mid; continue; }
				//check high
				s = 0;
				s1 = 0;
				for (int i = n - 1; i >=0; i--) {
					s1 = s;
					s += a[i].r * mid;
					if (cap(s - v) != -1) {
						a2 = (a2 * s1 + (v - s1) * a[i].c) / v;
						break;
					}
					a2 = (a2 * s1  + mid * a[i].r * a[i].c) / s;
				}
				// printf("%.8lf\n", s);
				if (s < v) { ll = mid; continue; }
				// cout << a1 <<  ' ' << a2 << endl;
				// printf("%.8lf %.8lf %.8lf\n", a1, a2, x);
				if (cap(x - a1) != -1 && cap(x - a2) != 1) {
					rr = mid;
				} else { 
					ll = mid;
				}
			}
			printf("Case #%d: %.9lf\n", tt, rr);
		}
	}
}