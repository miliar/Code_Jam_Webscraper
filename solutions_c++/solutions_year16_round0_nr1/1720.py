#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

long long find_number(long long i) {
	int length = 0;
	int cnt = 0;
	long long n = 0, cop, x;
	bool app[10];
	fill(app, app + 10, false);

	n = i;
	length = 1;
	while (cnt < 10) {
		n = length*i;

		cop = n;
		while (n != 0) {
			x = n % 10;
			if (!app[x]) {
				app[x] = true;
				cnt++;
			}
			n = n / 10;
		}

		length++;
	}

	return cop;
}

int main() {
	int tests, n;

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &tests);

	for (int t = 1; t <= tests; t++) {
		scanf("%d", &n);

		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", t);
		}
		else {
			printf("Case #%d: %lld\n", t, find_number(n));
		}
	}

	return 0;
}