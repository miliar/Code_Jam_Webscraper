#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt0.in");
	fout.open("output.txt");

	int N;
	fin >> N;

	for (int i = 1; i <= N; i++) {
		int Line1, Line2;
		int Card[16] = { 0, }, CardInput[16] = { 0, };
		fin >> Line1;
		for (int j = 0; j < 16; j++) {
			fin >> CardInput[j];
			if (j >= (Line1 - 1) * 4 && j < Line1 * 4) Card[CardInput[j] - 1] = 1;
		}
		fin >> Line2;
		int Case = 0, count = 0;
		for (int j = 0; j < 16; j++) {
			fin >> CardInput[j];
			if (j >= (Line2 - 1) * 4 && j < Line2 * 4) {
				if (Card[CardInput[j] - 1] == 1) {
					Case = CardInput[j];
					count++;
				}
			}
		}
		fout << "Case #" << i << ": ";
		if (count > 1) fout << "Bad magician!";
		else if (count == 1) fout << Case;
		else fout << "Volunteer cheated!";
		fout << "\n";
	}
	return 0;
}