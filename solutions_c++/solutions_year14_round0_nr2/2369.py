#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int nc = 1; nc <= T; ++nc) {
		printf("Case #%d: ", nc);
		double C, F, X;
		cin >> C >> F >> X;
		double ans = X / 2.0;
		if (X <= C) {
			printf("%.10lf\n", ans);
			continue;
		}
		double cur = 0, rate = 2.0;
		while (cur < ans) {
			ans = min(ans, cur + X / rate);
			cur += 1.0 * C / rate;
			rate += F;
		}
		printf("%.10lf\n", ans);
	}
}
