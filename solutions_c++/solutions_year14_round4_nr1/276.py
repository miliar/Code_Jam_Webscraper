#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <memory.h>
#include <cassert>
#include <algorithm>
#include <vector>

#define DB(x) cerr << #x << ": " << x << endl;

using namespace std;

// const char* inputFile = "input.in";
const char* inputFile = "A-large.in";
const char* outputFile = "A-large.out";

class Solver {
public:
	Solver() {
	}

	int getMovesNumber(int median, int position, const vector<vector< pair<int, char> > > &values) {
	}

	string solveTest() {
		cin >> n >> x;
		sizes.resize(n);
		for (int i = 0; i < n; ++i) {
			cin >> sizes[i];
		}
		sort(sizes.begin(), sizes.end());

		int ans = 0;
		int R = sizes.size();
		vector<char> used(sizes.size(), false);
		// DB(sizes.size());
		for (int i = 0; i < sizes.size(); ++i) {
			int a = sizes[i];
			if (used[i]) {
				continue;
			}
			used[i] = true;
			ans++;
			int l = i + 1;
			int r = R;
			while (l + 1 < r) {
				int m = (l + r) / 2;
				if (a + sizes[m] > x) {
					r = m;
				} else {
					l = m;
				}
			}
			if (a + sizes[l] <= x) {
				used[l] = true;
				R = l;
			}
		}
		return std::to_string(ans);
	}

	int n, x;
	vector<int> sizes;
};

int main() {
	freopen(inputFile, "r", stdin);
	freopen(outputFile, "w", stdout);
	int T;
	scanf("%d", &T);

	for (int testNumber = 1; testNumber <= T; ++testNumber) {
		Solver solver;
		string verdict = solver.solveTest();
		printf("Case #%d: %s\n", testNumber, verdict.c_str());
	}
	return 0;
}
