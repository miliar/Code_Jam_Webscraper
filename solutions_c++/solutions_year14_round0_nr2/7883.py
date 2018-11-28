#include <iostream>

using namespace std;

double C, F, X;

void Solve() {
	cin >> C >> F >> X;

	const int MAX_FARMS = 101 * 1000;

	double ans = 1e100;
	double subTime = 0;
	for (int i = 0; i < MAX_FARMS; ++i) {
		if (i > 0)
			subTime += C / (2. + (i - 1.) * F);
		double time = subTime + X / (2. + i * F);
		ans = min(ans, time);
	}
	printf("%.6lf\n", ans);
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		Solve();
	}
}