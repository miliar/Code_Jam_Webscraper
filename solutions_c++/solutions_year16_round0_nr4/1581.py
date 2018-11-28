#include <iostream>

using namespace std;

typedef unsigned long long ull;

ull pow(ull a, ull n) {
	ull r = 1;
	while (n) {
		if (n % 2) {
			r *= a;
		}
		n /= 2;
		a *= a;
	}
	return r;
}

int main() {
	int T = 0;
	cin >> T;

	for (int i = 0; i < T; ++i) {
		ull K, C, S;
		cin >> K >> C >> S;
		ull add = pow(K, C - 1);
		cout << "Case #" << i + 1 << ":";
		for (ull j = 0; j < K; ++j) {
			cout << ' ' << 1 + j * add;
		}
		cout << endl;
	}

	return 0;
}
