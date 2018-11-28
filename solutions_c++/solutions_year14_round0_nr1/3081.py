#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int inputs;
	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.out");
	fin >> inputs;
	for (int i = 0; i < inputs; i++) {
		int rownum, cardid, firstrow[4], secondrow[4], matches = 0;
		fin >> rownum;
		for (int j = 0; j < 4; j++) {
			fin >> cardid;
			if (rownum == 1) firstrow[j] = cardid;
		}
		for (int j = 0; j < 4; j++) {
			fin >> cardid;
			if (rownum == 2) firstrow[j] = cardid;
		}
		for (int j = 0; j < 4; j++) {
			fin >> cardid;
			if (rownum == 3) firstrow[j] = cardid;
		}
		for (int j = 0; j < 4; j++) {
			fin >> cardid;
			if (rownum == 4) firstrow[j] = cardid;
		}
		fin >> rownum;
		for (int j = 0; j < 4; j++) {
			fin >> cardid;
			if (rownum == 1) secondrow[j] = cardid;
		}
		for (int j = 0; j < 4; j++) {
			fin >> cardid;
			if (rownum == 2) secondrow[j] = cardid;
		}
		for (int j = 0; j < 4; j++) {
			fin >> cardid;
			if (rownum == 3) secondrow[j] = cardid;
		}
		for (int j = 0; j < 4; j++) {
			fin >> cardid;
			if (rownum == 4) secondrow[j] = cardid;
		}

		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (firstrow[j] == secondrow[k]) {
					cardid = firstrow[j];
					matches++;
				}
			}
		}
		if (matches == 0) {
			fout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
		}
		if (matches == 1) {
			fout << "Case #" << i + 1 << ": " << cardid << endl;
		}
		if (matches > 1) {
			fout << "Case #" << i + 1 << ": Bad magician!" << endl;
		}
	}
}