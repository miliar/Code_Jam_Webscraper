#include <iostream>
#include <string>
#include <cstdlib>

using std::string;
using std::cin;
using std::cout;

int main() {

	int t;
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		bool nums[10];
		for (int j = 0; j < 10; ++j) {
			nums[j] = false;
		}

		int n;
		cin >> n;

		if (n == 0) {
			cout << "Case #" << i << ": INSOMNIA\n";
		} else {
			int k = n;
			bool all_digits_seen = false;
			while (!all_digits_seen) {
				all_digits_seen = true;
				string digits = std::to_string(k);
				for (string::iterator iter = digits.begin(); iter != digits.end(); ++iter) {
					nums[*iter - '0'] = true;
				}
				for (int j = 0; j < 10; ++j) {
					if (nums[j] == false) {
						all_digits_seen = false;
						k += n;
						break;
					}
				}
			}
			cout << "Case #" << i << ": " << k << "\n";
		}
	}

	return 0;
}