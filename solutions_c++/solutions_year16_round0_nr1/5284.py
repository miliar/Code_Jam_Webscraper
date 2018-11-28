#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <functional>
#include <numeric>

using namespace std;

using llong = long long;

bool seen[10];

bool seen_all() {
	return all_of(begin(seen), end(seen), [](bool x) {return x;});
}

void see_digits(llong x) {
	while (x != 0) {
		seen[x % 10] = 1;
		x /= 10;
	}
}

llong solve(llong x) {
	llong y = x;
	memset(seen, 0, sizeof(seen));
	see_digits(y);
	while (!seen_all()) {
		y += x;
		see_digits(y);
	}
	return y;
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1;i <= t;i++) {
		int a;
		cin >> a;
		printf("Case #%d: ", i);
		if (a == 0) printf("INSOMNIA\n");
		else printf("%lld\n", solve(a));
	}

	return 0;
}