#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int solve(vector <int> &w, int n, int x) {
	int ans = 0;
	sort(w.begin(), w.end());
	for (int i = n - 1; i >= 0; --i) {
		if (w[i] != -1) {
			for (int j = i - 1; j >= 0; --j) {
				if (w[j] != -1) {
					if (w[i] + w[j] <= x) {
						++ans;
						w[j] = -1;
						w[i] = -1;
						break;
					}
				}
			}
		}
		if (w[i] != -1) {
			w[i] = -1;
			++ans;
		}
	}
	return ans;
}

/*int solve(vector <int> &w, int n, int x, int disk) {
	int f = false;
	for (int i = 0; i < n; ++i) {
		if (w[i] != -1) {
			f = true;
			break;
		}
	}
	if (f) {
		int best = 1000 * 1000 * 1000;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (i != j && w[i] != -1 && w[j] != -1) {
					if (w[i] + w[j] <= x) {
						int a = w[i];
						int b = w[j];
						w[i] = -1;
						w[j] = -1;
						best = min(best, solve(w, n, x, disk + 1) + 1);
						w[i] = a;
						w[j] = b;
					}
				}
			}
		}
		for (int i = 0; i < n; ++i) {
			if (w[i] != -1) {
				int a = w[i];
				w[i] = -1;
				best = min(best, solve(w, n, x, disk + 1) + 1);
				w[i] = a;
			}
		}
		return best;
	}
	else return 0;
}*/
int main() {
	freopen("A-large.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int T; cin >> T;
	for (int t = 0; t < T; ++t) {
		vector <int> w;
		int n, x;
		cin >> n >> x;
		for (int i = 0; i < n; ++i) {
			int w0;
			cin >> w0;
			w.push_back(w0);
		}
		cout << "Case #" << t + 1 << ": ";
		cout << solve(w, n, x);
		cout << endl;
	}

}