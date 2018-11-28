#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

void work() {
	double c, f, x;
	scanf("%lf%lf%lf", &c, &f, &x);
	double ans = x / 2;
	double sum = 0, v = 2;
	for (int i = 0; ; i++) {
		ans = min(ans, x / v + sum);
		sum += c / v;
		v += f;
		if (sum > ans)
			break;
	}
	printf("%.10f\n", ans);
}

int main() {
	int T, C = 0;
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d: ", ++C);
		work();
	}
	return 0;
}
