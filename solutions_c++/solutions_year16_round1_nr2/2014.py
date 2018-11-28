#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
#include <cassert>
using namespace std;

typedef long long tl; //type long
int _tc;

#define index(a, b) ((a * n) + b)

bool testCase() {
	int n;
	cin >> n;

	//std::vector<int> heights(100000, 0);
	std::vector<int> counts(2500, 0);
	for (int l = 0; l < (2 * n - 1); ++l) {
		for (int i = 0 ; i < n; ++i) {
			int height;
			cin >> height;
			height -= 1; //normalize
			//heights[index(l, i)] = height;
			counts[height] += 1;
		}
	}
	int c = 0;
	for (int i = 0; i < 2500; ++i) {
		if (counts[i] % 2 != 0) {
			cout << " " << (i + 1);
			++c;
		}
	}
	assert(c == (n));

	return true;
}

int main(){
	int ntc;

	cin >> ntc;
	//cerr << "tests " << n << endl;
	for (int _tc = 0; _tc < ntc; ++_tc) {
		cout << "Case #" << (_tc + 1) << ":";
		if (!testCase()) {
			cout << " IMPOSSIBLE";
		}
		cout << endl;
	}
	return 0;
}