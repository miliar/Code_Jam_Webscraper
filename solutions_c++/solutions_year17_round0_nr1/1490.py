
#include <iostream>

using namespace std;

char op(char c) {
	return c == '+' ? '-' : '+';
}

void flip(string &s, int st, int len) {
	for (int i = st; i < st + len; i++) {
		s[i] = op(s[i]);
	}
}

int main() {
	int N;
	string S;
	int K;

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> S;
		cin >> K;

		// solve
		int flips = 0;
		for (int j = 0; j <= S.length() - K; j++) {
			if (S[j] == '-') {
				flips++;
				flip(S, j, K);
			}
		}
		bool p = true;
		for (int j = S.length() - K; j < S.length(); j++) {
			if (S[j] == '-') {
				p = false;
				break;
			}
		}
		cout << "Case #" << (i+1) << ": ";
		if (p) {
			cout << flips;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}

