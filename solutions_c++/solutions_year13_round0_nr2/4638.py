#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        cout << "Case #" << (t+1) << ":";
		int N;
		cin >> N;
		int M;
		cin >> M;
		
		int lawn[N][M];
		int max_in_row[N];
		int max_in_column[M];
		
		for (int i = 0; i < N; i++) {
			max_in_row[i] = 0;
			for (int j = 0; j < M; j++) {
				cin >> lawn[i][j];
				if (max_in_row[i] < lawn[i][j]) max_in_row[i] = lawn[i][j];
			}
		}

		for (int j = 0; j < M; j++) {
			max_in_column[j] = 0;
			for (int i = 0; i < N; i++) {
				if (max_in_column[j] < lawn[i][j]) max_in_column[j] = lawn[i][j];
			}
		}
		
		bool possible = true;
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (lawn[i][j] < max_in_row[i] && lawn[i][j] < max_in_column[j]) {
					possible = false; break;
				}
			}
			if (!possible) break;
		}
		if (possible) cout << " YES"; else cout << " NO";
		cout << endl;
	}
}
