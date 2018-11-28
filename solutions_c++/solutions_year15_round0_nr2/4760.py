/*
 * Main.cpp
 *
 *  Created on: 11 Apr 2015
 *      Author: Kristjan
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cmath>

using namespace std;

void pancake();
int algo(vector<int> inp);
int algo2(vector<int> inp);

int main() {
	pancake();
	return 0;
}

void pancake() {
	int T = 0;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		clock_t start = clock();
		int D = 0;
		cin >> D;
		vector<int> inp;
		int temp = 0;
		for (int d = 1; d <= D; d++) {
			cin >> temp;
			inp.push_back(temp);
		}

		cout << "Case #" << t << ": " << algo2(inp) << endl;
		cerr << "Case #" << t << " - ";
		cerr << "time: " << (clock() - start) / (double) (CLOCKS_PER_SEC / 1000)
				<< " ms" << endl;
	}
}

int algo(vector<int> inp) {
	auto it = inp.begin();
	for (; it != inp.end(); it++) {
		cerr << *it << " ";
	}
	cerr << endl;

	int max = *max_element(inp.begin(), inp.end());
	int best = max;
	int xtra = 0;

	while (max > 3) {
		*max_element(inp.begin(), inp.end()) -= int(max / 2.0);
		inp.push_back(max / 2.0);
		max = *max_element(inp.begin(), inp.end());
		xtra++;
		if (max + xtra < best)
			best = max + xtra;
		if (xtra > best)
			break;
	}

	return best;
}

int algo2(vector<int> inp) {
	int best = 400000;
	int cur = 0;

	for (int d = 1; d <= 1000; d++) {
		cur = 0;
		for (auto e : inp) {
			cur += ceil(float(e) / d) - 1;
		}
		if (cur + d < best)
			best = cur + d;
	}

	return best;
}
