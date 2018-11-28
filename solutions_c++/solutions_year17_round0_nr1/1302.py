#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		char S[1001];
		int C[1001];
		int K;
		cin >> S >> K;
		int sz = strlen(S);
		for (int i = 0; i < sz; i++) C[i] = (S[i] == '+' ? 1 : 0);
		int res = 0;
		for (int i = 0; i <= sz - K; i++) {
			if (!C[i]) {
				int sz2 = i + K;
				for (int h = i; h < sz2; h++) {
					C[h] = !C[h];
				}
				res++;
			}
		}
		for (int i = sz - K + 1; i < sz; i++) {
			if (!C[i]) {
				res = -1;
				break;
			}
		}
		if (res < 0) {
			cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << t << ": " << res << endl;
		}
	}

	return 0;
}
