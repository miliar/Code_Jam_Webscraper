#include <iostream>
#include <fstream>
using namespace std;


int main() {

	ifstream fin("atxt.in");
	ofstream fout("atxt.out");

	int board[4][4], testcases, row;
	int guess1[4], guess2[4];

	fin >> testcases;
	for (int t=0; t<testcases; ++t) {
		fout << "Case #" << t + 1 << ": ";
		fin >> row;
		--row;
		for (int r=0; r<4; ++r) for (int c=0; c<4; ++c) {
			fin >> board[r][c];
		}
		for (int i=0; i<4; ++i) {
			guess1[i] = board[row][i];
		}
		fin >> row;
		--row;
		for (int r=0; r<4; ++r) for (int c=0; c<4; ++c) {
			fin >> board[r][c];
		}
		bool found = false;
		int ans = -1;
		for (int i=0; i<4; ++i) {
			for (int j=0; j<4; ++j) {
				if (board[row][i] == guess1[j]) {
					if (found) {
						fout << "Bad magician!" << endl;
						goto next;
					} else {
						ans = board[row][i];
						found = true;
					}
				}
			}
		}
		if (found) {
			fout << ans << endl;
		} else {
			fout << "Volunteer cheated!" << endl;
		}
next:   ;
	}

	return 0;
}