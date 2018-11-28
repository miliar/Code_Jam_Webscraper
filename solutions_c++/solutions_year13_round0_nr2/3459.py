#include <iostream>
using namespace std;
int n, m;
int r_max(int l[101][101], int s) {
	int max = 0;
	for (int i=0; i<m; ++i) {
		if (l[s][i]>max) max = l[s][i];
	}
	return max;
}

int c_max(int l[101][101], int s) {
	int max = 0;
	for (int i=0; i<n; ++i) {
		if (l[i][s]>max) max = l[i][s];
	}
	return max;
}

int main() {
	int t;
	cin >> t;
	for (int i=0; i<t; ++i) {
		int res = 1;
		cin >> n >> m;
		int l[101][101] = {0};
		int maxR[101] = {0};
		int maxC[101] = {0};
		for (int j=0; j<n; ++j) {
			for (int k=0; k<m; ++k) {
				cin >> l[j][k];
			}
		}
		for (int j=0; j<n; ++j) {
			maxR[j] = r_max(l, j);
		}
		for (int j=0; j<m; ++j) {
			maxC[j] = c_max(l,j);
		}
		for (int j=0; j<n; ++j) {
			for (int k=0; k<m; ++k) {
				if (l[j][k]<maxC[k] && l[j][k]<maxR[j]) {
					res = 0;
				}
			}
		}
		if (res) {
			cout << "Case #" << i+1 << ": " << "YES" << endl;
		}
		else {
			cout << "Case #" << i+1 << ": " << "NO" << endl;
		}
	}
}
