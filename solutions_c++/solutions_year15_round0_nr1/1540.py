#include <iostream>
#include <fstream>
#include <cassert>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;


int solve(vector<int> &data) {
	int size = data.size();
	int result = 0;
	int curr = 0;
	for (int i = 0; i < size; i++) {
		if (curr < i) {
			result += i - curr;
			curr = i;
		}
		curr += data[i];
	}
	return result;
}

int main() {
	string inputFile = "A-large.in";
	string outputFile = "A-large.out";
	ifstream fin(R"(D:\coder\)" + inputFile);
	ofstream fout(R"(D:\coder\)" + outputFile);
	int t;
	fin >> t;
	for (int k = 1; k <= t; k++) {
		int s;
		fin >> s;
		vector<int> data(s+1, 0);
		string line;
		fin >> line;
		for (int i = 0; i <= s; i++) {
			data[i] = line[i] - '0';
		}
		int result = solve(data);
		fout << "Case #" << k << ": " << result << endl;
	}
	return 0;
}
