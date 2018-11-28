

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int T;
//int matrix[4][4];
int row_idx1, row_idx2;
vector<int> row1, row2;

int main()
{
	int val;
	//istream &in = cin;
	istream &in = ifstream("in.txt");
	//ostream &out = cout;
	ostream &out = ofstream("out.txt");
	in >> T;
	for (int i = 0; i < T; ++i) {
		int same = 0;
		int same_cnt = 0;
		in >> row_idx1;
		--row_idx1;
		row1.clear();
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				in >> val;
				if (j == row_idx1)
					row1.push_back(val);
			}
		}

		in >> row_idx2;
		--row_idx2;
		//row2.clear();
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				in >> val;
				if (j == row_idx2) {
					//row2.push_back(val);
					for (int m = 0; m < 4; ++m) {
						if (row1[m] == val) {
							same = val;
							++same_cnt;
							break;
						}
					}
				}
			}
		}
		out << "Case #" << (i + 1) << ": ";
		if (same_cnt == 0) {
			out << "Volunteer cheated!" << endl;
		}
		else if (same_cnt == 1) {
			out << same << endl;
		}
		else {
			out << "Bad magician!" << endl;
		}

	}
	return 0;
}