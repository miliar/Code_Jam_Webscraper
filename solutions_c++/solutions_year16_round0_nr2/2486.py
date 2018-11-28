#include <iostream>
#include <algorithm>

using namespace std;

int solve(string s) {
	int count = 0;
	for (int i = s.length() - 1; i >= 0; --i) {
		if (s[i] == '-') {
			int j = 0;
			while (s[j] == '+') {
				++j;
			}

			if (j > 0) {
				for (int k = 0; k < j; ++k) {
					s[k] = '-';
				}
				++count;
			}
			reverse(s.begin(), s.begin() + i + 1);
			for (int k = 0; k <= i; ++k) {
				if (s[k] == '+') {
					s[k] = '-';
				} else {
					s[k] = '+';
				}
			}
			++count;
		}
	}
	return count;
}

int main() {
	int testCaseCount = 0;
	cin >> testCaseCount;
	for (int i = 1; i <= testCaseCount; ++i) {
		string s;
		cin >> s;
		int result = solve(s);
		cout << "Case #" << i << ": " << result << endl;
	}
	return 0;
}
