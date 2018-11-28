#include <bits/stdc++.h>
using namespace std;

int T, N;
int grid[52][52];
vector <vector<int>> L;
int res[52];

int skipped_row = -1;
int skipped_col = -1;
bool found;

void go(int index, int R, int C) {
	if (found) return;

	if (index == 2*N-1) {
		if (skipped_row == -1 && skipped_col == -1) {
			if (C < N) skipped_col = N-1;
			else if (R < N) skipped_row = N-1;
		}
		if (skipped_row > -1) {
			for (int c=0; c<N; c++)
				res[c] = grid[skipped_row][c];
		} else {
			for (int r=0; r<N; r++)
				res[r] = grid[r][skipped_col];
		}
		found = true;
	} else {
		// put on a row
		bool ok = true;
		if (R < N) {
			for (int c=0; c<N; c++)
				if (!(grid[R][c] == 0 && (R == 0 || grid[R-1][c] < L[index][c]) 
					|| grid[R][c] == L[index][c]))
				{
					ok = false;
					break;
				}
			if (ok) {
				int store[52];
				for (int c=0; c<N; c++) {
					store[c] = grid[R][c];
					grid[R][c] = L[index][c];
				}
				go(index+1, R+1, C);
				for (int c=0; c<N; c++) 
					grid[R][c] = store[c];
			}
		}

		// put on a column
		ok = true;
		if (C < N) {
			for (int r=0; r<N; r++)
				if (!(grid[r][C] == 0 && (C == 0 || grid[r][C-1] < L[index][r]) 
					|| grid[r][C] == L[index][r]))
				{
					ok = false;
					break;
				}
			if (ok) {
				int store[52];
				for (int r=0; r<N; r++) {
					store[r] = grid[r][C];
					grid[r][C] = L[index][r];
				}
				go(index+1, R, C+1);
				for (int r=0; r<N; r++) 
					grid[r][C] = store[r];
			}
		}
	
		if (skipped_row == -1 && skipped_col == -1) {
			skipped_row = R;
			go(index, R+1, C);
			skipped_row = -1;
			skipped_col = C;
			go(index, R, C+1);
			skipped_col = -1;
		}
	}
}

int main() {
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> N;
		L.resize(2*N-1);
		for (int i=0; i<2*N-1; i++) {
			L[i].resize(N);
			for (int j=0; j<N; j++)
				cin >> L[i][j];
		}
		sort(L.begin(), L.end());
		memset(grid, 0, sizeof(grid));
		skipped_row = -1;
		skipped_col = -1;
		found = false;
		go(0, 0, 0);

		cout << "Case #" << t << ":";
		for (int i=0; i<N; i++)
			cout << " " << res[i];
		cout << endl;
	}
}
