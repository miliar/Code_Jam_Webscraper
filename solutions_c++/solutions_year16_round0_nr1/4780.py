#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int n;
		cin >> n;
		if (n == 0) {
			cout << "Case #" << test << ": INSOMNIA" << endl;
			continue;
		}
		int ans;
		vector<int> digits(10);
		int count = 0;
		for (ans = 1;; ++ans) {
			int num = ans*n;
			while (num != 0) {
				int last = num % 10;
				if (digits[last] == 0) {
					++digits[last];
					++count;
				}
				num = num / 10;
			}
			if (count == 10) {
				break;
			}
		}
		cout << "Case #" << test << ": " << ans*n << endl;
	}
}
