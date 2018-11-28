#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

typedef long long ll;



void solve() {
	int n, x;
	scanf("%d%d", &n, &x);
	vector<int> a(n);
	vector<bool> used(n, false);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &a[i]);
	}
	sort(a.rbegin(), a.rend());
	int ans = 0;
	for (int i = 0; i < n; ++i) {
		if (!used[i]) {
			used[i] = true;
			int j = -1;
			for (int k = 0; k < n; ++k) {
				if (!used[k] && a[k] <= x - a[i]) {
					j = k;
					break;
				}
			}
			if (j != -1) {
				used[j] = true;
			}
			ans++;
		}
	}
	printf("%d", ans);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
		printf("\n");
	}
	return 0;
}