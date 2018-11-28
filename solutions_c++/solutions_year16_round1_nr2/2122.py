#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <queue>
#include <assert.h>

using namespace std;

struct Compare {
	bool operator() (const vector<int>& a, const vector<int>& b) const
	{
		for (int i = 0; i < a.size(); i++) {
			if (a[i] != b[i]) {
				return a[i] < b[i];
			}
		}
		return false;
	}
};

void test()
{
	int N;
	cin >> N;
	vector<vector<int>> vv(2 * N - 1, vector<int>(N, 0));
	for (int i = 0; i < 2 * N - 1; i++) {
		for (int j = 0; j < N; j++) {
			cin >> vv[i][j];
		}
	}

	sort(vv.begin(), vv.end(), Compare());

	vector<vector<int>> M(N, vector<int>(N, 0));
	vector<bool> rowsUsed(N, false);
	vector<bool> colsUsed(N, false);
	vector<bool> used(2 * N - 1, false);
	for (int k = 0; k < 2 * N - 1; k++) {
		bool skip = false;
		for (int i = 0; i < N; i++) {
			int rowCount = 0;
			int rowQ = 0;
			int colCount = 0;
			int colQ = 0;
			for (int q = 0; q < 2 * N - 1; q++) {
				if (used[q]) continue;
				const auto& v = vv[q];
				if (!rowsUsed[i]) {
					bool success = true;
					for (int j = 0; j < N; j++) {
						if (M[i][j] != 0 && v[j] != M[i][j]) {
							success = false;
							break;
						}
					}
					if (success) {
						rowCount++;
						rowQ = q;
					}
				}
				if (!colsUsed[i]) {
					bool success = true;
					for (int j = 0; j < N; j++) {
						if (M[j][i] != 0 && v[j] != M[j][i]) {
							success = false;
							break;
						}
					}
					if (success) {
						colCount++;
						colQ = q;
					}
				}
			}
			if (rowCount == 1 && !(colCount == 1 && rowQ == colQ)) {
				//assert(colCount != 1);
				rowsUsed[i] = true;
				used[rowQ] = true;
				for (int j = 0; j < N; j++) {
					M[i][j] = vv[rowQ][j];
				}
				skip = true;
				break;
			} else if (colCount == 1 && !(rowCount == 1 && rowQ == colQ)) {
				//assert(rowCount != 1);
				colsUsed[i] = true;
				used[colQ] = true;
				for (int j = 0; j < N; j++) {
					M[j][i] = vv[colQ][j];
				}
				skip = true;
				break;
			}
		}

		if (skip) {
			continue;
		}
		for (int q = 0; q < 2 * N - 1; q++) {
			if (used[q]) continue;
			const auto& v = vv[q];
			bool success = true;
			// ∆адно впихиваем
			for (int i = 0; i < N; i++) {
				success = true;
				if (!rowsUsed[i]) {
					// ѕытаемс€ впихнуть строчку
					for (int j = 0; j < N; j++) {
						if (M[i][j] != 0 && v[j] != M[i][j]) {
							success = false;
							break;
						}
					}
					if (success) {
						rowsUsed[i] = true;
						used[q] = true;
						for (int j = 0; j < N; j++) {
							M[i][j] = v[j];
						}
						break;
					}
				}

				// ѕытаемс€ впихнуть колонку
				success = true;
				if (!colsUsed[i]) {
					for (int j = 0; j < N; j++) {
						if (M[j][i] != 0 && v[j] != M[j][i]) {
							success = false;
							break;
						}
					}
					if (success) {
						colsUsed[i] = true;
						used[q] = true;
						for (int j = 0; j < N; j++) {
							M[j][i] = v[j];
						}
						break;
					}
				}
			}
			assert(success);
			break;
		}
	}

	for (int i = 0; i < N; i++) {
		if (!rowsUsed[i]) {
			for (int j = 0; j < N; j++) {
				cout << M[i][j] << " ";
			}
		}
	}
	for (int j = 0; j < N; j++) {
		if (!colsUsed[j]) {
			for (int i = 0; i < N; i++) {
				cout << M[i][j] << " ";
			}
		}
	}
}

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		test();
		cout << endl;
	}
	return 0;
}
