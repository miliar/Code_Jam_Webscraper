#include <cstdio>
#include <map>
#include <algorithm>
using namespace std;

int a[1000], b[1000], c[1000], d[1000];

int solve() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i += 1)
		scanf("%d", a + i);
	int l = 0, r = N - 1;
	int ans = 0;
	while (l < r) {
		int mn = l;
		for (int i = l; i <= r; i += 1)
			if (a[i] < a[mn])
				mn = i;
		if (mn - l < r - mn) {
			ans += mn - l;
			while (mn > l) {
				swap(a[mn], a[mn - 1]);
				--mn;
			}
			l += 1;
		} else {
			ans += r - mn;
			while (mn < r) {
				swap(a[mn], a[mn + 1]);
				++mn;
			}
			r -= 1;
		}
	}
	return ans;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i += 1)
		printf("Case #%d: %d\n", i, solve());
}

