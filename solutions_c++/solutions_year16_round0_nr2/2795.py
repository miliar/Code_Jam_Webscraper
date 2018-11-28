#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int T;
	cin >> T;

	for (int tt = 1; tt <= T; ++tt) {
		cout << "Case #" << tt << ": ";
		int count = 0;
		string S;
		cin >> S;

		if (S.length() == 1) {
			if (S[0] == '-') cout << 1 << '\n';
			else cout << 0 << '\n';
			continue;
		}

		char cur = S[0];
		for (int i = 1; i < S.length(); ++i) {
			if (S[i] != cur) {
				if (cur == '+') {
					count += 1;
				} else {
					count += 1;
				}
				cur = S[i];
			}
		}

		if (cur == '-') count++;
		cout << count << '\n';
	}

	return 0;
}