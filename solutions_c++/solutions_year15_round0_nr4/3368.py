/*
ID: kostya.3
PROG: test
LANG: C++11
*/
#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <string>
#include <utility>
using namespace std;

int main() {
	ofstream fout("output.txt");
	ifstream fin("input.txt");
	int t;
	fin >> t;
	for (int times = 1; times <= t; times++)
	{
		int x, r, c;
		fin >> x >> r >> c;
		int maxd = max(r, c);
		int mind = min(r, c);
		bool poss = 1;
		if ((r*c) % x != 0)
			poss = 0;
		if (x == 2 && maxd < 2)
			poss = 0;
		if (x == 3 && (maxd < 3 || mind < 2))
			poss = 0;
		if (x == 4 && (maxd < 4 || mind < 3))
			poss = 0;
		fout << "Case #" << times << ": ";
		if (poss)
			fout << "GABRIEL" << endl;
		else
			fout << "RICHARD" << endl;
	}
	cin.get();
	return 0;
}