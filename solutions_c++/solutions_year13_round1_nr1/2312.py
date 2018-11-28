#include<stdio.h>
int main() {
	int T, cas = 0;
	long long r, t;
	long long p, i;
	scanf("%d", &T);
	while (T--) {
		cas++;
		scanf("%I64d%I64d", &r, &t);
		p = 0;
		r++;
		for (i = 0;; ++i) {
			if (p > t - r * r + (r - 1) * (r - 1))
				break;
			p += (r * r - (r - 1) * (r - 1));
			r += 2;
		}
		printf("Case #%d: %I64d\n", cas, i);
	}
}
