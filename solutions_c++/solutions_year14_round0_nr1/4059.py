#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	int i, j, k;
	int num;
	int first, second;
	int target;
	bool mark[17];
	int match = 0;
	int result;

	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in");
	out.open("result.txt");

	in >> num;
	for (i = 0; i < num; i++) {
		match = 0;
		fill_n(mark, 17, false);
		in >> first;
		for (j = 1; j <= 4; j++) {
			if (j == first) {
				for (k = 0; k < 4; k++) {
					in >> target;
					mark[target] = true;
				}
			}
			else {
				for (k = 0; k < 4; k++) {
					in >> target;
				}
			}
		}
		in >> second;
		for (j = 1; j <= 4; j++) {
			if (j == second) {
				for (k = 0; k < 4; k++) {
					in >> target;
					if (mark[target] == true) {
						match++;
						result = target;
					}
				}
			}
			else {
				for (k = 0; k < 4; k++) {
					in >> target;
				}
			}
		}
		out << "Case #" << i + 1 << ": ";
		if (match == 1)
			out << result << '\n';
		else if (match == 0)
			out << "Volunteer cheated!\n";
		else
			out << "Bad magician!\n";
	}

	out.close();

	return 0;
}