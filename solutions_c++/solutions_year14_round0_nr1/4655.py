#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

/**
	Google Code Jam
	Qualification Round 2014
	Problem A. Magic Trick

	https://code.google.com/codejam/contest/2974486/dashboard#s=p0
*/

void read_next_testcase(ifstream &in, int &row1, int &row2,
	vector<vector<int> > &config1, vector<vector<int> > &config2
) {
	in >> row1;
	for (int i = 0; i < 4; ++ i) {
		vector<int> row(4);
		for (int j = 0; j < 4; ++ j) {
			in >> row[j];
		}
		config1.push_back(row);
	}

	in >> row2;
	for (int i = 0; i < 4; ++ i) {
		vector<int> row(4);
		for (int j = 0; j < 4; ++ j) {
			in >> row[j];
		}
		config2.push_back(row);
	}
}

void solve_next_testcase(ifstream &in, ofstream &out, int case_nr) {
	int row1, row2;
	vector<vector<int> > config1, config2;
	read_next_testcase(in, row1, row2, config1, config2);
	row1 --;
	row2 --;

	map<int, bool> seen;
	for (int i = 0; i < 4; ++ i) {
		seen[config1[row1][i]] = true;
	}
	int cnt = 0, solution_index = -1;
	for (int i = 0; i < 4; ++ i) {
		if (seen[config2[row2][i]] == true) {
			cnt ++;
			solution_index = i;
		}
	}
	switch(cnt) {
		case 0:
			out << "Case #" << case_nr << ": Volunteer cheated!" << endl;
			break;
		case 1:
			out << "Case #" << case_nr << ": " << config2[row2][solution_index] << endl;
			break;
		default:
			out << "Case #" << case_nr << ": Bad magician!" << endl;
			break;
	}
}

int main () {
	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in");
	out.open("output-small.txt");

	int T;
	in >> T;
	int case_nr = 0;
	while (case_nr ++ < T)
		solve_next_testcase(in, out, case_nr);

    in.close();
    out.close();
	return 0;
}