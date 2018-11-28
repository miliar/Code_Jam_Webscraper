#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <set>
#include <algorithm>

using namespace std;

const int MAXN = 710;

int n, x, y;
int cnt[MAXN];

void solve(int test_id) {
	cout << "Case #" << test_id << ": ";
	memset(cnt, 0, sizeof(cnt));

	cin >> n >> x;
	for (int i = 0; i < n; ++i) {
		cin >> y;
		cnt[y]++;
	}

	int mid = (x / 2) + (x % 2);
	int result = 0;
	for (int i = x; i >= mid; --i) {
		result += cnt[i];
		int t = cnt[i];
		for (int j = 1; j <= x - i && t > 0; ++j) {
			if (t >= cnt[j]) {
				t -= cnt[j];
				cnt[j] = 0;
			}
			else {
				cnt[j] -= t;
				t = 0;
			}
		}
	}
	int last = 0;
	for (int i = mid - 1; i >= 1; --i)
		last += cnt[i];
	result += (last / 2) + (last % 2);

	cout << result << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int test_id = 1; test_id <= t; ++test_id)
		solve(test_id);
	return 0;
}
