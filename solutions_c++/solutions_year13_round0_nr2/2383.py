#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int board[111][111];

int main() {
	ios_base::sync_with_stdio(false);
	int T; cin >> T;
	for (int t = 0; t < T; t++) {
		int N, M; cin >> N >> M;
		memset(board, 0, sizeof(board));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				int val; cin >> val;
				board[i][j] = val;
			}
		}
		bool poss = true;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				// check if there is at least 1 way (horizontal/vertical s.t. there is no element larger than it - can be equal)
				bool noneBigger = true;
				for (int k = 0; k < M; k++) {
					if (board[i][k] > board[i][j]) {
						noneBigger = false;
						break;
					}
				}
				if (!noneBigger) {
					noneBigger = true;
					for (int k = 0; k < N; k++) {
						if (board[k][j] > board[i][j]) {
							noneBigger = false;
							break;
						}
					}
				}
				if (!noneBigger) {
					// either case
					poss = false;
					break;
				}
			}
			if (!poss) break;
		}
		cout << "Case #" << (t+1) << ": ";
		if (poss) cout << "YES\n"; else cout << "NO\n";
	}
	return 0;
}