#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

ifstream fin("B-small-attempt0.in");
ofstream fout("out.txt");

vector<vector<int>> a;
int n;
int res_matr[50][50];
bool used_row[50];
bool used_col[50];

bool comp(vector<int> i, vector<int> j) {
	int k = 0;
	while (k < n && i[k] == j[k]) {
		++k;
	}
	if (k == n) {
		return false;
	}
	return i[k] < j[k];
}

bool matches(int i, int j, bool row) {
	for (int x = 0; x < n; ++x) {
		if (row) {
			if (res_matr[j][x] != 0 && a[i][x] != res_matr[j][x]) {
				return false;
			}
			if (j > 0 && res_matr[j - 1][x] >= a[i][x]) {
				return false;
			}
			if (j < n - 1 && res_matr[j + 1][x] <= a[i][x] && res_matr[j + 1][x] != 0) {
				return false;
			}
		} else {
			if (res_matr[x][j] != 0 && a[i][x] != res_matr[x][j]) {
				return false;
			}
			if (j > 0 && res_matr[x][j - 1] >= a[i][x]) {
				return false;
			}
			if (j < n - 1 && res_matr[x][j + 1] <= a[i][x] && res_matr[x][j + 1] != 0) {
				return false;
			}
		}
	}
	return true;
}

bool build(int cur) {
	if (cur == 2 * n - 1) {
		return true;
	}

	for (int i = 0; i < n; ++i) {
		if (matches(cur, i, true) && !used_row[i]) {
			used_row[i] = true;
			int temp[50];
			for (int j = 0; j < n; ++j) {
				temp[j] = res_matr[i][j];
				res_matr[i][j] = a[cur][j];
			}

			if (build(cur + 1)) {
				return true;
			}

			used_row[i] = false;
			for (int j = 0; j < n; ++j) {
				res_matr[i][j] = temp[j];
			}
		}
	}

	for (int i = 0; i < n; ++i) {
		if (matches(cur, i, false) && !used_col[i]) {
			used_col[i] = true;
			int temp[50];
			for (int j = 0; j < n; ++j) {
				temp[j] = res_matr[j][i];
				res_matr[j][i] = a[cur][j];
			}

			if (build(cur + 1)) {
				return true;
			}

			used_col[i] = false;
			for (int j = 0; j < n; ++j) {
				res_matr[j][i] = temp[j];
			}
		}
	}

	return false;
}

int main() {
	int tests;
	fin >> tests;

	for(int test = 0; test < tests; ++test) {
		int ans[50];
		fin >> n;
		int x;
		a.resize(2 * n - 1);
		for (int i = 0; i < 2 * n - 1; ++i) {
			a[i].clear();
			for (int j = 0; j < n; ++j) {
				fin >> x;
				a[i].push_back(x);
			}
		}

		sort(a.begin(), a.end(), comp);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				res_matr[i][j] = 0;
			}
		} 
		memset(used_row, 0, sizeof(used_row));
		memset(used_col, 0, sizeof(used_col));

		bool done = build(0);

		for (int i = 0; i < n; ++i) {
			if (!used_row[i]) {
				for (int j = 0; j < n; ++j) {
					ans[j] = res_matr[i][j];
				}
			}
		}

		for (int i = 0; i < n; ++i) {
			if (!used_col[i]) {
				for (int j = 0; j < n; ++j) {
					ans[j] = res_matr[j][i];
				}
			}
		}

		fout << "Case #" << test + 1 << ": ";
		for (int i = 0; i < n; ++i) {
			fout << ans[i] << " ";
		}
		fout << endl;
	}

	return 0;
}
