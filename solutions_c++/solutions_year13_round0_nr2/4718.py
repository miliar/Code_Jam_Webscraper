#pragma comment(linker, "/STACK:256000000")

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <sstream>

using namespace std;

// #define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define sqr(x) ((x)*(x))
//#define foreach(e,x) for(__typeof(x.begin()) e=x.begin();e!=x.end();++e)


const double PI = acos(-1.0);
const int INF = 1000000000;
const int MOD = 1000000007;

class solver {
public:
	vector< vector<int> > current, field;
	int n, m;

	solver() {
	}

	solver(const vector<vector<int> >& field)
		: n(field.size()), m(field[0].size()), current(field.size(), vector<int>(field[0].size(), 100)), field(field) {
	}

	int height_row(int row_index) {
		int height = -1;
		for (int i = 0; i < m; ++i) {
			if (current[row_index][i] != field[row_index][i]) {
				height = max(height, field[row_index][i]);
			}
		}

		if (height == 105) height = -1;
		return height;
	}

	int height_column(int column_index) {
		int height = -1;
		for (int i = 0; i < n; ++i) {
			if (current[i][column_index] != field[i][column_index]) {
				height = max(height, field[i][column_index]);
			}
		}

		if (height == 105) height = -1;
		return height;
	}

	bool can_row(int row_index, int height) {
		for (int i = 0; i < m; ++i)
			if (field[row_index][i] > height) {
				return 0;
			}
		return 1;
	}

	void make_row(int row_index, int height) {
		for (int i = 0; i < m; ++i) {
			current[row_index][i] = min(current[row_index][i], height);
		}
	}

	bool can_column(int column_index, int height) {
		for (int i = 0; i < n; ++i)
			if (field[i][column_index] > height) {
				return 0;
			}
		return 1;
	}

	void make_column(int column_index, int height) {
		for (int i = 0; i < n; ++i) {
			current[i][column_index] = min(current[i][column_index], height);
		}
	}


	string solve() {
		while(1) {
			for (int i = 0; i < n; ++i) {
				int height = height_row(i);
				if (height == -1) continue;
				if (can_row(i, height)) {					
					make_row(i, height);
					goto end;
				}
			}

			for (int i = 0; i < m; ++i) {
				int height = height_column(i);
				if (height == -1) continue;
				if (can_column(i, height)) {
					make_column(i, height);
					goto end;
				}
			}

			if (current != field) {
				return "NO";
			}
			return "YES";

			end:;
		}
	}
};




int main() {

	/*
	//freopen("in.txt","w",stdout);
	cout << 1 << endl;
	cout << "100 100\n";
	for (int i = 0; i < 100; ++i) {
		for (int j = 0; j < 100; ++j) {
			cout << 100 - j << " ";
		}
		cout << endl;
	}

	return 0;
	*/

	freopen("in.txt","r", stdin);
	freopen("out.txt", "w", stdout);
 
	int T; cin >> T;
	for (int test = 1; test <= T; ++test) {
		int n, m;
		cin >> n >> m;
		vector< vector<int> > field(n, vector<int>(m));
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				cin >> field[i][j];
			}
		}

		solver s(field);

		printf("Case #%d: %s\n", test, s.solve().c_str());
	}
	
	return 0;
}

// nrg 3