#include <cstdio>

const double EPS = 0;

int main(void) {
	int test_count;
	scanf("%d", &test_count);
	for (int test = 1; test <= test_count; ++ test) {
		double c, f, x, f_cnt = 2;
		scanf("%lf%lf%lf", &c, &f, &x);
		double ret = 0, ans = x / 2.0;
		while (ret + c / f_cnt + x / (f_cnt + f) < ans - EPS) {
			ret += c / f_cnt;
			f_cnt += f;
			ans = ret + x / f_cnt;
		}
		printf("Case #%d: %.8f\n", test, ans);
	}
	return 0;
}
