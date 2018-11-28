#include <bits/stdc++.h>

using namespace std;

string solve() {
	int n;
	cin >> n;
	vector <bool> digits(10, false);
	for (int i = 0; i < 1000000; ++i) {
		int nn = (i + 1) * n;
		while (nn > 0) {
			digits[nn % 10] = true;
			nn /= 10;
		}
		if (count(digits.begin(), digits.end(), true) == 10) {
			return to_string((i + 1) * n);
		}		 
	}
	return "INSOMNIA";
}

int main() {
#ifdef ALEXEY
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
#endif
	int test_count;
	cin >> test_count;
	for (int i = 1; i <= test_count; ++i) {
		cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}
