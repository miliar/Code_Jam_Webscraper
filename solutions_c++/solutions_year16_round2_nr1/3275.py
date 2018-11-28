#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <array>

using namespace std;

int main() {
	ifstream infile("a.in");
	if (!infile.is_open()) {
		cout << "Where's the file dude?";
		return 0;
	}

	ofstream outfile;
	outfile.open("output.txt");

	int n; //# of testcases
	infile >> n;
	string oneline;
	int cursor;

	for (int a0 = 0; a0 < n; a0++) {
		infile >> oneline;
		array<int, 10> tmp = { 0,0,0,0,0,0,0,0,0,0 };

		for (int a1 = 0; a1 < 1; a1++) {
			while (oneline.find("Z") >= 0 && oneline.find("Z") <= oneline.size()) {
				cursor = oneline.find("Z");
				oneline.erase(cursor,1);
				cursor = oneline.find("E");
				oneline.erase(cursor,1);
				cursor = oneline.find("R");
				oneline.erase(cursor,1);
				cursor = oneline.find("O");
				oneline.erase(cursor,1);
				tmp[0]++;
			}
			while (oneline.find("W") >= 0 && oneline.find("W") <= oneline.size()) {
				cursor = oneline.find("W");
				oneline.erase(cursor,1);
				cursor = oneline.find("T");
				oneline.erase(cursor,1);
				cursor = oneline.find("O");
				oneline.erase(cursor,1);
				tmp[2]++;
			}
			while (oneline.find("X") >= 0 && oneline.find("X") <= oneline.size()) {
				cursor = oneline.find("X");
				oneline.erase(cursor,1);
				cursor = oneline.find("S");
				oneline.erase(cursor,1);
				cursor = oneline.find("I");
				oneline.erase(cursor,1);
				tmp[6]++;
			}
			while (oneline.find("G") >= 0 && oneline.find("G") <= oneline.size()) {
				cursor = oneline.find("G");
				oneline.erase(cursor,1);
				cursor = oneline.find("E");
				oneline.erase(cursor,1);
				cursor = oneline.find("I");
				oneline.erase(cursor,1);
				cursor = oneline.find("H");
				oneline.erase(cursor,1);
				cursor = oneline.find("T");
				oneline.erase(cursor,1);
				tmp[8]++;
			}
			while (oneline.find("H") >= 0 && oneline.find("H") <= oneline.size()) {
				cursor = oneline.find("H");
				oneline.erase(cursor,1);
				cursor = oneline.find("T");
				oneline.erase(cursor,1);
				cursor = oneline.find("R");
				oneline.erase(cursor,1);
				cursor = oneline.find("E");
				oneline.erase(cursor,1);
				cursor = oneline.find("E");
				oneline.erase(cursor,1);
				tmp[3]++;
			}
			while (oneline.find("U") >= 0 && oneline.find("U") <= oneline.size()) {
				cursor = oneline.find("U");
				oneline.erase(cursor,1);
				cursor = oneline.find("F");
				oneline.erase(cursor,1);
				cursor = oneline.find("O");
				oneline.erase(cursor,1);
				cursor = oneline.find("R");
				oneline.erase(cursor,1);
				tmp[4]++;
			}
			while (oneline.find("O") >= 0 && oneline.find("O") <= oneline.size()) {
				cursor = oneline.find("O");
				oneline.erase(cursor,1);
				cursor = oneline.find("N");
				oneline.erase(cursor,1);
				cursor = oneline.find("E");
				oneline.erase(cursor,1);
				tmp[1]++;
			}
			while (oneline.find("F") >= 0 && oneline.find("F") <= oneline.size()) {
				cursor = oneline.find("F");
				oneline.erase(cursor,1);
				cursor = oneline.find("I");
				oneline.erase(cursor,1);
				cursor = oneline.find("V");
				oneline.erase(cursor,1);
				cursor = oneline.find("E");
				oneline.erase(cursor,1);
				tmp[5]++;
			}
			while (oneline.find("V") >= 0 && oneline.find("V") <= oneline.size()) {
				cursor = oneline.find("V");
				oneline.erase(cursor,1);
				cursor = oneline.find("S");
				oneline.erase(cursor,1);
				cursor = oneline.find("E");
				oneline.erase(cursor,1);
				cursor = oneline.find("E");
				oneline.erase(cursor,1);
				cursor = oneline.find("N");
				oneline.erase(cursor,1);
				tmp[7]++;
			}
			while (oneline.find("N") >= 0 && oneline.find("N") <= oneline.size()) {
				cursor = oneline.find("N");
				oneline.erase(cursor,1);
				cursor = oneline.find("I");
				oneline.erase(cursor,1);
				cursor = oneline.find("N");
				oneline.erase(cursor,1);
				cursor = oneline.find("E");
				oneline.erase(cursor,1);
				tmp[9]++;
			}
		}

		outfile << "Case #" << a0 + 1 << ": ";

		for (int a1 = 0; a1 < 10; a1++) {
			for (int a2 = 0; a2 < tmp[a1]; a2++) {
				outfile << a1;
			}
		}

		outfile << "\n";
	}

	infile.close();
	outfile.close();

	return 0;
}
