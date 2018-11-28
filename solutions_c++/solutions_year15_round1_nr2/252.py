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


typedef long long LL;

int solve(vector<int> &data, int b, int n) {
	vector<LL> curr(data.size(), 0);
	double avg = 0;
	int mmax = 0;
	for (int d : data) {
		avg += 1.0 / d;
		mmax = max(mmax, d);
	}
	avg = 1 / avg;
	LL time = avg * (n - 1) - mmax;
	if (time < 0)
		time = 0;
	for (int i = 0; i < data.size(); i++) {
		n -= time / data[i];
		curr[i] = time % data[i];
		if (curr[i])
			n -= 1;
	}
	assert(n >= 0);
	while (n >= 0) {
		for (int i = 0; i < curr.size(); i++) {
			if (curr[i] == 0) {
				if (n == 0)
					return i;
				n--;
			}
		}
		LL mmin = data[0] - curr[0];
		for (int i = 1; i < curr.size(); i++) {
			if ((data[i] - curr[i]) < mmin) {
				mmin = data[i] - curr[i];
			}
		}
		assert(mmin > 0);
		for (int i = 0; i < curr.size(); i++) {
			curr[i] = (curr[i] + mmin) % data[i];
		}
	}
	assert(false);
	return -1;
}

int main() {
	string path = R"(D:\coder\)";
	string infile = "B-large.in";
	string outfile = "B-large.out";
	ifstream cin(path + infile);
	ofstream cout(path + outfile);
	int t;
	cin >> t;
	for (int k = 1; k <= t; k++) {
		int b, n;
		cin >> b >> n;
		vector<int> data(b, 0);
		for (int i = 0; i < b; i++) {
			cin >> data[i];
		}
		int ret = solve(data, b, n - 1) + 1;
		cout << "Case #" << k << ": " << ret << endl;
	}
	system("pause");
}
