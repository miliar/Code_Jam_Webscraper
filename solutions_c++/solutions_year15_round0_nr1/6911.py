#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <set>

using namespace std;

int main(int argc, char** argv) {
	bool const isCout = argc == 2;
	ostream * out = argc == 3 ? new ofstream(argv[2]) : &cout;

	ifstream in(argv[1]);
	size_t T;
	in >> T;
	for (size_t t = 0; t < T; ++t) {
		*out << "Case #" << t+1 << ": ";
		size_t SMax;
		in >> SMax;
		size_t numStanding = 0;
		size_t numExtras = 0;
		for (size_t shyness = 0; shyness <= SMax; ++shyness) {
			char digit;
			in >> digit;
			auto const numAtShyness = stoi(string(1,digit));
			if (numStanding < shyness)  {
				auto const numNeeded = shyness - numStanding;
				numExtras += numNeeded;
				numStanding += numNeeded;
			}
			numStanding += numAtShyness;
		}
		*out << numExtras << endl;
	}

	if (not isCout) delete out;
	return 0;
}
