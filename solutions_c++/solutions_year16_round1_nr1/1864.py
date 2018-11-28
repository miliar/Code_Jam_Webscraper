#include "stdafx.h"
#include <math.h> 
#include <iostream>
#include <fstream>
#include <sstream> 
#include <set> 
#include <map> 
#include <vector> 
#include <list> 
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
PrintResult(int i, const string& res)
{
	cout << "Case #" << i << ": " << res << endl;
}

string
Solve(string N)
{
	int larger[256] = {};
	for (auto c : N) {
		for (int i = 'A'; i < c; ++i) {
			++larger[i];
		}
	}
	string res;
	for (auto c : N) {
		int i = (int)c;
		if (res.empty() || res[0] > c) {
			res.push_back(c);
		}
		else {
			res.insert(0, 1, c);
		}
		for (int i = 'A'; i < c; ++i) {
			--larger[i];
		}
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

	string S;
	for (int i = 1; i <= T; ++i) {
		do {
			getline(cin, S);
		} while (S.empty());
		auto r = Solve(S);
		PrintResult(i, r);
	}

	return 0;
}
