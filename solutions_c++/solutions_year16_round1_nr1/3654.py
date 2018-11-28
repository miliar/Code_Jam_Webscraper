// gcjr1a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>

using namespace std;


int main()
{
	ifstream a("D:\\gcj\\A-large.in.sdx");
	ofstream o("D:\\gcj\\output.txt");
	int nr; a >> nr;
	std::string line;
	std::getline(a, line);
	for (int i = 0; i<nr; i++) {
		o << "Case #" << (i + 1) << ": ";
		string word;
		a >> word;
		string lw;
		for (auto it = word.begin(); it != word.end(); it++) {
			if (lw.empty()) {
				lw.push_back(*it);
				continue;
			}
			if (lw[0] > *it) {
				lw.push_back(*it);
			}
			else {
				lw.insert( lw.begin(), *it);
			}

		}
		cout << lw << endl;
		o << lw << endl;
	}
	a.close();
	o.close();
	char c; cin >> c;
	return 0;
}

