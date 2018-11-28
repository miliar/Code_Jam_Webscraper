// Problem B. Cookie Clicker Alpha
#include <cstdio>
#include <cstdlib>

using namespace std;

int main(int argc, char *argv[])
{
	int nc, ci;

	scanf("%d", &nc);
	for (ci = 1; ci <= nc; ci++) {
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double ans = x;
		for (double t = 0, v = 2; ; t += c / v, v += f) {
			double tt = t + x / v;
			if (tt < ans) ans = tt;
			else break;
		}

		printf("Case #%d: %.7f\n", ci, ans);
	}

	return 0;
}
