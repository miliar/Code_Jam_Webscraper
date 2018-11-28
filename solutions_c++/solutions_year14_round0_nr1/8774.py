#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small-attempt0.out", "wt", stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		int arr[32] = {0};
		for (int i = 0; i < 2; ++i) {
			int r;
			cin >> r, --r;
			int grid[4][4];
			for (int j = 0; j < 4; ++j)
				for (int k = 0; k < 4; ++k)
					cin >> grid[j][k];
			for (int j = 0; j < 4; ++j)
				++arr[grid[r][j]];
		}
		int temp = count(arr, arr + 32, 2);
		cout << "Case #" << t + 1 << ": ";
		if (temp == 1)
			cout << (find(arr, arr + 32, 2) - arr);
		else if (temp > 1)
			cout << "Bad magician!";
		else
			cout << "Volunteer cheated!";
		cout << "\n";
	}
	return 0;
}
