#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int N, M;
int a[105][105];
int h[105][105];

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> N >> M;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++) {
				h[i][j] = 100;
				cin >> a[i][j];
			}
		// For each row, find the max height across all cols; make a slice
		for (int i = 0; i < N; i++) {
			int v = 0;
			for (int j = 0; j < M; j++)
				v = max(v, a[i][j]);
			for (int j = 0; j < M; j++)
				h[i][j] = min(v, h[i][j]);
		}
		// For each col, find the max; make a slice down the col
		for (int j = 0; j < M; j++) {
			int v = 0;
			for (int i = 0; i < N; i++)
				v = max(v, a[i][j]);
			for (int i = 0; i < N; i++)
				h[i][j] = min(v, h[i][j]);
		}
		string res = "YES";
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				if (h[i][j] != a[i][j])
					res = "NO";
		cout << "Case #" << icase << ": " << res << endl;
	}
	return 0;
}
