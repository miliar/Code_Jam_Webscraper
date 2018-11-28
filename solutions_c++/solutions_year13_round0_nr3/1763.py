#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long int uint64;

bool is_palindrome(uint64 n) {
	uint64 rev = 0;
	uint64 ori = n;

	while (n > 0) {
		rev *= 10;
		rev += n%10;
		n /= 10;
	}

	return rev == ori;
}

int main() {
	int t;
	vector<uint64> faqs;

	for (uint64 ab = 0; ab <= 10000000; ++ab) {
		if (is_palindrome(ab) && is_palindrome(ab*ab)) {
			faqs.push_back(ab*ab);
		}
	}

	cin >> t;
	for (int tt = 0; tt < t; ++tt) {
		uint64 a, b;
		int count = 0;
		cin >> a >> b;

		for (int i = 0; i < faqs.size(); ++i) {
			if (faqs[i] >= a && faqs[i] <= b) ++count;
		}

		cout << "Case #" << tt+1 << ": " << count << endl;
	}
}