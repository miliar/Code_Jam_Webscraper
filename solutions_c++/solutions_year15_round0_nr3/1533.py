#include <iostream>
#include <fstream>
#include <cassert>
#include <algorithm>
#include <functional>
#include <vector>
#include <stack>
#include <queue>
#include <string>

using namespace std;


char table[5][5] = {
	{ 0, 0, 0, 0, 0 },
	{ 0, 1, 2, 3, 4 },
	{ 0, 2, -1, 4, -3 },
	{ 0, 3, -4, -1, 2 },
	{ 0, 4, 3, -2, -1 }
};

char calc(char a, char b) {
	bool neg = false;
	if (a < 0) {
		a = -a;
		neg = !neg;
	}
	if (b < 0) {
		b = -b;
		neg = !neg;
	}
	char ret = table[a][b];
	return (neg ? -ret : ret);
}

bool solve(int l, int x, string line) {
	int lineSize = line.length();
	vector<char> data(lineSize, 0);
	char total = 1;
	for (int i = 0; i<lineSize; i++) {
		data[i] = line[i] - 'g';
		total = calc(total, data[i]);
	}
	char tmp = 1;
	for (int i = 0; i<x % 4; i++) {
		tmp = calc(tmp, total);
	}
	if (tmp != -1)
		return false;
	int maxIndex = lineSize * ((x >= 8) ? (x % 4 + 8) : x);
	int leftIndex, rightIndex;
	int left = 1, right = 1;
	for (leftIndex = 0; leftIndex < maxIndex; leftIndex++) {
		left = calc(left, data[leftIndex%lineSize]);
		if (left == 2)
			break;
	}
	for (rightIndex = maxIndex - 1; rightIndex >= 0; rightIndex--) {
		right = calc(data[rightIndex%lineSize], right);
		if (right == 4)
			break;
	}
	if (leftIndex >= maxIndex || rightIndex < 0)
		return false;
	if (leftIndex >= rightIndex - 1)
		return false;
	return true;
}

int main() {
	string inputFile = "C-small-attempt3.in";
	string outputFile = "C-small-attempt3.out";
	ifstream fin(R"(D:\coder\)" + inputFile);
	ofstream fout(R"(D:\coder\)" + outputFile);
	int t;
	fin >> t;
	for (int k = 1; k <= t; k++) {
		int l, x;
		string line;
		fin >> l >> x >> line;
		bool result = solve(l, x, line);
		fout << "Case #" << k << ": " << (result ? "YES" : "NO") << endl;
	}
	return 0;
}
