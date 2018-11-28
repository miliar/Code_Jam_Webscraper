#include <queue>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

#define LL long long

int T;
LL B, N;
LL M[1024];
int ans;
LL l, r, mid, st;

bool check(LL num) {
	LL sum = 0;
	for (int i = 0; i < B; ++i) {
		sum += (num / M[i]) + 1ll;
		if (sum >= N) return true;
	}
	return false;
}

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d: ", test);
		scanf("%lld %lld", &B, &N);
		for (int i = 0; i < B; i++)
			scanf("%lld", M + i);
		l = 0;
		r = 1e18;
		st = r;
		while (l <= r) {
			mid = (l + r) / 2;
			if (check(mid)) {
				st = mid;
				r = mid - 1;
			} 
			else l = mid + 1;
		}
		LL now = 0;
		for (int i = 0; i < B; i++)
			now += (st + M[i] - 1ll) / M[i];
		for (int i = 0; i < B; i++) {
			if (st % M[i] == 0) {
				now++;
				if (now == N) {
					ans = i + 1;
				}
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}