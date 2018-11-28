#include <iostream>
#include <stdlib.h>
#include <float.h>
#include <math.h>

using namespace std;

bool test(int state[100][100], int i, int j, int n, int m) {
	bool success = true;
	int t = 0;
	for (t = 0; t < n; ++t) {
		if (state[i][j] < state[t][j]) {
			success = false;
			break;
		}
	}
	if (success)
		return true;
//	if (!success)
//		cout << "\t t: " << t << endl;
	success = true;
	int k = 0;
	for (k = 0; k < m; ++k) {
		if (state[i][j] < state[i][k]) {
			success = false;
			break;
		}
	}
//	if (!success)
//		cout << "\t k: " << k << endl;
	return success;
}

void print(int state[100][100], int n, int m) {
	cout << endl;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			cout << state[i][j] << " ";
		}
		cout << endl;
	}
}

int main(int argc, char **argv) {
	int testCount = 0;
	int state[100][100];
	cin >> testCount;
	char dummy;
	int n;
	int m;
	for (int i = 0; i < testCount; ++i) {
		cin >> n;
		cin >> m;
		for (int j = 0; j < n; ++j) {
			for (int t = 0; t < m; ++t) {
				cin >> state[j][t];
			}
		}
		bool success = true;
		for (int j = 0; j < n && success; ++j) {
			for (int t = 0; t < m; ++t) {
				bool res = test(state, j, t, n, m);
				if (!res) {
					success = false;
//					cout << "\tj: " << j << " t: " << t << endl;
					break;
				}
			}
		}
		if (success) {
//			print(state, n, m);
			cout << "Case #" << (i + 1) << ": YES" << endl;
		} else {
//			print(state, n, m);
			cout << "Case #" << (i + 1) << ": NO" << endl;
		}
	}
}
