#include <cstdio>
#include <bitset>
using namespace std;

int main() {
	int t;
	double f, c, x;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		scanf("%lf %lf %lf", &c, &f, &x);
		double cookies = 0.0;
		double ans = 0.0;
		double plus = 2.0;
		while ((ans + x / plus) > (ans + (c / plus) + (x / (plus + f)))) {
			ans += c / plus;
			plus += f;
		}
		ans += x / plus;
		printf("Case #%d: %.10lf\n", tc, ans);
	}
	return 0;
}
