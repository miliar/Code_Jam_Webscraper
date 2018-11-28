#include <iostream>
#include <fstream>
using namespace std;

#define cin fin
#define cout fout
ifstream fin("B-large.in");
ofstream fout("B-large.out");
const int MAXN = 100;
int field[MAXN][MAXN];
int height[MAXN][MAXN];
int rowMax[MAXN], colMax[MAXN];
int row, col;

void cutRow(int r, int n) {
	for (int i = 0; i < col; i++)
		height[r][i] = min(height[r][i], n);
}

void cutCol(int c, int n) {
	for (int i = 0; i < row; i++)
		height[i][c] = min(height[i][c], n);
}

bool isSame() {
	for (int i = 0; i < row; i++)
		for (int k = 0; k < col; k++)
			if (field[i][k] != height[i][k])
				return false;

	return true;
}

void cutGross() {
	for (int i = 0; i < row; i++)
		for (int k = 0; k < col; k++)
			height[i][k] = 100;

	for (int i = 0; i < row; i++)
		cutRow(i, rowMax[i]);

	for (int k = 0; k < col; k++)
		cutCol(k, colMax[k]);
}

int main() {
	int nCases;
	cin >> nCases;

	for (int cnt = 1; cnt <= nCases; cnt++) {
		cin >> row >> col;

		memset(rowMax, 0, sizeof(rowMax));
		memset(colMax, 0, sizeof(colMax));

		for (int i = 0; i < row; i++)
			for (int k = 0; k < col; k++) {
				cin >> field[i][k];
				rowMax[i] = max(rowMax[i], field[i][k]);
				colMax[k] = max(colMax[k], field[i][k]);
			}

		cutGross();
		cout << "Case #" << cnt << ": ";
		if (isSame())
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}

	return 0;
}
