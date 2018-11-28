#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <sstream>
#include <map>
using namespace std;
int t, n, sz, s[10000];
int main() {
	//freopen("in", "r", stdin);
	//freopen("out", "w", stdout);
	cin >> t;
	for (int ctt = 1; ctt <= t; ctt++) {
		int ans = 0;
		cin >> n >> sz;
		for (int i = 0; i < n; i++)
			scanf("%d", &s[i]);
		sort(s, s + n);
		for (int i = n - 1, j = 0; i >= j; i--) {
			if (s[i] + s[j] <= sz && i != j) {
				j++;

			}
			ans++;
		}
		printf("Case #%d: %d\n", ctt, ans);
	}
	return 0;
}