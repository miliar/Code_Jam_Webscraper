#include <cstdio>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char* argv[]) {
	ifstream f;
	f.open("B-large.in");
	if (!f.is_open()) {
		cerr << "Could not open file.\n";
		return -1;
	}

	ofstream out;
	out.open("output_small2.txt");
	if (!out.is_open()) {
		cerr << "Could not open output file.\n";
		return -1;
	}

	int n;
	f >> n;

	for(int o = 1; o <= n; o++) {
		double c, t, x;
		f >> c;
		f >> t;
		f >> x;

		double tcur = 2.0;
		double tfarm = 0.0;
		double tgoal = 0.0;

		double time_elapsed = 0.0;

		do {
			tfarm = c / tcur + x/(tcur+t);
			tgoal = x / tcur;

			if (tfarm < tgoal) {
				time_elapsed += c / tcur;
				tcur += t;
			} else {
				time_elapsed += tgoal;
				break;
			}
		}
		while (true);

		out << "Case #" << o << ": ";
		out << fixed << setprecision(7) << time_elapsed << endl;

	}

	f.close();
	out.flush();
	out.close();
}