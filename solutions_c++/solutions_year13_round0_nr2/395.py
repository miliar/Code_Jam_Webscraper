#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <functional>
using namespace std;
int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int N;
	fin >> N;
	for (int cas = 0; cas < N; ++cas) {
		fout << "Case #" << cas + 1 << ": ";
		int w, h;
		fin >> w >> h;
		vector<vector<int>> m(w, vector<int>(h));
		for (int i = 0; i < w; ++i)
			for (int j = 0; j < h; ++j)
				fin >> m[i][j];
		vector<int> r(w), c(h);
		for (int i = 0; i < w; ++i)
			for (int j = 0; j < h; ++j)
				r[i] = max(r[i], m[i][j]), c[j] = max(c[j], m[i][j]);
		bool possible = true;
		for (int i = 0; i < w; ++i)
			for (int j = 0; j < h; ++j)
				if (m[i][j] < r[i] && m[i][j] < c[j])
					possible = false;
		fout << (possible ? "YES" : "NO") << endl;
	}
}