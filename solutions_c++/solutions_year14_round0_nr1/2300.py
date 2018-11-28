#include <iostream>
#include <fstream>
using namespace std;

int t;
int ansQ1, ansQ2;
int rowQ1[4], rowQ2[4];

int main() {
	ifstream fi("in.txt");
	ofstream fo("out.txt");

	fi >> t;
	for (int i = 1; i <= t; i ++) {
		fi >> ansQ1;
		for (int j = 1; j <= ansQ1; j ++) {
			for (int k = 0; k < 4; k ++) {
				fi >> rowQ1[k];
			}
		}
		int tmp;
		for (int j = 1; j <= (4 - ansQ1) * 4; j ++) fi >> tmp;

		fi >> ansQ2;
		for (int j = 1; j <= ansQ2; j ++) {
			for (int k = 0; k < 4; k ++) {
				fi >> rowQ2[k];
			}
		}
		for (int j = 1; j <= (4 - ansQ2) * 4; j ++) fi >> tmp;

		fo << "Case #" << i <<": ";
		int card = 0;
		for (int i = 0; i < 4; i ++) {
			for (int j = 0; j < 4; j ++) {
				if (rowQ1[i] == rowQ2[j]) {
					if (!card) {
						card = rowQ1[i];
					} else {
						goto two;
					}
				}
			}
		}
		if (card) {
			fo << card << endl;
		} else {
			fo << "Volunteer cheated!" << endl;
		}
		continue;
two:
		fo << "Bad magician!" << endl;
	}
	return 0;
}