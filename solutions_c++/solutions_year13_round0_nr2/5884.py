#include<iostream>
using namespace std;
bool check(int row, int col, int sourceRow, int sourceCol);
bool checkSource(int row, int col);
int source[10][10];

int main() {
	int sum;
	cin >> sum;
	for(int i = 0; i < sum; i++) {	
		int N, M;
		cin >> N >> M;

		for(int a = 0; a < N; a++) {
			for(int b = 0; b < M; b++) {
				cin >> source[a][b];
			}
		}

		if(checkSource(N, M)) {
			cout << "Case #" << i + 1 << ":" << " YES" << endl;
		}else {
			cout << "Case #" << i + 1 << ":" << " NO" << endl;
		}
	}
	return 0;
}

bool check(int row, int col, int sourceRow, int sourceCol) {
	bool isMax = true, rowMax = true;
	for(int i = 0; i < sourceRow; i++) {
		if(source[i][col] > 1) {
			rowMax = false;
		}
	}
	if(!rowMax) {
		for(int i = 0; i < sourceCol; i++) {
			if(source[row][i] > 1) {
				isMax = false;
			}
		}
	}

	return isMax;
}

bool checkSource(int row, int col) {
	for(int a = 0; a < row; a++) {
		for(int b = 0; b < col; b++) {
			if(source[a][b] == 1) {
				if(check(a, b, row, col) == false) {
					return false;
				}
			}
		}
	}
	return true;
}
