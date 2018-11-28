/*
 * A.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: nmarwan
 */

#include <iostream>
#include <sstream>
#include <set>
#include <algorithm>
#include <vector>
#include <memory.h>
#include <math.h>
#include <map>

using namespace std;

#define min(x, y) ((x) < (y) ? (x) : (y))
#define KEY(a,b,c) (make_pair(a, make_pair(b,c)))

string c, j;
map< pair<int, pair<int, int>>, pair<int, pair<int, int>>> mem;
int l;
pair<int, pair<int, int>> calc(int idx, int cc, int jj) {
	if (idx == l){
		return make_pair(abs(cc - jj), make_pair(cc, jj));
	}

	if (mem.count(KEY(idx, cc, jj)) > 0) {
		return mem[KEY(idx, cc, jj)];
	}

	pair<int, pair<int, int>> r = KEY(1e5, cc, jj);
	int v = pow(10, l - idx - 1);
	if (c[idx] == '?' && j[idx] == '?') {
		for (int i = 0; i < 10; i++) {
			for (int ii = 0; ii < 10; ii++) {
				r = min(r, calc(idx + 1, cc*10 + i, jj*10 + ii));
			}
		}
	} else if (c[idx] == '?') {
		for (int i = 0; i < 10; i++) {
			r = min(r, calc(idx + 1, cc*10 +i, jj*10 + j[idx]-'0'));
		}
	} else if (j[idx] == '?') {
		for (int i = 0; i < 10; i++) {
			r = min(r, calc(idx + 1, cc*10 + c[idx] - '0', jj*10 + i) );
		}
	} else {
		r = min(r, calc(idx + 1, cc*10 + c[idx]-'0', jj*10 + j[idx]-'0'));
	}
	return r;
}

enum state {
	eq = 0, cBig = 1, jBig = 2
};

int main() {
	freopen("A.in", "rt", stdin);
	freopen ("a2.txt", "wt", stdout);

	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		cout << "Case #" << tt << ": ";
		cin >> c >> j;
		l = c.size();
		auto res = calc(0 , 0, 0);
		stringstream ss;
		ss << res.second.first ;
		string newc;
		ss >> newc;

		stringstream ss1;
		ss1 << res.second.second ;
		string newj;
		ss1 >> newj;

		while(newc.size() < c.size()) {
			newc = "0"+newc;
		}

		while(newj.size() < j.size()) {
			newj = "0"+newj;
		}
		cout << newc << " " << newj << endl;
//		cout << res.first << " " << res.second.first << " " << res.second.second << endl;

	}
}
