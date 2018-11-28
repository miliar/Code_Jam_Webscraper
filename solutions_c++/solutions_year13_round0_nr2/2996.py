#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main() {
	int T, N, M;
	cin >> T;

	int h[100][100];
	for (int t=1; t<=T; t++) {
		cin >> N >> M;
		for (int i=0; i<N; i++)
			for (int j=0; j<M; j++)
				cin >> h[i][j];

		int row[100], col[100];
		for (int i=0; i<N; i++) {
			int max = 0;
			for (int j=0; j<M; j++)
				if (h[i][j]>max) max=h[i][j];
			row[i] = max;
		}
		for (int j=0; j<M; j++) {
			int max = 0;
			for (int i=0; i<N; i++)
				if (h[i][j]>max) max=h[i][j];
			col[j] = max;
		}

		bool possible = true;
		for (int j=0; j<M; j++) {
			for (int i=0; i<N; i++)
				if (h[i][j]<row[i] && h[i][j]<col[j]) { possible=false; break; }
			if (!possible) break;
		}

		cout << "Case #" << t << ": " << (possible? "YES":"NO") << endl;
	}
	return 0;
}


