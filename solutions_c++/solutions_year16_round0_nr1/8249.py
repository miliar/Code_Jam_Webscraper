#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll solve(int n) {
	ll cur = 0;
	set<int> digits;
	int iters = 0;
	while (digits.size() < 10 && iters < 100) {
		cur += n;
		int tmp = cur;
		while (tmp) {
			digits.insert(tmp % 10);
			tmp /= 10;
		}

		iters++;
	}

	if (digits.size() < 10) return -1;
	return cur;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int ctest = 1; ctest <= t; ctest++) {
		int n;
		scanf("%d", &n);


		printf("Case #%d: ", ctest);
		ll res = solve(n);
		if (res == -1) printf("INSOMNIA\n");
		else printf("%lld\n", res);
	}

	/*for (int i = 0; i <= 1e6; i++) {
		int res = solve(i);
		if (res == -1) printf("-> %d\n", i);
	}*/

	return 0;
}
