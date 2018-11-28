#include <iostream>
#include <queue>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		string S;
		int K;
		cin >> S >> K;

		int ans = 0, parity = 0;
		bool pos = true;
		queue<int> q;

		for (int i = 0; i < S.size(); i++) {
			if (!q.empty() && q.front() == i - K) {
				q.pop();
				parity--;
			}

			if (S[i] == '-' != parity % 2) {
				if (i <= S.size() - K) {
					q.push(i);
					ans++, parity++;
				} else {
					pos = false;
					break;
				}
			}
		}

		cout << "Case #" << t << ": " << (pos ? to_string(ans) : "IMPOSSIBLE") << endl;
	}

	return 0;
}