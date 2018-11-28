#include <cstdio>
using namespace std;

void solve() {
	double c, f, x;
	scanf("%lf%lf%lf", &c, &f, &x);
	double ans = x / 2;
	for(int i = 1; i < ((x + c) * f - c * (f + 2)) / (f * c); ++i)
		ans += (c - x) / (2 + f * (i - 1)) + x / (2 + i * f);
	printf("%.7lf\n", ans);
}

int main() {
	// freopen("input.txt", "r", stdin);
	freopen("B-large.in.txt", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	
	return 0;
}