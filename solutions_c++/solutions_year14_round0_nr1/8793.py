//============================================================================
// Name        : gcj2014.cpp
// Author      : rajappan
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <fstream>
using namespace std;

int main() {
	int T;
	ifstream infile(
			"/home/grad06/rajappan/workspace/gcj2014/src/A-small-attempt1.in");
	ofstream outfile(
			"/home/grad06/rajappan/workspace/gcj2014/src/A-small-output1.out");
	if (!infile) {
		cout << "Error opening file!" << endl;
		exit(1);
	}
	infile >> T;
	cout << T << endl;
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		int ans[2];
		vector<int> v[2];
		for (int i = 0; i < 2; ++i) {
			infile >> ans[i];
			for (int j = 0; j < 4; ++j) {
				for (int k = 0; k < 4; ++k) {
					int tmp;
					infile >> tmp;
					if (j == (ans[i] - 1)) {
						v[i].push_back(tmp);
					}
				}
			}
			sort(v[i].begin(), v[i].end());
		}
		// find the intersection of two sets
		vector<int> v_intersection;

		std::set_intersection(v[0].begin(), v[0].end(), v[1].begin(),
				v[1].end(), std::back_inserter(v_intersection));
		outfile << "Case #" << caseNum << ": ";
		cout << "Case #" << caseNum << ": ";
		if (v_intersection.size() == 1) {
			outfile << v_intersection[0] << endl;
			cout << v_intersection[0] << endl;
		} else if (v_intersection.size() > 1) {
			outfile << "Bad magician!" << endl;
			cout << "Bad magician!" << endl;
		} else {
			outfile << "Volunteer cheated!" << endl;
			cout << "Volunteer cheated!" << endl;
		}
	}
	infile.close();
	outfile.close();
	return 0;
}
