// CodeJam.cpp : �w�q�D���x���ε{�����i�J�I�C
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

/*
int solve(priority_queue<int> &q, int steps) {
	if (q.top() == 1) return steps+1;
	if (q.top() == 2) return steps+2;

	int max = q.top();
	q.pop();
	//cout << "Max: " << max << " step: " << steps << endl;

	//cur_min = min(cur_min, max + steps);

	if (max % 2 == 1) {
		q.push(max / 2 + 1);
		q.push(max / 2);
	}
	else {
		q.push(max / 2);
		q.push(max / 2);
	}

	return min(max+steps, solve(q, steps+1));
}*/

int solve(const vector<int> &q) {
	int MAX = INT_MIN;
	for (int i = 0; i < q.size(); ++i) {
		MAX = max(MAX, q[i]);
	}

	int ans = MAX;
	for (int eat = 2; eat < MAX; ++eat) {
		int steps = 0;
		for (int i = 0; i < q.size(); ++i) {
			int pan = q[i];
			while (pan > eat) {
				pan -= eat;
				++steps;
			}
		}

		ans = min(ans, eat + steps);
	}

	return ans;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream infile("B-large.in");
	ofstream outfile("B-large.out");

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
		//cout << "numItem: " << numItem << endl;

		vector<int> ps;
		//priority_queue<int> ps;
		//int max = INT_MIN;
		getline(infile, line);
		stringstream ss3(line);
		//cout << "p: ";
		for (int i = 0; i < numItem; ++i) {
			int p;
			ss3 >> p;
			//cout << p << " ";
			ps.push_back(p);
			//if (p > max) max = p;
		}
		//cout << endl;
		assert(ps.size() == numItem);

		int ans = 0;
		ans = solve(ps);
		outfile << "Case #" << ++curCase << ": " << ans << endl;
		//system("pause");
	}
	assert(curCase == numCase);
	infile.close();
	outfile.close();

	system("pause");
	return 0;
}

