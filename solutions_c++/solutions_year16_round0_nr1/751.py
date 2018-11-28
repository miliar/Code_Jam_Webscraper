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
	if (res > 0) {
		cout << "Case #" << i << ": " << res << endl;
	}
	else {
		cout << "Case #" << i << ": INSOMNIA" << endl;
	}
}

int 
Solve(int N)
{
	assert(N >= 0);
	if (N > 0) {
		bitset<10> digitsSeen;
		int val = 0;
		while (!digitsSeen.all()) {
			val += N;
			assert(val >= 0);
			auto digits = val;
			while (digits > 0) {
				int lastDigit = digits % 10;
				digits = digits / 10;
				digitsSeen.set(lastDigit);
			};
		}
		return val;
	}
	else {
		return 0;
	}
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

	for (int i = 1; i <= T; ++i) {
		int N;
		cin >> N;
		auto r = Solve(N);
		PrintResult(i, r);
	}
	
    return 0;
}

