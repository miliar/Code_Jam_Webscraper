#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cassert>

using namespace std;

int main () {
	int i, j, k, ca, T;

	freopen ("B-large.in", "r", stdin);
	freopen ("outBlarge.txt", "w", stdout);
	scanf ("%d", &T);
	for (ca = 1; ca <= T; ++ca) {
		double rate = 2.0;
		double inc, tot, cost, ans = 100000.0, tm = .0;
		scanf ("%lf%lf%lf", &cost, &inc, &tot);

		while (true) {
			ans = min(ans, tm + tot / rate);
			if (cost / rate + tm > ans + 1e-9) break;
			tm += cost / rate;
			rate += inc;
		}
		printf ("Case #%d: %.9lf\n", ca, ans);
	}
	return 0;
}
