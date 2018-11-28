#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int nCases;

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	
	fin >> nCases;
	for (int i = 1; i <= nCases; i ++) {
		int ans;
		int chose1[4], chose2[4];
		// first set
		fin >> ans;
		int buffer;
		for (int row = 1; row <= 4; row ++) {
			if (row == ans) {
				fin >> chose1[0] >> chose1[1] >> chose1[2] >> chose1[3];
			} else {
				fin >> buffer >> buffer >> buffer >> buffer;
			}
		}
		// second set
		fin >> ans;
		for (int row = 1; row <= 4; row ++) {
			if (row == ans) {
				fin >> chose2[0] >> chose2[1] >> chose2[2] >> chose2[3];
			} else {
				fin >> buffer >> buffer >> buffer >> buffer;
			}
		}
		ans = 0;
		int num = 0;
		// determine answer
		for (int j = 0; j < 4; j ++) {
			for (int k = 0; k < 4; k ++) {
				if (chose1[j] == chose2[k]) {
					num ++;
					ans = chose1[j];
				}
			}
		}
		fout << "Case #" << i << ": ";
		if (num == 0)
			fout << "Volunteer cheated!" << endl;
		else if (num == 1)
			fout << ans << endl;
		else
			fout << "Bad magician!" << endl;
	}
	
	return 0;
}
