#include <fstream>
#include <iostream>

using namespace std;

int main() {
	ifstream fin;
	fin.open("A-small-attempt0.in", ifstream::in);
	ofstream fout;
	fout.open("A.out", ofstream::out);
	int cases;
	int row_1, row_2;
	int count, tmp;
	int A[4][4], B[4][4];
	fin >> cases;
	for(int i = 0; i < cases; ++i) {
		fin >> row_1;
		for(int j = 0; j < 4; ++j) {
			for(int k = 0; k < 4; ++k) {
				fin >> A[j][k];
			}
		}
		fin >> row_2;
		for(int j = 0; j < 4; ++j) {
			for(int k = 0; k < 4; ++k) {
				fin >> B[j][k];
			}
		}
		count = 0;
		for(int j = 0; j < 4; ++j) {
			for(int k = 0; k < 4; ++k) {
				if(A[row_1-1][j] == B[row_2-1][k]) {
					count++;
					tmp = A[row_1-1][j];
				}
			}
		}
		if(count == 1) {
			fout << "Case #" << i+1 << ": " << tmp << endl;
		} else if(count == 0) {
			fout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
		} else {
			fout << "Case #" << i+1 << ": Bad magician!" << endl;
		}
	}

}