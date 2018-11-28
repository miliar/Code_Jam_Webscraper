#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define Rep(i, n) for (int i = 1; i <= (n); ++i)
#define clr(x, a) memset(x, (a), sizeof x)
using namespace std;
typedef long long ll;
double const eps = 1e-8;
double r[111], c[111];
int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("b-small-ans2.txt", "w", stdout);
	int T, ca = 1, n;
	double vs, cs;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%lf%lf", &n, &vs, &cs);
		rep(i, n) {
			scanf("%lf %lf", &r[i], &c[i]);
		}
		if (n == 1) {
			if (fabs(c[0] - cs) < eps) {
				double ans = vs / r[0];
				printf("Case #%d: %.10lf\n", ca++, ans);
			} else{
				printf("Case #%d: IMPOSSIBLE\n", ca++);
			}
		} else {
			double ans = -1;
			if (fabs(c[0] - c[1]) < eps) {
				ans = vs / (r[0] + r[1]);
			} else {
				double v0 = vs * (cs - c[1]) / (c[0] - c[1]);
				if (v0 >= 0 && v0 <= vs + eps) {
					double v1 = vs - v0;
					ans = max(v0 / r[0], v1 / r[1]);
				}
			}
			if (c[0] < cs && c[1] < cs) ans = -1;
			if (c[0] > cs && c[1] > cs) ans = -1;
			if (ans < 0) {
				printf("Case #%d: IMPOSSIBLE\n", ca++);
			} else {
				printf("Case #%d: %.10lf\n", ca++, ans);
			}
		}
	}
	return 0;
}


