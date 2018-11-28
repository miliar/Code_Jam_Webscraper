#include <iostream>
#include <cstdio>
#include <sstream>

using namespace std;
typedef pair<int, int> P;

int field[11][11];
int used[11][11];
int N, M;

int main() {
	int T; scanf("%d", &T);
	stringstream ss;

	for (int i = 0; i < T; i++) {
		ss << "Case #" << i+1 << ": ";

		scanf("%d %d", &N, &M);
		for (int j = 0; j < N; j++) {
			for (int k = 0; k < M; k++) scanf("%d", &field[j][k]);
		}

		int res = 1;
		for (int h = 1; h < 100; h++) {
			for (int j = 0; j < N; j++) {
				for (int k = 0; k < M; k++) used[j][k] = 0;
			}

			for (int j = 0; j < M; j++) {
				int flg  = 1;
				for (int k = 0; k < N; k++) {
					if (field[k][j] > h) flg = 0;
				}
				if (flg) {
					for (int k = 0; k < N; k++) used[k][j] = 1;
				}
			}
			for (int j = 0; j < N; j++) {
				int flg = 1;
				for (int k = 0; k < M; k++) {
					if (field[j][k] > h) flg = 0;
				}
				if (flg) {
					for (int k = 0; k < M; k++) used[j][k] = 1;
				}
			}

			for (int j = 0; j < N; j++) {
				for (int k = 0; k < M; k++) {
					if (used[j][k] == 0 && field[j][k] == h) {
						res = 0;
					}
				}
			}
		}

		if (res) ss << "YES" << endl;
		else ss << "NO" << endl;
	}
	cout << ss.str();
	return 0;
}
