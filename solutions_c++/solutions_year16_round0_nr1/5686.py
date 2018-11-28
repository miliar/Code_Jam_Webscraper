#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

int count(int n) {
	int all = 0b1111111111;
	int seen = 0b0000000000;
	int nx = 0;
	while (seen != all) {
		nx += n;
		for (int m = nx; m > 0; m/=10) {
			seen |= 1 << (m % 10);
		}
	}
	return nx;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n", t);
		} else {
			int nx = count(n);
			printf("Case #%d: %d\n", t, nx);
		}
	}
}
