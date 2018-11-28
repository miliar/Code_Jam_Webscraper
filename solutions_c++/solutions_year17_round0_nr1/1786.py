#include <iostream>
#include <string>

using namespace std;

void Solve(string s, int K) {
	int ans = 0;
	for (int i = 0; i < s.length() - K + 1; ++i) {
		if (s[i] == '-') {
			++ans;
			for (int j = i; j < i + K; ++j) {
				s[j] = s[j] == '-' ? '+' : '-';
			}
		}
	}
	if (s.find('-') != string::npos) {
		cout << "IMPOSSIBLE";
		return;
	}

	cout << ans;
}

void main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		string s;
		cin >> s;
		int K;
		cin >> K;
		cout << "Case #" << i + 1 << ": ";
		Solve(s, K);
		cout << endl;
	}
}