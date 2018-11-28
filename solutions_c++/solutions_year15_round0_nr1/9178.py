#include <cstdio>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int main(int argc, char* argv[]) {
	ifstream f;
	f.open("A-large.in");
	if (!f.is_open()) {
		cerr << "Could not open file.\n";
		return -1;
	}

	ofstream out;
	out.open("A-large.txt");
	if (!out.is_open()) {
		cerr << "Could not open output file.\n";
		return -1;
	}

	int t;
	f >> t;

	for (int q = 0; q < t; q++) {
		int m;
		f >> m;

		char empty;
		f.get(empty);

		char rising = 0;
		int already_standing = 0;
		int extra_invited = 0;
		for (int s = 0; s <= m; s++) {
			int level_extra = 0;
			f.get(rising);
			rising -= 48;
			if (s != 0 && rising != 0) {
				if (already_standing < s)
					level_extra += (s-already_standing);
			}
			already_standing += rising + level_extra;
			extra_invited += level_extra;
		}

		out << "Case #" << q+1 << ": " << extra_invited << "\n";
	}

	f.close();
	out.close();
}