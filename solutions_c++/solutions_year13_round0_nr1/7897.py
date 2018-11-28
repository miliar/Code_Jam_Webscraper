#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
	ifstream fin ("A-large.in");
	ofstream fout ("output.out");
	int cases;
	vector<vector<int> > board(4, vector<int>(4));
	
	fin >> cases;
	
	for (int i = 0; i < cases; ++i) {
		bool finished = 1;
		char temp;
		for (int j = 0; j < 4; ++j) { 
			for (int k = 0; k < 4; ++k) {
				fin >> temp;
				if (temp == 'O') {
					board[j][k] = -1;
				} else if (temp == 'X') {
					board[j][k] = 1;
				} else if (temp == 'T') {
					board[j][k] = 0;
				} else {
					board[j][k] = 1000;
					finished = 0;
				}
			}
		}
		
		int test1, test2;
		bool complete = 1;
		for (int j = 0; j < 4; ++j) {
			test1 = board[j][0] + board[j][1] + board[j][2] + board[j][3];
			test2 = board[0][j] + board[1][j] + board[2][j] + board[3][j];
			if (test1 == -3 || test1 == -4 || test2 == -3 || test2 == -4) {
				fout << "Case #" << i + 1 << ": O won\n";
				complete = 0;
				break;
			} else if (test1 == 3 || test1 == 4 || test2 == 3 || test2 == 4) {
				fout << "Case #" << i + 1 << ": X won\n";
				complete = 0;
				break;
			}
		}
		if (complete) {
			test1 = board[0][0] + board[1][1] + board[2][2] + board[3][3];
			test2 = board[0][3] + board[1][2] + board[2][1] + board[3][0];
			if (test1 == -3 || test1 == -4 || test2 == -3 || test2 == -4) {
				fout << "Case #" << i + 1 << ": O won\n";
				complete = 0;
			} else if (test1 == 3 || test1 == 4 || test2 == 3 || test2 == 4) {
				fout << "Case #" << i + 1 << ": X won\n";
				complete = 0;
			}
		}
		
		if (complete) {
			if (finished) {
				fout << "Case #" << i + 1 << ": Draw\n";
			} else {
				fout << "Case #" << i + 1 << ": Game has not completed\n";
			}
		}
	}
	return 0;
}
