#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	ifstream fin("A-small-attempt0.in.txt");
	ofstream fout("magictrick.out");

	int t;
	fin >> t;

	for(int tc = 1; tc <= t; tc++) {
		int cards[16];
		fill(cards, cards+16, 0);

		int l1[4][4], l2[4][4];
		int a1, a2;

		fin >> a1;
		for(int i = 0; i < 4; i++) for(int j = 0; j < 4; j++) fin >> l1[i][j];
		fin >> a2;
		for(int i = 0; i < 4; i++) for(int j = 0; j < 4; j++) fin >> l2[i][j];

		for(int j = 0; j < 4; j++) cards[l1[a1-1][j]-1]++;
		for(int j = 0; j < 4; j++) cards[l2[a2-1][j]-1]++;

		int twoc = 0, twoi = -1; bool bad = false; string res = "";
		for(int i = 0; i < 16 && !bad; i++) {
			if(cards[i] == 2) {
				if(twoc >= 1) {
					bad = true;
					res = "Bad magician!";

				} else {
					twoc += 1;
					twoi = i;
				}
			}

			if(i == 15 && twoc == 0) {
				bad = true;
				res = "Volunteer cheated!";
			}
		}

		if(!bad) {
			fout << "Case #" << tc << ": " << (twoi + 1) << "\n";
		} else {
			fout << "Case #" << tc << ": " << res << "\n";
		}
	}

	return 0;
}
