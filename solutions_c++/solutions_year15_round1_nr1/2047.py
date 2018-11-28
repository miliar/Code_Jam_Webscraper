// CodeJam.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <assert.h>
#include <unordered_map>
#include <algorithm>
#include <queue>

using namespace std;

void solve(const vector<long long> &q, long long &first, long long &second) {
	long long diff = LLONG_MIN;
	for (int i = 1; i < q.size(); ++i) {
		if (q[i-1] - q[i] > 0)
			first += q[i-1] - q[i];
		diff = max(q[i-1] - q[i], diff);
	}

	// diff<0? 
	// diff = rate*10
	for (int i = 0; i < q.size()-1; ++i) {
		if (q[i] >= diff) {
			second += diff;
		}
		else {
			second += q[i];
		}
	}

}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");

	string line;
	int numCase;
	getline(infile, line);
	istringstream iss(line);
	iss >> numCase;
	cout << "numCase: " << numCase << endl;

	int curCase = 0;
	while (getline(infile, line)) {
		int numItem;
		stringstream ss2(line);
		ss2 >> numItem;
		cout << "numItem: " << numItem << endl;

		vector<long long> ps;
		getline(infile, line);
		stringstream ss3(line);
		for (int i = 0; i < numItem; ++i) {
			int p;
			ss3 >> p;
			ps.push_back(p);
		}
		assert(ps.size() == numItem);

		long long first = 0, second = 0;
		solve(ps, first, second);
		outfile << "Case #" << ++curCase << ": " << first << " " << second << endl;
		//system("pause");
	}
	assert(curCase == numCase);
	infile.close();
	outfile.close();

	system("pause");
	return 0;
}

