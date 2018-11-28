#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;


bool rfit(vvi &grid, vi list, int row) {
	//int i;
	//for (i = 0; i < list.size() && list[i] == grid[row][i]; i++);
	int N = list.size();
	for (int j = 0; j < list.size(); j++) {
		if ((row-1 >= 0 && grid[row-1][j] >= list[j])|| 
		(row+1 < N && grid[row+1][j] != -1 && grid[row+1][j] <= list[j])
		|| (grid[row][j] != -1 && grid[row][j] != list[j])) return false;
	}
	return true;
}

int cfit(vvi &grid, vi list, int col) {
	//int i;
	//for (i = 0; i < list.size() && list[i] == grid[col][i]; i++);
	int N = list.size();
	for (int j = 0; j < list.size(); j++) {
		if ((col-1 >= 0 && grid[j][col-1] >= list[j] )|| 
		(col+1 < N && grid[j][col+1] != -1 && grid[j][col+1] <= list[j])
		|| (grid[j][col] != -1 && grid[j][col] != list[j])) return false;
	}
	return true;
}

bool backtrack(vvi &grid, vvi &inputs, vb &filled) {
	int N = grid.size();
	if (inputs.empty()) return true;
	vi input = inputs.back();
	inputs.pop_back();
	for (int i = 0; i < N; i++) {
		if (!filled[i] && rfit(grid, input, i)) {
			vi state;
			for (int j = 0; j < N; j++) {
				state.push_back(grid[i][j]);
				grid[i][j] = input[j];
			}
			filled[i] = true;
			if (backtrack(grid, inputs, filled)) return true;
			for (int j = 0; j < N; j++) {
				grid[i][j] = state[j];
			}
			filled[i] = false;
		}
		if (!filled[i+N] && cfit(grid, input, i)) {
			vi state;
			for (int j = 0; j < N; j++) {
				state.push_back(grid[j][i]);
				grid[j][i] = input[j];
			}
			filled[i+N] = true;
			if (backtrack(grid, inputs, filled)) return true;
			for (int j = 0; j < N; j++) {
				grid[j][i] = state[j];
			}
			filled[i+N] = false;
		}
		
	}
	inputs.push_back(input);
	return false;
}

int main() {

	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		vvi grid(N, vi(N, -1));
		vvi inputs;
		vb filled(2 * N, false);
		for (int i = 0; i < 2*N-1; i++) {
			vi temp;
			for (int j = 0; j < N; j++) {
				int tem; cin >> tem;
				temp.push_back(tem);
			}
			inputs.push_back(temp);
		}
		backtrack(grid, inputs, filled);
		cout << "Case #" << t << ": ";
		for (int i = 0; i < filled.size(); i++) {
			if (!filled[i]) {
				if (i < N) {
					for (int j = 0; j < N; j++) {
						cout << grid[i][j] << " ";
					}
				} else {
					for (int j = 0; j < N; j++) {
						cout << grid[j][i-N] << " ";
					}
				}
			}
		}
		cout << endl;

	}

}
