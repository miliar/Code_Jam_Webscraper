#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
using namespace std;

int N, M;
int target_lawn[100][100];
//int current_lawn[100][100];
/*
bool find_max(int *row_i, int *col_j, int current_max){
	bool res = false;
	for (int i = 0; (i < N) && !res; i++){
		for (int j = 0; (j < M) && !res; j++){
			if ((target_lawn[i][j] == current_max) &&
				(target_lawn[i][j] != current_lawn[i][j])){
				res = true;
				*row_i = i;
				*col_j = j;
			}
		}
	}
	return res;
}
*/
bool mow(int row_i, int col_j){
	// Check that the current location is not already target
	//if (current_lawn[row_i][col_j] == target_lawn[row_i][col_j])
	//	return true;
	int target = target_lawn[row_i][col_j];
	// Try to mow the row
	bool can_mow_row = true;
	for (int j = 0; j < M; j++){
		can_mow_row &= (target_lawn[row_i][j] <= target);
	}
	bool can_mow_col = true;
	for (int i = 0; i < N; i++){
		can_mow_col &= (target_lawn[i][col_j] <= target);
	}
	return can_mow_row || can_mow_col;
}

int main(){
	int T, case_num;
	cin >> T;
	for (case_num = 1; case_num <= T; ++case_num){
		//int current_max = 0;
		// Read in data, initialize current_lawn, and find largest num in target_lawn
		cin >> N >> M;
		for (int i = 0; i < N; i++){
			for (int j = 0; j < M; j++){
				cin >> target_lawn[i][j];
				//if (target_lawn[i][j] > current_max)
				//	current_max = target_lawn[i][j];
				//current_lawn[i][j] = 100;
			}
		}

		bool still_possible = true;
		// Try to find location of current_max
		/*int row_i, row_j;
		while (current_max > 0){
			while (find_max(&row_i, &col_j, current_max) && still_possible){
				still_possible = mow(row_i, col_j);
			}
			current_max--;
		}*/

		// Just try to mow every cell to see if possible...
		for (int i = 0; (i < N) && still_possible; i++){
			for (int j = 0; (j < M) && still_possible; j++){
				still_possible = mow(i, j);
			}
		}

		cout << "Case #" << case_num << ": ";
		if (still_possible)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}

