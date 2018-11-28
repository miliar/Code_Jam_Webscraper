#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cfloat>
#include <ctime>
#include <algorithm>
#include <functional>
#include <vector>
#include <set>
#include <map>
#include <queue>
using namespace std;

int T;
double C, F, X;

int main() {
	scanf("%d", &T);
	for (int casen = 1; casen <= T; casen++) {
		printf("Case #%d: ", casen);

		scanf("%lf%lf%lf", &C, &F, &X);
		double v = 2, base = 0;
		double ans = DBL_MAX;

		while (1) {
			double cur = base + X / v;
			if (cur > ans) break;
			ans = cur;
			base += C / v;
			v += F;
		}
		printf("%.8lf\n", ans);

	}

	return 0;
}
