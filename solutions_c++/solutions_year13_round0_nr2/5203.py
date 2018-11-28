#include <iostream>
#include <vector>
using namespace std;

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int n, m;
		cin >> n >> m;
		vector < vector <int> > in(n, vector <int> (m));
		vector < vector <int> > pa(n, vector <int> (m, 100));
		int a;
		for (int j = 0; j < n; ++j) {
			for (int k = 0; k < m; ++k) {
				cin >> a;
				in[j][k] = a;
			}
		}

		for (int j = 0; j < n; ++j) {
			int max = 0;
			for (int k = 0; k < m; ++k) {
				if (in[j][k] > max) max = in[j][k];
			}
			for (int k = 0; k < m; ++k) {
				if (max < pa[j][k]) pa[j][k] = max;
			}
		}

		for (int k = 0; k < m; ++k) {
			int max = 0;
			for (int j = 0; j < n; ++j) {
				if (in[j][k] > max) max = in[j][k];
			}
			for (int j = 0; j < n; ++j) {
				if (max < pa[j][k]) pa[j][k] = max;
			}
		}

		bool found = true;

		for (int j = 0; j < n; ++j) {
			for (int k = 0; k < m; ++k) {
				if (in[j][k] != pa[j][k]) found = false;
			}
		}

		cout << "Case #" << i+1 << ": ";
		if (!found) cout << "NO";
		else cout << "YES";
		cout << endl;
	}
}