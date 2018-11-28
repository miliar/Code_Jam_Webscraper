#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <string>
#include <cassert>
#include <algorithm>
#include <climits>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>

using namespace std;


int solve1(vector<int> &data) {
	int result = 0;
	int prev = 0;
	for (int d : data) {
		if (d < prev)
			result += prev - d;
		prev = d;
	}
	return result;
}

int solve2(vector<int> &data) {
	int speed = 0;
	int prev = 0;
	for (int d : data) {
		speed = max(speed, prev - d);
		prev = d;
	}
	int result = 0;
	prev = 0;
	for (int d : data) {
		if (prev < speed) {
			result += prev;
			prev = 0;
		}
		else {
			result += speed;
			prev -= speed;
		}
		if (prev > d) {
			cout << "err";
		}
		prev = d;
	}
	return result;
}

int main() {
	string path = R"(D:\coder\)";
	string infile = "A-large.in";
	string outfile = "A-large.out";
	ifstream cin(path + infile);
	ofstream cout(path + outfile);
	int t;
	cin >> t;
	for (int k = 1; k <= t; k++) {
		int n;
		cin >> n;
		vector<int> data(n, 0);
		for (int i = 0; i < n; i++) {
			cin >> data[i];
		}
		int ret1 = solve1(data);
		int ret2 = solve2(data);
		cout << "Case #" << k << ": " << ret1 << " " << ret2 << endl;
	}
}
