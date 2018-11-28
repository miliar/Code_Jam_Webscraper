#include <iostream>
#include <vector>

using namespace std;

void mark(vector<bool>& digits, int n) {
	if (n == 0) digits[0] = true;
	while (n > 0) {
		digits[n % 10] = true;
		n /= 10;
	}
}

bool done(vector<bool>& digits) {
	for (int i = 0; i < 10; ++i) if (digits[i] == false) return false;
	return true;
}

bool loop() {
	// TODO
	return false;
}

int testcase() {
	int n;
	cin >> n;
	if (n == 0) return -1;

	vector<bool> digits(10);
	for (int i = 0; i < 10; ++i) digits[i] = false;

	int x = n;
	while (true) {
		mark(digits, x);
		if (done(digits)) return x;
		//if (loop()) return -1;
		x += n;
	}
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		int n = testcase();
		if (n == -1) cout << "Case #" << i << ": INSOMNIA" << endl;
		else cout << "Case #" << i << ": " << n << endl;
	}
}
