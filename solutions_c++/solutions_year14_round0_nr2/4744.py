#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;
int T;
int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		double c, f, x, ans(0);
		scanf("%lf%lf%lf", &c, &f, &x);
		double v0 = f * (x - c) / c;
		if (v0 < 2.0) ans = x / 2.0;
		else {
			int n0 = ceil((v0 - 2.0) / f);
			for (int i = 0; i < n0; ++i)
				ans += c / (2.0 + i * f);
			ans += x / (2.0 + n0 * f);
		}
		printf("Case #%d: %.7lf\n",t, ans);
	}
	return 0;
}
