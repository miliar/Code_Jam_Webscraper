#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int minimumScore(int c, int w) {
	if (c == w) {
		return w;
	}
	if (c <= w * 2 - 1) {
		return w + 1;
	}
	return minimumScore(c - w, w) + 1;
}

int main() {
	freopen("A-small-practice.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		int r, c, w;
		cin >> r >> c >> w;
		
		cout << "Case #" << tc << ": " << minimumScore(c, w) << endl;
		
	}
}