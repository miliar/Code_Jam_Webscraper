#include <bits/stdc++.h>

using namespace std;

int t;

int getbitmask(int n) {
	int ret = 0;
	if (n == 0) return 1;
	while (n != 0) {
		ret = ret | (1<<(n%10));
		n /= 10;
	}
	return ret;
}

void solve(long long int n) {
	long long int l = 0;
	int mask = 0;
	while (l <= 10000 && mask != 1023) {
		l += 1;
		mask |= getbitmask(n * l);
	}
	if (mask == 1023) {
		printf("%lld\n", l * n);
	}
	else {
		printf("INSOMNIA\n");
	}
}

int main() {
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		int n; scanf("%d", &n);
		printf("Case #%d: ", i);
		solve(n);
	}
	return 0;
}