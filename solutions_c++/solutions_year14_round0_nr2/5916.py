#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif

#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#define INF 1000000007
#define EPS 0.000000001
using namespace std;

int T, t, i, k;
double c, f, x, res;

int main() {
//	freopen("gcj2.in", "r", stdin);
//	freopen("gcj2.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%lf %lf %lf", &c, &f, &x);
		k = floor(x / c - 2.0 / f - 1) + 1;
		if (k < 0) {
			res = 0.5 * x;
		}
		else {
			res = x / (2.0 + k * f);
			for (i = 0; i < k; i++) {
				res += c / (2.0 + i*f);
			}
		}
		printf("Case #%d: %.6lf\n", t, res);
	}
	return 0;
}