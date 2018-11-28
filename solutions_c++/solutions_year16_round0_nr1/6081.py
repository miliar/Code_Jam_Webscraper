#include <iostream>

using namespace std;

inline void setBit(int& n, int position) {
	n = n | (1 << position);
}

long int solve(int N) {
	int counted = 0;
	long int num = 0, temp;
	const int allSetChecker = (1 << 10) - 1;

	if (0 == N) {
		return -1;
	}

	for (int i = 1; num <= N * 1000000; ++i) {
		num += N;
		temp = num;

		while (temp > 0) {
			setBit(counted, temp % 10);
			temp = temp / 10;
		}

		if (counted == allSetChecker) {
			return num;
		}
	}

	return -1;
}

int main() {
	int T, N;
	cin >> T;

	for (int i = 0; i < T; ++i) {
		cin >> N;

		long int answer = solve(N);

		cout << "Case #" << i + 1 << ": ";
		if (-1 == answer) {
			cout << "INSOMNIA" << endl;
		}
		else {
			cout << answer << endl;
		}
	}

	return 0;
}