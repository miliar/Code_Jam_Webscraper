#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

struct node {
	double v, x;
} a[1005];
bool cmp(node a, node b) {
	return a.x < b.x;

}
int main() {
	int t, cas = 0;
	int n;
	int i, j, k;
	double v, x;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d", &n);
		//cin >> v >> x;
		scanf("%lf%lf", &v, &x);
		bool flag1, flag2, flag3;
		flag2 = flag1 = false;
		for (i = 0; i < n; ++i) {
			scanf("%lf%lf", &a[i].v, &a[i].x);
			if (x + 1e-5 > a[i].x)
				flag1 = true;
			if (x - 1e-5 < a[i].x)
				flag2 = true;
		}
		if (n == 1 && fabs(x - a[0].x) < 1e-5) {
			printf("Case #%d: %.12f\n", cas, v / a[0].v);
			continue;
		}

		if (n == 2 && fabs(x - a[0].x) < 1e-5 && fabs(x - a[1].x) < 1e-5) {
			printf("Case #%d: %.12f\n", cas, v / (a[0].v + a[1].v));
			continue;
		}
		if (n == 2 && fabs(x - a[0].x) < 1e-5) {
			printf("Case #%d: %.12f\n", cas, v / a[0].v);
			continue;
		}
		if (n == 2 && fabs(x - a[1].x) < 1e-5) {
			printf("Case #%d: %.12f\n", cas, v / a[1].v);
			continue;
		}
		double v2 = v * (a[0].x - x) / (-a[1].x + a[0].x);
		double v1 = v - v2;
		double ans = max(v2 / a[1].v, v1 / a[0].v);

		if (flag1 == false || flag2 == false)
			printf("Case #%d: IMPOSSIBLE\n", cas);
		else
			printf("Case #%d: %.12f\n", cas, ans);
	}
}
