# include <string>
# include <fstream>
# include <algorithm>
# include <set>
# include <map>
# include <iostream>
# include <vector>
using namespace std;

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");


	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		int n, x;
		cin >> n >> x;
		vector<int> f(n);
		for (int i = 0; i < n; i++) {
			cin >> f[i];
		}
		sort(f.begin(), f.end());
		reverse(f.begin(), f.end());

		int ans = 0;

		int l = 0, r = f.size() - 1;
		while (l <= r) {
			ans++;
			if (r > l && f[r] + f[l] <= x) {
				r--;
			}
			l++;
		}
		cout << "Case #" << test << ": " << ans << endl;
	}

	return 0;
}