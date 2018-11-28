#include <cstdio>

int casei, cases;
long long N, P, NN;

bool win(long long now) {
	now = NN - now;
	long long top = NN;
	while (now > 1LL) {
		now >>= 1LL;
		top >>= 1LL;
	}
	return (top <= P);
}

bool lose(long long now) {
	now = now + 1LL;
	long long dist = NN >> 1LL;
	long long top = 0;
	while (now > 1LL) {
		now >>= 1LL;
		top += dist;
		dist >>= 1LL;
	}
	return (top >= P);
}

int main() {
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf("%I64d%I64d", &N, &P);
		NN = 1LL << N;
		long long left = 0;
		long long right = NN - 1LL;
		long long mid;
		long long ans1 = 0, ans2 = 0;
		while (left <= right) {
			mid = (left + right) >> 1LL;
			if (win(mid)) {
				if (mid > ans2) ans2 = mid;
				left = mid + 1LL;
			}
			else
				right = mid - 1LL;
		}
		left = 0;
		right = NN - 1LL;
		while (left <= right) {
			mid = (left + right) >> 1LL;
			if (lose(mid)) {
				right = mid - 1;
			}
			else {
				if (mid > ans1) ans1 = mid;
				left = mid + 1;
			}
		}
		
		printf("Case #%d: %I64d %I64d\n", casei, ans1, ans2);
	}

	return 0;
}
