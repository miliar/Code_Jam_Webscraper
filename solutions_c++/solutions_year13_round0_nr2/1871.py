#include <iostream>
using namespace std;

const int MaxNM = 100;
int N, M;
int table[MaxNM][MaxNM];

int main() {
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 0; t < T; t ++) {
		cin >> N >> M;
		for (int i = 0; i < N; i ++)
			for (int j = 0; j < M; j ++)
				cin >> table[i][j];

		bool ans = true;
		for (int i = 0; i < N; i ++)
			for (int j = 0; j < M; j ++) {
				int cnt[2] = {0};
				for (int k = 0; k < N; k ++)
					cnt[0] += (table[k][j] <= table[i][j]);
				for (int k = 0; k < M; k ++)
					cnt[1] += (table[i][k] <= table[i][j]);
				ans &= (cnt[0] == N || cnt[1] == M);
			}

		cout << "Case #" << t + 1 << ": " << (ans ? "YES" : "NO") << endl;
	}

	return 0;
}

