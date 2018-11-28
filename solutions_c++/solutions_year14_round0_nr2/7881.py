#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int TC;
	scanf("%d", &TC);
	for(int tc=1; tc<=TC; tc++) {
		double c, f, x;
		double c_t=0, t;
		double cookie = 2;
		double ans;
		scanf("%lf %lf %lf", &c, &f, &x);
		ans = 0.5*x;
		for(int i=0; i<100002; i++) {
			t = 1/cookie;
			ans = min(ans, c_t+t*x);
			c_t += t*c;
			cookie += f;
		}
		printf("Case #%d: %.7lf\n", tc, ans);
	}
	return 0;
}