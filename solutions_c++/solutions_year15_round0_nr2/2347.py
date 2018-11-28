#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
	int t;
	freopen("input.txt", "r", stdin);
	freopen("outputbrute.txt", "w", stdout);

	cin >> t;
	for (int test = 0; test < t; test++) {
		cout << "Case #" << test + 1 << ": ";
		int n;
		cin >> n;
		vector <int> v;
		for (int i = 0; i < n; i++) {
			int a;
			cin >> a;
			v.push_back(a);
		}
		sort(v.begin(), v.end());
		reverse(v.begin(), v.end());
		int to = v[0];
		int ans = v[0];
		for (int i = 1; i < to; i++) {
			int cur = i;
			for (int j = 0; j < v.size(); j++)
				cur += (v[j] / i) - (v[j] % i == 0);
			if (cur < ans)
				ans = cur;
		}
		cout << ans << endl;
	}
}