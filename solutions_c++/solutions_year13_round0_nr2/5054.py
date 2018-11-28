#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

int isPossible(vector<vector<int> > lawn, int n, int m) {
	//find the maximum element per each row and column;
	int row[n];
	int column[m];
	for (int i = 0; i < n; i++) {
		row[i] = lawn[i][0];
		for (int j = 1; j < m; j++) {
			if (row[i] < lawn[i][j])
				row[i] = lawn[i][j];
		}
		cout << "maximum of row" << i << "is " << row[i] << endl;
	}

	for (int i = 0; i < m; i++) {
		column[i] = lawn[0][i];
		for (int j = 1; j < n; j++) {
			if (column[i] < lawn[j][i])
				column[i] = lawn[j][i];
		}
	}

	//check
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (100 - lawn[i][j] > (100 - row[i]) + (100 - column[j]))
				return 0;
			if (lawn[i][j] != row[i] && lawn[i][j] != column[j])
				return 0;
		}
	}
	return 1;
}

int main () {
	ifstream input;
	ofstream output;
	input.open("./B-large.in");
	//input.open("./test.in");
	//output.open("./B-small-practice.out");
	output.open("./test.out");

	int t = 0;

	input >> t;
	int n, m;
	int res;
	for (int i = 0; i < t; i++) {
		input >> n >> m;
		vector<vector<int> > lawn;
		for (int j = 0; j < n; j++) {
			vector<int> tmp(m);
			for (int k = 0; k < m; k++) {
				input >> tmp[k];
			}
			lawn.push_back(tmp);
		}
		res = isPossible(lawn, n, m);
		output << "Case #" << i + 1 << ": ";
		if (res == 1) {
			output << "YES\n";
		} else
			output << "NO\n";
	}
	input.close();
	output.close();
	return 0;
}