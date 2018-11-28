#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

void digit(int n, int& bitmask) {

}

int solve(int n) {
	if (!n) return -1;


	int x = 1, cnt = 0;
	bool chk[10];
	memset(chk, 0, sizeof(chk));

	while (true) {
		int m = n * x;

		while (m > 0) {
			if (!chk[m % 10]) cnt++;
			chk[m % 10] = true;
			m /= 10;
		}

		if (cnt == 10) return n * x;

		x++;
	}
}

int main() {

	int testcase, n;
	cin >> testcase;

	for (int t = 1; t <= testcase; t++) {
		scanf("%d", &n);

		int ans = solve(n);

		if (ans == -1) printf("Case #%d: INSOMNIA\n", t);
		else printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}