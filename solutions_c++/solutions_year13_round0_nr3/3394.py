#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

bool isPalindrome(long long val) {
	vector<int> digits;
	while (val > 0) {
		digits.push_back(val % 10);
		val /= 10;
	}
	for (int i = 0, j = digits.size() - 1; i < j; i++, j--)
		if (digits[i] != digits[j])
			return false;
	return true;
}

int main() {
	int T;
	long long A, B;
	cin >> T;
	for (int CASE = 1; CASE <= T; CASE++) {
		cin >> A >> B;
		int count = 0;
		for (long long i = (long long)ceil(sqrt(A)); i*i <= B; i++) {
			if (isPalindrome(i) && isPalindrome(i*i)) {
				// cout << i * i << endl;
				count++;
			}
		}
		cout << "Case #" << CASE << ": " << count << endl;
	}
}