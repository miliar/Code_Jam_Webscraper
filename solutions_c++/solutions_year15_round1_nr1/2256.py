#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <set>
#include <queue>
using namespace std;
int const N = 1010;
typedef long long ll;
int n, m[N];
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T; scanf("%d", &T);
	for (int _ = 1; _ <= T; _++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) scanf("%d", &m[i]);
		ll ans0 = 0, ans1 = 0, rate = 0;
		for (int i = 0, tmp; i < n - 1; i++) {
			if ((tmp = m[i] - m[i + 1]) >= 0) {
				ans0 += m[i] - m[i + 1];
				rate = max(rate, ll(tmp));
			}
		}
		for (int i = 0; i < n - 1; i++)
			ans1 += min(rate, ll(m[i]));
		printf("Case #%d: %lld %lld\n", _, ans0, ans1);
	}
	return 0;
}