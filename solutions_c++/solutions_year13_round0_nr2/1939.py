#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

bool check(vvi &lawn, int n, int m) {
	int desired = lawn[n][m];
	bool c1 = true;
	bool c2 = true;

	for (int i = 0; i < lawn[0].size() && c1; ++i) {
		if (lawn[n][i] > desired) c1 = false;
	}

	for (int i = 0; i < lawn.size() && c2; ++i) {
		if (lawn[i][m] > desired) c2 = false;
	}

	return (c1 || c2);
}

int main() {
	int t;
	cin >> t;

	for (int tt = 0; tt < t; ++tt) {
		int n, m;
		cin >> n >> m;

		vvi desired_lawn(n, vi(m));
		for (int nn = 0; nn < n; ++nn) {
			for (int mm = 0; mm < m; ++mm) {
				cin >> desired_lawn[nn][mm];
			}
		}

		bool valid = true;
		for (int nn = 0; nn < n && valid; ++nn) {
			for (int mm = 0; mm < m && valid; ++mm) {
				valid = check(desired_lawn, nn, mm);
			}
		}

		cout << "Case #" << tt + 1 << ": ";
		if (valid) cout << "YES";
		else cout << "NO";
		cout << endl;
	}
}