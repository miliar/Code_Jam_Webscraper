#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int t;
int n1, n2;
int arrange1[4][4];
int arrange2[4][4];

int main() {
	//ifstream fin ("A-small-attempt2.in");
	ifstream fin ("A-small-attempt3.in");
	ofstream fout ("magic_trick.out");
	fin >> t;
	for (int i = 1; i <= t; i++) {
		fin >> n1;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				fin >> arrange1[j][k];
			}
		}
		fin >> n2;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				fin >> arrange2[j][k];
			}
		}
		int ans = -1;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (arrange1[n1-1][j] == arrange2[n2-1][k]) {
					if (ans == -1 || ans == arrange1[n1-1][j]) {
						ans = arrange1[n1-1][j];
					}
					else
						ans = -2;
				}
			}
		}
		switch (ans) {
		case -1:
			fout << "Case #" << i << ": Volunteer cheated!" << endl;
			break;
		case -2:
			fout << "Case #" << i << ": Bad magician!" << endl;
			break;
		default:
			fout << "Case #" << i << ": " << ans << endl;
		}
	}
}
