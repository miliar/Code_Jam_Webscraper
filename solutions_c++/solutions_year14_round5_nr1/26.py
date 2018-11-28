#include <cstdio>
#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;

#define mp(a,b) make_pair(a, b)

long long q[1000005];

void Solve() {
	long long n, p, qq, r, s;
	cin >> n >> p >> qq >> r >> s;
	for (int i = 1; i <= n; ++i) {
		q[i] = ((i - 1) * p + qq) % r + s;
		q[i] += q[i - 1];
	}
	long long best = 0, total = q[n];
	for (int i = 1; i <= n; ++i) {
		int lb = 0, ub = i;
		while (ub - lb > 1) {
			int mb = (ub + lb) >> 1;
			if (q[mb] < q[i] / 2) {
				lb = mb;
			} else {
				ub = mb;
			}
		}
		long long dvd = min(max(q[lb], q[i] - q[lb]), max(q[ub], q[i] - q[ub]));
		long long enemy = max(total - q[i], dvd);
		best = max(best, total - enemy);
	}
	printf("%.10f\n", (double)best / total);
}

int main() {
	freopen("a_large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d: ", I + 1);
		Solve();
	}
	return 0;
}