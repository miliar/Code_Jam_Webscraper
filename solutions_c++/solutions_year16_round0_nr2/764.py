#include "stdafx.h"
#include <math.h> 
#include <iostream>
#include <fstream>
#include <sstream> 
#include <set> 
#include <map> 
#include <vector> 
#include <list> 
#include <string>
#include <algorithm>
#include <cassert>
#include <bitset>

using namespace std;

void
PrintResult(int i, int res)
{
	cout << "Case #" << i << ": " << res << endl;
}

int 
Solve(const string& pancakes)
{
	int res = 0;
	auto lastSeen = pancakes[0];
	for (auto& pancake : pancakes) {
		assert(pancake == '+' || pancake == '-');
		if (lastSeen != pancake) {
			++res;
			lastSeen = pancake;
		}
	}
	if (lastSeen == '-') {
		++res;
	}
	return res;
}

int
main()
{
	ifstream in("in.txt");
	cin.rdbuf(in.rdbuf());

	ofstream out("out.txt");
	cout.rdbuf(out.rdbuf());

	int T;
	cin >> T;

	string pancakes;
	for (int i = 1; i <= T; ++i) {
		do {
			getline(cin, pancakes);
		} while (pancakes.empty());
		auto r = Solve(pancakes);
		PrintResult(i, r);
	}

	return 0;
}
