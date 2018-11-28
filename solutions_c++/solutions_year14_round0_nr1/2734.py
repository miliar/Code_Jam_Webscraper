#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

const int SIZE = 4;

int t;
int rows[2][SIZE];

vector<int> common;

int main() {
	cin >> t;
	for (int i = 0; i < t; ++i) {
		for (int j = 0; j < 2; ++j) {
			int rowNum;
			cin >> rowNum;
			for (int k = 0; k < SIZE; ++k) {
				int trash;
				if (k+1 == rowNum)
					for (int l = 0; l < SIZE; ++l)
						cin >> rows[j][l];
				else
					for (int l = 0; l < SIZE; ++l)
						cin >> trash;
			}
		}

		common.clear();
		sort(rows[0], rows[0]+SIZE);
		sort(rows[1], rows[1]+SIZE);
		int ia = 0, ib = 0;
		while (ia < SIZE && ib < SIZE) {
			if (rows[0][ia] == rows[1][ib]) {
				common.push_back(rows[0][ia]);
				ia++; ib++;
			}
			else if (rows[0][ia] < rows[1][ib])
				ia++;
			else
				ib++;
		}

		cout << "Case #" << i+1 << ": ";
		if (common.size() == 1)
			cout << common[0];
		else if (common.size() == 0)
			cout << "Volunteer cheated!";
		else
			cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}
