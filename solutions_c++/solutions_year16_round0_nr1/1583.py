#include <iostream>

using namespace std;

typedef unsigned long long ull;

void solve(int i, ull n) {
	if (0 == n) {
		cout << "Case #" << i << ": INSOMNIA" << endl;
		return;
	}

	bool digs[10] = { false };
	ull sum = 10;

	ull nn = 0;
	while (0 < sum) {
		nn += n;
		ull cur = nn;
		while (0 < cur) {
			ull dig = cur % 10;
			cur /= 10;
			if (!digs[dig]) {
				--sum;
				digs[dig] = true;
			}
		}
	}

	cout << "Case #" << i << ": " << nn << endl;
}

int main() {
	int T = 0;
	
	cin >> T;

	for (int i = 0; i < T; ++i) {
		ull n = 0;
		cin >> n;
		solve(i + 1, n);
	}

	return 0;
}
