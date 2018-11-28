#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

char flip(char c) {
	return c == '+' ? '-' : '+';
}

void solve(int testcase) {
	string s;
	int K;
	cin >> s >> K;

	int ans = 0;
	const int n = s.size();
	for (int i = 0; i + K <= n; i++) {
		if (s[i] == '-') {
			for (int j = 0; j < K; j++) {
				s[i + j] = flip(s[i + j]);
			}
			ans++;
		}
	}

	if (s.find('-') == string::npos) {
		printf("Case #%d: %d\n", testcase, ans);
	} else {
		printf("Case #%d: IMPOSSIBLE\n", testcase, ans);
	}
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		solve(i + 1);
	}
}
