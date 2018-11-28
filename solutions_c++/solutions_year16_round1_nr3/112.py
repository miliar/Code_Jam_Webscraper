#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

using ll = long long int;
ifstream fin("3.in");
ofstream fout("3.out");

int recipCount[1000][1000] = {};

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		int bff[1000], n;
		fin >> n;
		for (int i = 0; i < n; i++) {
			fin >> bff[i];
			bff[i]--;
		}

		for (int i = 0; i < n; i++) 
			for (int j = 0; j < n; j++)
				recipCount[i][j] = 0;

		int largestLoop = 0;
		for (int start = 0; start < n; start++) {
			bool visited[1000] = {};
			int count = 0;
			int cur = start;
			while (!visited[cur]) {
				visited[cur] = true;
				count++;
				cur = bff[cur];
			}
			if (cur == start)
				largestLoop = max(largestLoop, count);
			if (bff[bff[cur]] == cur) 
				recipCount[cur][bff[cur]] = max(recipCount[cur][bff[cur]], count - 1);
		}

		int total = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				total += recipCount[i][j];

		fout << "Case #" << t << ": ";
		fout << max(total, largestLoop) << endl;
	}
}
