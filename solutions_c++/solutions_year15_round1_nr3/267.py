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


#define PI 3.1415926535898

vector<int> solve(vector<pair<int, int>> &data) {
	vector<int> result;
	for (const pair<int, int> curr : data) {
		vector<long double> angle;
		for (const pair<int, int> p : data) {
			if (p == curr)
				continue;
			angle.push_back(atan2l(p.second - curr.second, p.first - curr.first));
		}
		sort(angle.begin(), angle.end());
		int size = angle.size();
		for (int i = 0; i < size; i++) {
			angle.push_back(angle[i] + 2 * PI);
		}
		int start = 0, end = 0;
		int mmax = 1;
		for (end = 1; end < angle.size(); end++) {
			while (angle[end] - angle[start] > (PI + 1e-8))
				start++;
			mmax = max(mmax, end - start + 1);
		}
		if (mmax > size)
			mmax = size;
		result.push_back(size - mmax);
	}
	return result;
}

int main() {
	string path = R"(D:\coder\)";
	string infile = "C-large.in";
	string outfile = "C-large.out";
	ifstream cin(path + infile);
	ofstream cout(path + outfile);
	int t;
	cin >> t;
	for (int k = 1; k <= t; k++) {
		int n;
		cin >> n;
		vector<pair<int, int>> data(n);
		for (int i = 0; i < n; i++) {
			int x, y;
			cin >> x >> y;
			data[i].first = x;
			data[i].second = y;
		}
		vector<int> ret = solve(data);
		cout << "Case #" << k << ":" << endl;
		for (int r : ret) {
			cout << r << endl;
		}
	}
	system("pause");
}
