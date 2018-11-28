#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int T;

	cin >> T;

	for (int i = 0; i < T; ++i) {
		int K;
		cin >> K;
		int C;
		cin >> C;
		int S;
		cin >> S;

		long long res = 1;

		for (int j = 0; j < C - 1; ++j) {
			res *= K;
		}

		cout << "Case #" << i + 1 << ":";

		for (int j = 0; j < S; ++j) {
			cout << " " << j * res + 1;
		}
		cout << endl;
	}

	return 0;
}
