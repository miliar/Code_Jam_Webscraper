#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<unsigned> getDigits(unsigned n) {
	vector<unsigned> d;
	while (n >= 10) {
		d.push_back(n % 10);
		n /= 10;
	}
	d.push_back(n);
	return d;
}

unsigned getY(unsigned n) {
	unsigned y = n;
	vector<bool> digits(10, 0);
	for (unsigned i = 2; i < 10e6; i++) {
		// Extract and remember digits
		vector<unsigned> d = getDigits(y);
		for (auto& x : d)
			digits[x] = true;

		// Found all digits?
		bool all = true;
		for (auto b : digits) {
			if (b == false) {
				all = false;
				break;
			}
		}
		if (all == true)
			return y;
		y = n * i;
	}
	return 0;
}

int main() {
	unsigned numCases = 0;
	vector<unsigned> cases;

	// Read input
	string filename = "A-large";
	ifstream in(filename + ".in");
	if (!in.good())
		throw;

	in >> numCases;
	cases.resize(numCases);
	for (unsigned i = 0; i < numCases; i++) {
		in >> cases[i];
	}
	assert(in.good());

	// Compute result and write output
	ofstream out(filename + ".out");
	if (!out.good())
		throw;

	for (unsigned i = 0; i < cases.size(); i++) {
		unsigned y = getY(cases[i]);
		if (y == 0) {
			out << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
		} else {
			out << "Case #" << i + 1 << ": " << y << endl;
		}
	}
	assert(out.good());
	out.close();
	cout << "Wrote " << cases.size() << " lines" << endl;
	return 0;
}
