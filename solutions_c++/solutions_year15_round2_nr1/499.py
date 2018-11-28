// ConsoleApplication3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <algorithm>
#include <iostream>
#include <string>
#include <cassert>
#include <sstream>

using namespace std;

int to_int(string s) { stringstream ss(s); int x; ss >> x; return x; }

string to_str(long long x) { stringstream ss; ss << x; string s; ss >> s; return s; }

void solve()
{
	long long k; cin >> k;
	int res = 0;
	while (k % 10 == 0) {
		--k;
		++res;
	}
	string s = to_str(k);
	while (s.size() > 1) {
		int n = s.size();
		string s1 = s.substr(0, n / 2);
		reverse(s1.begin(), s1.end());
		string s2 = s.substr(n / 2, (n + 1) / 2);
		res += to_int(s2) - 1;
		if (to_int(s1) != 1) {
			res += 1;
			res += to_int(s1) - 1;
		}
		string new_s = "";
		for (int i = 0; i < n - 1; ++i)
			new_s += '9';
		res += 2;
		s = new_s;
	}
	res += s[0] - '0';
	cout << res;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t; cin >> t;
	for (auto q = 1; q <= t; ++q) {
		cout << "Case #" << q << ": ";
		solve();
		cout << endl;
	}
	return 0;
}

