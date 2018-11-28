#include <bits/stdc++.h>

using namespace std;

void solve() {
	int n;
	scanf("%d", &n);
	if (n == 0) {
		printf("INSOMNIA\n");
		return;
	}          
	int mask = 0;
	int add = n;
	while (true) {
		int tmp = n;
		for(; tmp; tmp /= 10) mask |= (1 << (tmp % 10));
		if (mask == (1 << 10) - 1) {
			printf("%d\n", n);
			return;
		}
		n += add;
	}
}

int main() {
	int ntest;
	scanf("%d", &ntest);
	for(int tc = 1; tc <= ntest; ++tc) {
		printf("Case #%d: ", tc);
		solve();
	}
	return 0;
}