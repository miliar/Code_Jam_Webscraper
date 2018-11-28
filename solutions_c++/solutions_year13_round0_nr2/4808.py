#include <algorithm>
#include <stdio.h>
#include <vector>

using namespace std;

int GetMaxInARow(const vector<vector<int> >& data, int i) {
	if (data[i].size () == 0) {
		return 0;
	}

	int maxVal = data[i][0];
	for (int j = 1; j < data[i].size (); ++j) {
		maxVal = max (maxVal, data[i][j]);
	}

	return maxVal;
}

int GetMaxInACol(const vector<vector<int> >& data, int j) {
	if (data.size () == 0) {
		return 0;
	}

	int maxVal = data[0][j];
	for (int i = 1; i < data.size (); ++i) {
		maxVal = max (maxVal, data[i][j]);
	}

	return maxVal;
}

int main() {
	FILE *fin, *fout;

	fin = fopen ("input.txt", "r");
	fout = fopen ("output.txt", "w");

	int T;
	fscanf (fin, "%d", &T);

	for (int t = 1; t <= T; ++t) {
		int N, M;
		fscanf (fin, "%d %d", &N, &M);

		vector<vector<int> > data (N, vector<int> (M));
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < M; ++j) {
				fscanf (fin, "%d", &data[i][j]);
			}
		}

		bool possible = true;

		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < M; ++j) {
				if (GetMaxInARow (data, i) != data[i][j] && GetMaxInACol (data, j) != data[i][j]) {
					possible = false;
					break;
				}
			}
			if (!possible) {
				break;
			}
		}

		fprintf (fout, "Case #%d: %s\n", t, (possible ? "YES" : "NO"));
	}

	fclose (fin);
	fclose (fout);

	return 0;
}
