#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
	int T;

	cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		int n, x;
		cin >> n >> x;
		vector<int> a;
		for (int i = 0; i < n; i++) {
			int t;
			cin >> t;
			a.push_back(t);
		}
		sort(a.begin(), a.end());
		int ans = 0;
		for (int i = 0, j = n - 1; i <= j; ) {
			if (i == j) {
				ans++;
				break;
			} else if (a[i] + a[j] <= x) {
				i++, j--;
				ans++;
			} else {
				j--;
				ans++;
			}
		}

		printf("Case #%d: %d\n", ti, ans);
	}

	return 0;
}
