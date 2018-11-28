#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

int main() {
	ifstream input("A-small-attempt2.in", ios::in);
	ofstream output("A-small-attempt2.out", ios::out);
	
	int T, smax;
	char val;
	vector<unsigned int> *v;
	
	unsigned int clappers, needed_clappers;
	
	input >> T;
	v = new vector<unsigned int>[T];
	
	
	for (int i = 0; i < T; i++) {
		input >> smax;
		for (int j = 0; j <= smax; j++) {
			input >> val;
			v[i].push_back((val - 48));
		}
	}
	
	
	for (int i = 0; i < T; i++) {
		clappers = 0;
		needed_clappers = 0;
		for (unsigned j = 0; j < v[i].size() - 1; j++) {
			clappers += v[i][j];
			if (j + 1 > clappers && v[i][j + 1] > 0) {
				needed_clappers += j + 1 - clappers;
				clappers += needed_clappers;
			}
		}
		output << "Case #" << i + 1 << ": " << needed_clappers << endl;
		 
	}
	return 0;
}
