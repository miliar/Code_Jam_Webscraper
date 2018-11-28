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
PrintResult(int i, const vector<uint64_t>& res)
{
	cout << "Case #" << i << ":";
	if (res.empty()) {
		cout << " IMPOSSIBLE";
	}
	else {
		for (auto s : res) {
			cout << " " << s;
		}
	}
	cout << endl;
}

int
Checked(int& c, int k)
{
	int ret = c;
	c = min(c + 1, k - 1);
	return ret;
}

uint64_t
Pow(int k, int c)
{
	uint64_t r = 1;
	for (int i = 0; i < c; ++i) {
		r *= k;
	}
	return r;
}

vector<uint64_t>
Solve(int K, int C, int S)
{
	vector<uint64_t> res;
	int minS = max(K / C + bool(K%C), 1);
	if (S < minS) return res;
	
	int nChecks = min(C, K);
	int checked = 0;
	for (int i = 0; i < minS; ++i) {
		uint64_t tile = 0;
		for (int j = 1; j <= nChecks; ++j) {
			uint64_t t = Checked(checked, K) * Pow(K, nChecks - j);
			tile += t;
			//cout << t << " ";
		}
		res.push_back(tile + 1);
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

	for (int i = 1; i <= T; ++i) {
		int K, C, S;
		cin >> K >> C >> S;
		auto r = Solve(K, C, S);
		PrintResult(i, r);
	}

	return 0;
}

