#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;

bool isPalindrome(int number) {
	stringstream ss;
	string n;
	int i, j;

	ss << number;
	n = ss.str();
	j = n.length() - 1;
	if (j == 0) {
		return true;
	}

	for (i = 0;  2*i < j; i++) {
		if (n[i] != n[j-i]) {
			return false;
		}
	}
	return true;
}

int calculate(unsigned long long A, unsigned long long B) {
	int i, j, min, max;
	int c = 0;

	min = ceil(sqrt(A));
	max = floor(sqrt(B));
	for (i = min; i <= max; ++i) {
		if (!isPalindrome(i)) {
			continue;
		}
		j = i * i;
		if (!isPalindrome(j)) {
			continue;
		}
		c++;
	}
	return c;
}

int main() {
	int T;
	unsigned long long A, B;
	int i;

	cin >> T;

	for (i = 1;  i <= T; ++i) {
		cin >> A >> B;
		cout << "Case #" << i << ": " << calculate(A, B) << endl;
	}
}
