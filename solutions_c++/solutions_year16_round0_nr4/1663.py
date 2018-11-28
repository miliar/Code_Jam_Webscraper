#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <tuple>
#include <queue>
#include <utility>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <limits>
#include <new>
#include <functional>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main(void) {
	cin.tie(nullptr);
	cin.sync_with_stdio(false);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int k, c, s;
		cin >> k >> c >> s;
		if (k == 1) {
			cout << "Case #" << i << ": 1\n";
			continue;
		}
		if (c == 1 && s != k) {
			cout << "Case #" << i << ": IMPOSSIBLE\n";
			continue;
		}
		if (c == 1 && s == k) {
			cout << "Case #" << i << ": ";
			for (int j = 0; j < k; j++) {
				cout << j + 1 << (j == k - 1 ? '\n' : ' ');
			}
			continue;
		}
		if (s >= k - 1) {
			cout << "Case #" << i << ": ";
			for (int j = 0; j < k - 1; j++) {
				cout << j + 2 << (j == k - 2 ? '\n' : ' ');
			}
			continue;
		}
		
	}

	return 0;
}