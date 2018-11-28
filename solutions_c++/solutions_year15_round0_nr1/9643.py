#include <iostream>

using namespace std;

int T, smax, s[1001];

int solve() {
	int sum = s[0];
	int result = 0;
	for (int i = 1; i <= smax; ++i) {
		while (sum < i) {
			++sum;
			++result;
		}
		sum += s[i];
	}
	return result;
}

int main() {
	cin >> T;
	char c;
	for (int t = 1; t <= T; ++t) {
		cin >> smax;
		for (int i = 0; i <= smax; ++i) {
			cin >> c;
			s[i] = (int) (c - 48);
		}
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}