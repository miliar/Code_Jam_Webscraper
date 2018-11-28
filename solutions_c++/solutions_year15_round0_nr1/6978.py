// CodeJam 2015: Qual. Round
// Author: Dan Roberts

#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main() {
	ifstream input("A-large.in");
	ofstream output("A-large.out");
	int tests;
	input >> tests;
	for(int test = 1; test <= tests; test++) {

		int max_s;
		input >> max_s;
		string s_levels;
		input >> s_levels;
		int brought = 0;
		int standing = s_levels[0] - '0';

		for(int s=1; s <= max_s; s++) {
			int level_c = s_levels[s] - '0';
			if(level_c == 0) { // skip shyness level with no people
				continue;
			}
			if(standing < s) {	
				int needed = s - standing;
				brought += needed; // add the gap between needed and avail.
				standing += needed;
			}
			standing += level_c;  
		}
		output << "Case #" << test << ": " << brought << endl;
	}
	return 0;
}
