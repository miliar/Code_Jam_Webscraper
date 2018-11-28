#include <iostream>
#include <cstring>
using namespace std;

int T;
int N, M;
int h[101][101];

bool check() {
	for (int row = 1; row <= N; row++) {
		for (int column = 1; column <= M; column++) {
			if (h[row][column] < h[0][column] && h[row][column] < h[row][0])
				return false;
		}
	}
	return true;
}

int main() {
	cin >> T;
	for (int cases = 1; cases <= T; cases++) {
		cin >> N >> M;
		memset(h[0], 0, sizeof(int) * (M + 1));
		for (int row = 1; row <= N; row++) {
			h[row][0] = 0;
			for (int column = 1; column <= M; column++) {
				cin >> h[row][column];
				h[row][0] = max(h[row][0], h[row][column]);
				h[0][column] = max(h[0][column], h[row][column]);
			}
		}

		if (check())
			cout << "Case #" << cases << ": YES" << endl;
		else
			cout << "Case #" << cases << ": NO" << endl;

	}
	return 0;
}
