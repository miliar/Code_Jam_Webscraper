#include <cstdio>
#define eps 1e-10
double c, f, x;
bool judge(double y) {
	double tim = 0;
	double money = 0;
	double per = 2.0;
	while(y - tim > eps) {
		if(money + (y - tim) * per >= x) return true;
		tim += c / per;
		per += f;
	}
	return false;
}
int main() {
//	freopen("in", "r", stdin);
//	freopen("out", "w", stdout);
	int T, cases = 0;
	scanf("%d", &T);
	while(T--) {
		scanf("%lf%lf%lf", &c, &f, &x);
		double l = 0, r = x, ans = 0;
		while(r - l > eps) {
			double mid = (l + r) / 2;
			if(judge(mid)) {
				ans = mid;
				r = mid;
			} else l = mid;
		}
		printf("Case #%d: %.8f\n", ++cases, ans);
	}
	return 0;
}
