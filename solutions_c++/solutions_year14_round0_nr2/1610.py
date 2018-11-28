#include <iostream>
#include <fstream>
#include <algorithm>
#include <limits>
#include <iomanip>
using namespace std;

int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");
	out << setprecision(numeric_limits<long double>::digits10);
	int T;
	in >> T;

	for (int i = 0; i < T; ++i) {
		long double farmcost, farmcps, goal;
		in >> farmcost >> farmcps >> goal;
		long double best = goal / 2;
		
		long double cps = 2;
		long double spent = 0;
		while (spent < best) {
			spent += farmcost / cps;
			cps += farmcps;
			best = min(best, spent + goal / cps);
		}

		out << "Case #" << i + 1 << ": " << best << endl;
	}
	return 0;
}