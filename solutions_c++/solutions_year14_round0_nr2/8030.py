#include <cstdio>

int main() {
	int T;
	double c, f, x, tt, time, minn, s;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%lf%lf%lf", &c, &f, &x);
		s = 2.0;
		time = 0.0;
		minn = 1e11;
		while (1) {
			tt = x / s + time;
			if (tt < minn) minn = tt;
			else break;
			time += c / s;
			s += f;
		}
		printf("Case #%d: %.7lf\n", t, minn);
	}
	return 0;
}
