#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int SolvePuzzle(unsigned A, vector<unsigned> &motes);

int main(int argc, char *argv[]) {

	fstream infile(argv[1]);
	if(!infile.is_open()) {
		cerr << "Could not open file " << argv[0] << endl;
		return -1;
	}

	string line;
	getline(infile, line);
	int testCase = atoi(line.c_str());
	for(int i = 1; i <= testCase; ++i) {
		cout << "Case #" << i << ": ";
		getline(infile, line);
		unsigned A, N;
		stringstream ss(line);
		ss >> A >> N;
		getline(infile, line);
		stringstream smotes(line);
		vector<unsigned> motes;
		for(unsigned i = 0; i < N; ++i) {
			unsigned mote;
			smotes >> mote;
			motes.push_back(mote);
		}
		cout << SolvePuzzle(A, motes) << endl;
	}

	return 0;
}

int SolvePuzzle(unsigned A, vector<unsigned> &motes) {
	if(A < 2) return motes.size();
	sort(motes.begin(), motes.end());
	unsigned curA(A), operation(0);
	for(unsigned i = 0; i < motes.size(); ++i) {
		if(curA <= motes[i]) {
			unsigned n = curA - 1;
			unsigned count(0);
			while(curA <= motes[i]) {
				curA += n;
				n = curA - 1;
				++count;
				if(count >= motes.size() - i) 
					return operation + motes.size() - i;
			}
			operation += count;
		}
		curA += motes[i];
	}
	return operation;
}
