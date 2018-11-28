#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

int T;
char mat[5][5];

bool judge(char c) {
	for (int i = 0; i < 4; ++i) {
		if (mat[i][0] == c && mat[i][1] == c && mat[i][2] == c && mat[i][3] == c)
			return true;
	}
	for (int i = 0; i < 4; ++i) {
		if (mat[0][i] == c && mat[1][i] == c && mat[2][i] == c && mat[3][i] == c)
			return true;
	}
	if (mat[0][0] == c && mat[1][1] == c && mat[2][2] == c && mat[3][3] == c)
		return true;
	if (mat[0][3] == c && mat[1][2] == c && mat[2][1] == c && mat[3][0] == c)
		return true;
	return false;
}
	
int main()
{
	cin >> T;
	for (int c = 1; c <= T; ++c) {
		bool fp, fx, fo;
		fp = fx = fo = false;
		
		for (int i = 0; i < 4; ++i) {
			cin >> mat[i];
		}

		int ti = 4, tj = 4;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (mat[i][j] == '.') {
					fp = true;
				}
				if (mat[i][j] == 'T') {
					ti = i;
					tj = j;
				}
			}
		}
		
		mat[ti][tj] = 'X';
		fx = judge('X');
		mat[ti][tj] = 'O';
		fo = judge('O');

		cout << "Case #" << c << ": ";
		if (fx) {
			cout << "X won";
		} else if (fo) {
			cout << "O won";
		} else if (!fp) {
			cout << "Draw";
		} else {
			cout << "Game has not completed";
		}

		cout << endl;
	}

	return 0;
}
