#include <iostream>
#include <vector>
#include <set>

using namespace std;

set<int> digitize(int N) {
	set<int> s;
	while (N > 0) {
		s.insert(N % 10);
		N = N / 10;
	}
	return s;
}

int lastNum(int N) {
	if (N == 0) {
		return -1;
	}
	set<int> digits, tempDigits;
	int i = 0;

	while (digits.size() < 10) {
		i++;
		tempDigits = digitize(i * N);
		digits.insert(tempDigits.begin(), tempDigits.end());
		if (i > 200000) {
			return -1;
		}
	}
	return i * N;
}

int main() {
	int T, N;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cin >> N;
		int last = lastNum(N);
		cout << "Case #" << i << ": ";
		if (last == -1)
			cout << "INSOMNIA";
		else
			cout << last;
		cout << endl;
	}
}