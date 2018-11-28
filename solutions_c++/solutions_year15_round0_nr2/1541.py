#include <Windows.h>
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


int solve(vector<int> &data) {
	int mmax = 0;
	for (int d : data) {
		mmax = max(mmax, d);
	}
	int result = mmax;
	for (int k = 2; k < result; k++) {
		int curr = k;
		for (int d : data) {
			curr += (d - 1) / k;
		}
		result = min(result, curr);
	}
	return result;
}

int main() {
	string inputFile = "B-large.in";
	string outputFile = "B-large.out";
	ifstream fin(R"(D:\coder\)" + inputFile);
	ofstream fout(R"(D:\coder\)" + outputFile);
	int t;
	fin >> t;
	for (int k = 1; k <= t; k++) {
		int d;
		fin >> d;
		vector<int> data(d, 0);
		for (int i = 0; i < d; i++) {
			fin >> data[i];
		}
		int result = solve(data);
		fout << "Case #" << k << ": " << result << endl;
	}
	return 0;
}
