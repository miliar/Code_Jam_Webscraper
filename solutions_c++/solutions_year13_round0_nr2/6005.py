#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int k = 0; k < T; k++) {
		int N, M;
		cin >> N >> M;
		int arr[100][100];

		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++) {
				cin >> arr[i][j];
			}

		bool res = true;
		for (int i = 0; i < N && res; i++) {
			for (int j = 0; j < M && res; j++) {
				if (arr[i][j] == 2)
					continue;
				else {
					int ti = 0;
					for (; ti < N; ti++) {
						if (arr[ti][j] != 1)
							break;
					}
					if (ti == N) {
						continue;
					}

					int tj = 0;
					for (; tj < M; tj++) {
						if (arr[i][tj] != 1)
							break;
					}
					if (tj == M) {
						continue;
					}

					res = false;
				}
			}
		}
		cout << "Case #" << (k + 1) << ": ";
		if (res) {
			cout << "YES" << endl;
		} else {
			cout << "NO" << endl;
		}
	}
}
