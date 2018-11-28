#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

using ll = long long int;
ifstream fin("2.in");
ofstream fout("2.out");


int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		fin >> n;
		int heights[2501] = {};
		for (int i = 0; i < 2*n-1; i++) {
			for (int j = 0; j < n; j++) {
				int h;
				fin >> h;
				heights[h]++;
			}
		}
		vector<int> answer;
		for (int i = 0; i < 2501; i++)
			if (heights[i] % 2 == 1)
				answer.push_back(i);
		if (answer.size() != n)
			cout << "ERROR" << endl;
		sort(answer.begin(), answer.end());

		fout << "Case #" << t << ":";
		for (int i : answer)
			fout << " " << i;
		fout << endl;
	}
}
