#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

const double INF = 500000.0;

int main() {
	int t;
	scanf("%d", &t);
	for(int kase = 1; kase <= t; kase++) {
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);

		double ans = INF;
		for(int i = 0; ; i++) {
			double tmp = 0;
			for(int j = 0; j < i; j++) {
				tmp += c / (2 + f * j);

			}

			//printf("%f|\n", tmp);

			double tmp2 = tmp + x / (i * f + 2);
			//printf("%f\n", tmp2);
			if(tmp2 < ans)	ans = tmp2;
			else	break;
		}

		printf("Case #%d: %.7f\n", kase, ans);
	}

	return 0;
}
