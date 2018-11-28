#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int N, M;
		cin >> N >> M;
		int height[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				cin >> height[i][j];
			}
		}

		bool possible = true;
		for (int i = 0; possible && i < N; i++) {
			for (int j = 0; j < M; j++) {
				bool p = true;

				// row
				for (int k = 0; p && k < N; k++) {
					if (height[i][j] < height[k][j]) {
						p = false;
					}
				}

				// col
				if (!p) {
					p = true;
					for (int k = 0; p && k < M; k++) {
						if (height[i][j] < height[i][k]) {
							p = false;
						}
					}
				}
				
				possible = possible && p;
			}
		}

		cout << "Case #" << t+1 << ": " << (possible ? "YES" : "NO") << endl;
	}
}
