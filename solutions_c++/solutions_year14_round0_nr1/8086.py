/**
*	MagicTrick.cpp
*	Copyright 2014, Matt Parish
*
*	See MagicTrick.pdf for problem description and sample input/output.
*
*	Algorith:
*	Read num cases
*	For each case
*		Read answer 1
*		Read 4x4 grid
*		Read answer 2
*		Read 4x4 grid
*		Test for answer
*		Output
*	end for
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

const string INPUT_FILE = "A-small-attempt0.in";
const string OUTPUT_FILE = "output.txt";

int main() {
	ifstream in(INPUT_FILE);
	if(in.fail()) {
		cerr << INPUT_FILE << " failed to open.\n";
		exit(1);
	}

	ofstream out(OUTPUT_FILE);
	if(out.fail()) {
		cerr << OUTPUT_FILE << " failed to open.\n";
		exit(2);
	}

	int numCases=0, answer1=0, answer2=0;
	vector<vector<int> > grid1, grid2;

	in >> numCases;

	for(int currCase=1; currCase<=numCases; ++currCase) {
		// Read question 1
		in >> answer1;
		answer1--;
		for(int i=0; i<4; ++i) {
			grid1.push_back(vector<int>());

			for(int j=0; j<4; ++j) {
				int card=0;
				in >> card;
				grid1[i].push_back(card);
			}
		}

		// Read question 2
		in >> answer2;
		answer2--;
		for(int i=0; i<4; ++i) {
			grid2.push_back(vector<int>());

			for(int j=0; j<4; ++j) {
				int card=0;
				in >> card;
				grid2[i].push_back(card);
			}
		}

		// Test for answer
		vector<int> cards;

		for(int i=0; i<4; ++i) {
			int card=grid1[answer1][i];

			if(find(grid2[answer2].begin(), grid2[answer2].end(), card) != grid2[answer2].end()) {
				cards.push_back(card);
			}
		}

		// Output
		out << "Case #" << currCase << ": ";

		switch(cards.size()) {
		case 0: out << "Volunteer cheated!\n"; break;
		case 1: out << cards.at(0) << endl; break;
		default: out << "Bad magician!\n"; break;
		}

		// Reset
		grid1.clear();
		grid2.clear();
	}

	return 0;
}