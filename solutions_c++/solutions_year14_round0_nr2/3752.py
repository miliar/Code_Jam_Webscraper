#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

void solve() {
	double c, f, x;
	scanf("%lf%lf%lf", &c, &f, &x);
	int cnt = x + 1;
	double cur_prod = 2;
	double ans = 1e9;
	double time_build = 0;
	for (int i = 0; i <= cnt; ++i) {
		ans = min(ans, x / cur_prod + time_build);
		time_build += c / cur_prod;
		cur_prod += f;
	}
	printf("%.10lf", ans);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
	}
	return 0;
}