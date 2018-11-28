#pragma comment(linker, "/STACK:64000000")
#include <algorithm>
#include <memory.h>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cassert>
#include <map>
#include <set>
#include <vector>
#include <queue>

using namespace std;
#define prev privet1
#define next privet2
#define y1 privet3
#define rank privet4
#define left privet5
#define right privet6
#define y0 privet7

const double pi = 3.141592653589793238;

void ensureLimit(long long n, long long l, long long r)
{
	assert(l <= n && n <= r);
}


double get(double c, double f, double x, long long cnt) {
	double res = 0, denumerator = 2;
	for (long long i = 0; i < cnt; i++) {
		res += c / denumerator;
		denumerator += f;
	}
	res += x / (f * cnt + 2);
	return res;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for (int cases = 1; cases <= tc; cases++) {
		printf("Case #%d: ", cases);
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		long long l = 0, r = 100000000;
		while (l + 2 < r) {
			long long m = (r - l) / 3;
			long long m1 = l + m, m2 = r - m;
			double f1 = get(c, f, x, m1), f2 = get(c, f, x, m2);
			if (f1 < f2) r = m2;
			else l = m1;
		}
		double ans = 1e18;
		while (l <= r) {
			ans = min((double)ans, (double)get(c, f, x, l));
			l++;
		}
		printf("%.15lf\n", ans);
	}
}
