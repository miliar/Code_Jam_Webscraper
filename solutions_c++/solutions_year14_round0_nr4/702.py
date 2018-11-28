#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

// Problem D. Deceiful War

//string infile = "sample.txt";
//string infile = "D-small-attempt1.in";
string infile = "D-large.in";
string outfile = "output.txt";

ifstream in(infile);
ofstream out(outfile);

int main () {

	int T;
	in >> T;
	for (int test = 1; test <= T; ++test) {
		int N;
		in >> N;
		map<double, int> masses;
		map<double, int> war;
		map<double, int> deceitful;
		for (int i = 0; i < 2; ++i) {
			for (int j = 0; j < N; ++j) {
				double mass;
				in >> mass;
				if (i == 0) {
					masses[mass] = 1;
				}
				war[mass] = i;
				deceitful[mass] = i;
			}
		}
		
		// do war
		int war_score = 0;
		auto it = masses.begin();
		for (int i = 0; i < N; ++i, ++it) {
			auto naomi = war.find(it->first);
			auto ken = war.begin();
			for (auto it = naomi; it != war.end();  ++it) {
				if (it->second == 1) {
					ken = it;
					break;
				}
			}
			double chosen[] = {naomi->first, ken->first};
			war.erase(chosen[0]);
			war.erase(chosen[1]);
			if (chosen[0] > chosen[1]) {
				++war_score;
			}
		}
		
		// do deceitful war
		int deceitful_score = 0;
		auto rit = masses.rbegin();
		for (int i = 0; i < N; ++i, ++rit) {
			auto naomi = deceitful.find(rit->first);
			auto ken = naomi;
			bool done = false;
			for (auto it = naomi; it != deceitful.begin(); --it) {
				if (it->second == 1) {
					ken = it;
					++deceitful_score;
					double chosen[] = {naomi->first, ken->first};
					deceitful.erase(chosen[0]);
					deceitful.erase(chosen[1]);
					done = true;
					break;
				}
			}
			if (! done) {
				if (deceitful.begin()->second == 1) {
					ken = deceitful.begin();
					++deceitful_score;
					double chosen[] = {naomi->first, ken->first};
					deceitful.erase(chosen[0]);
					deceitful.erase(chosen[1]);
				}
				break;
			}
		}

		// output scores
		out << "Case #" << test << ": " << deceitful_score << " " << war_score << endl;
	}

	return 0;
}
