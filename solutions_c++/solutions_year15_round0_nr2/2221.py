#include <cstdio>
#include <algorithm>
#include <functional>
using namespace std;

bool valid(int D, int P[], int mid) {
	for (int i = 0; i < mid; ++i) {
		int j = mid - i;
		int cnt = 0;
		for (int k = 0; k < D; ++k) {
			if (P[k] <= j) continue;
			cnt += (P[k] - 1) / j;
		}
		if (cnt <= i) return true;
	}
	return false;
}

int main() {
	int T, D, P[1005], p[1005];
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &D);
		for (int i = 0; i < D; ++i) {
			scanf("%d", &P[i]);
		}
		int mi = 1, mid, ma = 1000;
		while (mi < ma) {
			mid = (mi + ma) >> 1;
			if (valid(D, P, mid)) {
				ma = mid;
			}
			else {
				mi = mid + 1;
			}
		}
		printf("Case #%d: %d\n", tc, mi);
	}
	return 0;
}