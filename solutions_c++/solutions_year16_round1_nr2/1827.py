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
PrintResult(int i, const vector<int> res)
{
	cout << "Case #" << i << ":";
	for (auto i: res) {
		cout << " " << i;
	}
	cout << endl;
}

vector<int>
Solve(const vector<vector<int>>& table)
{
	vector<int> sols;
	for (auto& rowcol : table) {
		for (auto& i : rowcol) {
			sols.push_back(i);
		}
	}
	sort(sols.begin(), sols.end());

	vector<int> res;
	int count = 0;
	auto prev = sols[0];
	for (auto& i : sols) {
		if (i == prev) {
			++count;
		}
		else {
			if (count % 2) {
				res.push_back(prev);
			}
			count = 1;
			prev = i;
		}
	}
	if (count % 2) {
		res.push_back(prev);
	}
	sort(res.begin(), res.end());
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
		int N;
		cin >> N;
		vector<int> rowcol(N);
		vector<vector<int>> table;
		for (int k = 0; k < 2 * N - 1; ++k) {
			for (int j = 0; j < N; ++j) {
				cin >> rowcol[j];
			}
			table.push_back(rowcol);
		}
		auto r = Solve(table);
		PrintResult(i, r);
	}

	return 0;
}
