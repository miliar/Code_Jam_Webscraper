/*
 * Problem : 
 * Author : Hwhitetooth
 * Date : 
 * Result :
 */

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int N = 100 + 10;
const double INF = 1E9;
const double EPS = 1E-14;

struct Water {
	double r, c;
} a[N];
int testCases, n;
double v, x;
double ans;

int cmp(Water a, Water b) {
	return a.c < b.c;
}

int check(long double limit) {
	long double maxV = 0;
	for (int i = 0; i < n; ++i) {
		maxV += limit * a[i].r;
	}
	if (maxV < v) {
		return 0;
	}
	long double low = 0, tmpV = 0;
	for (int i = 0; i < n; ++i) {
		if (tmpV + limit * a[i].r <= v) {
			low = (low * tmpV + a[i].c * limit * a[i].r) / (tmpV + limit * a[i].r);
			tmpV += limit * a[i].r;
		}
		else {
			double deltaV = v - tmpV;
			low = (low * tmpV + a[i].c * deltaV) / v;
			break;
		}
	}
	if (x < low - EPS) {
//		cerr << x << ' ' << low << endl;
		return 0;
	}
	long double high = 0;
	tmpV = 0;
	for (int i = n - 1; i >= 0; --i) {
		if (tmpV + limit * a[i].r <= v) {
			high = (high * tmpV + a[i].c * limit * a[i].r) / (tmpV + limit * a[i].r);
			tmpV += limit * a[i].r;
		}
		else {
			long double deltaV = v - tmpV;
			high = (high * tmpV + a[i].c * deltaV) / v;
			break;
		}
	}
	if (x > high + EPS) {
//		cerr << x << ' ' << high << endl;
		return 0;
	}
	return 1;
}

int main() {
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		scanf("%d%lf%lf", &n, &v, &x);
		for (int i = 0; i < n; ++i) {
			scanf("%lf%lf", &a[i].r, &a[i].c);
		}
		sort(a, a + n, cmp);
		if (x < a[0].c || x > a[n - 1].c) {
			printf("Case #%d: IMPOSSIBLE\n", _);
			continue;
		}
		long double l = 0, r = INF, m;
		for (int i = 0; i < 100; ++i) {
			m = (l + r) * 0.5;
			if (check(m)) {
				r = m;
			}
			else {
				l = m;
			}
		}
		printf("Case #%d: %.20f\n", _, (double)r);
	}
	return 0;
}