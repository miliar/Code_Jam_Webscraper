#include <bits/stdc++.h>
using namespace std;

#define SZ(x) ((int)(x).size())

int arr[1005];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);
	freopen("A-large (1).in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int t;
	cin >> t;
	int id = 0;
	while (t--) {
		int n;
		cin >> n;
		for (int i = 0; i < n; ++i) {
			cin >> arr[i];
		}
		int way1 = 0;
		int way2 = 0;
		int rate = 0;
		for (int i = 1; i < n; ++i) {
			if (arr[i] < arr[i - 1]) {
				way1 += arr[i - 1] - arr[i];
				rate = max(rate, arr[i - 1] - arr[i]);
			}
		}
		for (int i = 1; i < n; ++i) {
			way2 += min(rate, arr[i - 1]);
		}
		cout << "Case #" << ++id << ": " << way1 << ' ' << way2 << '\n';
	}

	return 0;
}
