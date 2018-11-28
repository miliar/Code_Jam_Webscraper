#include <iostream>
#include <fstream>
#include <set>
using namespace std;
int main() {
	int n;
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt0.in");
	fout.open("A-small-attempt0.out");
	fin >> n;
	int answer1, answer2;
	set<int> row;
	int dummy;
	int count;
	int ret;
	for (int z = 0; z < n; z++) {
		count = 0;
		row.clear();
		fin >> answer1;
		for(int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				fin >> dummy;
				if (i == answer1 - 1) {
					row.insert(dummy);
				}
			}
		}
		fin >> answer2;
		for(int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				fin >> dummy;
				if (i == answer2 - 1 ) {
					if (row.find(dummy) != row.end()) {
						count++;
						ret = dummy;
					}
				}
			}
		}
		fout << "Case #" << z+1 << ": ";
		switch (count) {
		case 0: fout << "Volunteer cheated!"; break;
		case 1: fout << ret; break;
		default: fout << "Bad magician!"; 
		}
		fout << endl;
	}
}