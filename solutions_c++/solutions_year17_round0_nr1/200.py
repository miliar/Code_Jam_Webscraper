#include <iostream>
#include <string>

using namespace std;

char flip(char c) {
	return (c == '+') ? '-' : '+';
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		string S;
		int K;
		int count = 0;
		cin >> S >> K;
		int N = S.size();
		for (int j = 0; j + K <= N; ++j) {
			if (S[j] == '-') {
				count++;
				for (int k = j; k < j + K; ++k) S[k] = flip(S[k]);
			}
		}
		bool done = true;
		for (int j = 0; j < N; ++j) {
			if (S[j] == '-') done = false;
		}
		if (done) {
			cout << "Case #" << i << ": " << count << endl;
		}
		else cout << "Case #" << i << ": IMPOSSIBLE" << endl;
	}
}