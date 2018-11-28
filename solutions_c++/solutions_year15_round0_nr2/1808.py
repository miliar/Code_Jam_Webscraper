#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

const int MAX_N = 1000 + 10;
int a[MAX_N], n;

int main() {
	int T;
	cin >> T;
	for (int it = 1; it <= T; ++it) {
		cin >> n;
		for (int i = 0; i < n; ++i) {
			cin >> a[i];
		}

		int ans = *max_element(a, a + n);

		for (int after = 1; after <= ans; ++after) {
			int need = 0;
			for (int i = 0; i < n; ++i) {
				need += (a[i] - 1) / after;
			}
			ans = min(ans, need + after);
		}
		printf("Case #%d: %d\n", it, ans);
	}
}
