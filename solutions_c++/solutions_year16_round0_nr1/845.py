#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

int T;
LL N;

LL getbit(LL num) {
	LL ans = 0;
	while (num > 0) {
		ans |= (1 << (num % 10ll));
		num /= 10ll;
	}
	return ans;
}

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; ++test) {
		printf("Case #%d: ", test);
		scanf("%lld", &N);
		if (N == 0) {
			printf("INSOMNIA\n");
		} else {
			LL mask = 0, ans = 0;
			for (LL i = 1; ; ++i) {
				ans = i * N;
				mask |= getbit(ans);
				if (mask == 1023)
					break;
			}
			printf("%d\n", ans);
		}
	}
	return 0;
}