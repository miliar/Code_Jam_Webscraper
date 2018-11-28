#include <bits/stdc++.h>
using namespace std;

int T, N;
string S;

int main() {

	cin >> T;
	for (int test = 1; test <= T; ++test) {

		cin >> N;
		cin >> S;

		int total = 0;
		int ans = 0;

		for (int i = 0; i < (int)S.size(); ++i)
			if (S[i] - '0' >= 0) {
				if (i > total) {
					ans += i - total;
					total = i;
				}
				total += S[i] - '0';
			}

		cout << "Case #" << test << ": " << ans << endl;
	}

	return 0;
}
