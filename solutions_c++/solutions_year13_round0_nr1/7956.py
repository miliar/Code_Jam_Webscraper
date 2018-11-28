#include<iostream>
#include<fstream>
using namespace std;
bool isLeftDiagonal(int i, int j) {
	if (i == 0 && j == 0)
		return true;
	if (i == 1 && j == 1)
		return true;
	if (i == 2 && j == 2)
		return true;
	if (i == 3 && j == 3)
		return true;
	return false;
}

bool isRightDiagonal(int i, int j) {
	if (i == 0 && j == 3)
		return true;
	if (i == 1 && j == 2)
		return true;
	if (i == 2 && j == 1)
		return true;
	if (i == 3 && j == 0)
		return true;
	return false;
}

bool isEqual(char a, char b, char c, char d) {
	if (a == 'T')
		if (b == c && c == d)
			return true;
	if (b == 'T')
		if (a == c && c == d)
			return true;
	if (c == 'T')
		if (a == b && b == d)
			return true;
	if (d == 'T')
		if (a == b && b == c)
			return true;
	if (a == b && b == c && c == d)
		return true;
	return false;
}

string solveProblem(char arr[][4]) {
	string result = "  won";
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (isLeftDiagonal(i, j)) {
				if (isEqual(arr[0][0], arr[1][1], arr[2][2], arr[3][3])) {
					if (arr[0][0] != '.') {
						result[0] = arr[0][0];
						return result;
					}
				}
			}
			if (isRightDiagonal(i, j)) {
				if (isEqual(arr[0][3], arr[1][2], arr[2][1], arr[3][0])) {
					if (arr[0][3] != '.') {
						result[0] = arr[0][3];
						return result;
					}
				}
			}
			if (isEqual(arr[0][j], arr[1][j], arr[2][j], arr[3][j])) {
				if (arr[0][j] != '.') {
					result[0] = arr[0][j];
					return result;
				}
			}
			if (isEqual(arr[i][0], arr[i][1], arr[i][2], arr[i][3])) {
				if (arr[i][0] != '.') {
					result[0] = arr[i][0];
					return result;
				}
			}
		}
	}
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			if (arr[i][j] == '.')
				return "Game has not completed";
		}
	}
	return "Draw";
}

int main() {
	fstream f, fout;
	f.open("A-small-attempt2.in", ios::in);
	fout.open("A-small-attempt2.out", ios::out);
	int nOfCases, x = 0;
	f >> nOfCases;
	cout << nOfCases <<endl;
	char arr[4][4];
	while (x < nOfCases) {
		f >> arr[0][0];
		f >> arr[0][1];
		f >> arr[0][2];
		f >> arr[0][3];
		f >> arr[1][0];
		f >> arr[1][1];
		f >> arr[1][2];
		f >> arr[1][3];
		f >> arr[2][0];
		f >> arr[2][1];
		f >> arr[2][2];
		f >> arr[2][3];
		f >> arr[3][0];
		f >> arr[3][1];
		f >> arr[3][2];
		f >> arr[3][3];
		fout << "Case #" << ++x<<": ";
		fout << solveProblem(arr) << endl;
	}
	f.close();
	fout.close();
	return 0;
}
