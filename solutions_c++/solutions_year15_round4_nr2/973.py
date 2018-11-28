#include <iostream>
#include <algorithm>

using namespace std;

const int N = 104;

double rs[N];
double cs[N];

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		int n;
		double v, x;
		scanf("%d%lf%lf", &n, &v, &x);
		for (int i = 0; i < n; i++) {
			scanf("%lf%lf", rs+i, cs+i);
		}
		bool flag = true;
		double ans = 0;
		if (n == 2 && cs[1] == x && cs[0] != x) {
			n--;
			swap(cs[1], cs[0]);
			swap(rs[1], rs[0]);
		}
		else if (n == 2 && cs[0] == x && cs[1] != x) {
			n--;
		}
		if (n == 2 && cs[0] != cs[1]) {
			double v0 = (x-cs[1])/(cs[0]-cs[1])*v;
			if (v0 < 0 || v0 > v) {
				flag = false;
			}
			else {
				double v1 = v-v0;
				ans = max(v0/rs[0], v1/rs[1]);
			}
		}
		else {
			if (cs[0] != x) {
				flag = false;
			}
			else {
				if (n == 1) ans = v/rs[0];
				else ans = v/(rs[0]+rs[1]);
			}
		}
		if (flag) {
			printf("Case #%d: %lf\n", cas, ans);
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n", cas);
		}
	}
	return 0;
}