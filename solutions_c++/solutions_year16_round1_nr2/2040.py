#include <vector>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	int n, x;
	int last;
	int first;
	
	cin >> tests;
	for (int t = 1; t <= tests; t++) {
		cin >> n;
		int app[2501];
		fill(app, app + 2501, 0);
		vector<int> sol;
		
		for (int i = 0; i < 2 * n - 1; i++) {
			for (int j = 0; j < n; j++) {
				cin >> x;
				app[x]++;
			}
		}

		for (int i = 1; i <= 2500; i++) {
			if (app[i] % 2 != 0) sol.push_back(i);
		}

		sort(sol.begin(), sol.end());


		cout << "Case #" << t << ": ";

		for (int i = 0; i < n; i++) {
			cout << sol[i] << " ";
		}

		cout << "\n";
	}

	return 0;
}