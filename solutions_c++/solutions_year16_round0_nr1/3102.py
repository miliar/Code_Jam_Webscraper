#include <bits/stdc++.h>
using namespace std;
int check(long long x) {
	int ret = 0;
	while(x) {
		ret |= (1 << (x % 10));
		x /= 10;
	}
	return ret;
}
int main() {
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.ou", "w", stdout);
	int T, n, cases = 0;
	scanf("%d", &T);
	while(T--) {
		printf("Case #%d: ", ++cases);
		scanf("%d", &n);
		if(n == 0) {
			puts("INSOMNIA");
			continue;
		}
		int mask = 0;
		long long now = 0;
		while(mask != 1023) {
			now += n;
			mask |= check(now);
		}
		printf("%I64d\n", now);
	}
	return 0;
}
