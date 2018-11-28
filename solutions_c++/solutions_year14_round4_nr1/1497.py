#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cmath>
using namespace std;

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T; cin >> T;
	for (int t = 1; t <= T; ++ t) {
		printf("Case #%d: ", t);
		int n, x; 
		static int s[50000]; 
		cin >> n >> x;
		for (int i = 0; i < n; ++ i) {
			scanf("%d", &s[i]); 
		}
		sort(s, s + n); 
		int ans = 0; 
		for (int i = n - 1, j = 0; i >= j; -- i) {
			++ ans;
			if (i > j && s[i] + s[j] <= x) ++ j; 
		}
		printf("%d\n", ans); 
	}
}