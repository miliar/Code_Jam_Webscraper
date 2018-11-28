#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;


int main(int argc, char* argv[])
{
	string fname;
	std::cin >> fname;
	string ifname = fname + ".in";
	string ofname = fname + ".out";
	ifstream in(ifname.c_str());
	ofstream out(ofname.c_str());
	
	int T;
	in >> T;
	for (int i = 0; i < T; ++i) {
		int rowNum;
		vector<int> row;
		in >> rowNum;
		int t;
		for (int j = 0; j < 16; ++j) {
			in >> t;
			if ((j >= (rowNum - 1) * 4) && (j < rowNum * 4)) {
				row.push_back(t);
			}
		}

		in >> rowNum;
		vector<int> row2;
		for (int j = 0; j < 16; ++j) {
			in >> t;
			if ((j >= (rowNum - 1) * 4) && (j < rowNum * 4)) {
				row2.push_back(t);
			}
		}

		int matches = 0;
		int matched;
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				if (row.at(j) == row2.at(k)) { 
					matches++; 
					matched = row.at(j);
				}
			}
		}

		out << "Case #" << i + 1 << ": ";
		if (matches == 1) {
			out << matched << std::endl;
		}
		else if (matches == 0) {
			out << "Volunteer cheated!\n";
		}
		else {
			out << "Bad magician!\n";
		}
	}
	
	return 0;
}