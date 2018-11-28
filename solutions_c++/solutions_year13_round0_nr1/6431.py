#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <sstream>

#include <string.h>
#include <limits.h>
#include <stdio.h>

using namespace std;

int checkWinner(int cntA, int cntB, int cntT) {
	if (cntA == 4 || (cntA == 3 && cntT == 1)) {
		return 1;
	} else if ((cntB == 4 || (cntB == 3 && cntT == 1))) {
		return 2;
	}
	return 0;
}

int solve(vector<string> & mtx) {
	int countA;
	int countB;
	int countT;
	bool finished = true;
	for (int i = 0; i < 4; i++) { // check row
		countA = countB = countT = 0;
		for (int j = 0; j < 4; j++) {
			if (mtx[i][j] == '.') {
				finished = false;
			}
			if (mtx[i][j] == 'X') countA++;
			if (mtx[i][j] == 'O') countB++;
			if (mtx[i][j] == 'T') countT++;
		}
		int ret = checkWinner(countA, countB, countT);
		if (ret) return ret;
	}

	for (int i = 0; i < 4; i++) { // check col
		countA = countB = countT = 0;
		for (int j = 0; j < 4; j++) {
			if (mtx[j][i] == 'X') countA++;
			if (mtx[j][i] == 'O') countB++;
			if (mtx[j][i] == 'T') countT++;
		}
		int ret = checkWinner(countA, countB, countT);
		if (ret) return ret;
	}

	countA = countB = countT = 0;
	for (int i = 0; i < 4; i++) { // check diagonal
		if (mtx[i][i] == 'X') countA++;
		if (mtx[i][i] == 'O') countB++;
		if (mtx[i][i] == 'T') countT++;
	
		int ret = checkWinner(countA, countB, countT);
		if (ret) return ret;
	}

	countA = countB = countT = 0;
	for (int i = 0; i < 4; i++) { // check diagnoal
		if (mtx[i][3-i] == 'X') countA++;
		if (mtx[i][3-i] == 'O') countB++;
		if (mtx[i][3-i] == 'T') countT++;
	
		int ret = checkWinner(countA, countB, countT);
		if (ret) return ret;
	}

	if (finished) {
		return 3;
	} else {
		return 4;
	}
}
int main()
{
	vector<string> matrix;
	int N;
	int i = 1;
	cin >> N;
	// cout << N << endl;
	while (i <= N) {
		string tmp;
		for (int j = 0; j < 4; j++) {
			cin >> tmp;
			matrix.push_back(tmp);
			// cout << matrix[j] << endl;
		}
		int ret = solve(matrix);
		switch (ret) {
		case 1:
			printf("Case #%d: X won\n", i);
			break;
		case 2:
			printf("Case #%d: O won\n", i);
			break;
		case 3:
			printf("Case #%d: Draw\n", i);
			break;
		case 4:
			printf("Case #%d: Game has not completed\n", i);
			break;
		default:
			break;
		}
		i++;
		matrix.clear();
		// cin >> tmp;
	}
	return 0;
}
	
