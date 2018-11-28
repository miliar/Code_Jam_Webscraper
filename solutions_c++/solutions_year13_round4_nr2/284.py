#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <string>
#include <cstring>

using namespace std;

typedef pair<int, int> ii;
typedef long long ll;

void solve() {
	ll n, p;
	cin >> n >> p;
	if(p == (1ll << n)) {
		cout << p - 1 << ' ' << p - 1 << endl;
		return;
	}
	p = (1ll << n) - p;
	ll cur = 0;
	ll count1 = 0;
	while(p < (1ll << (n - count1 - 1))) {
		++count1;
	}
	ll count2 = 0;
	while(cur < p) {
		++count2;
		cur += (1ll << (n - count2));
	}
	ll ans1 = 0;
	for(ll i = 1; i <= count1; ++i) {
		ans1 += (1ll << i);
	}
	cout << ans1 << ' ' << (1ll << n) - (1ll << count2) << endl;
}

int main(int argc, char **argv) {
//	freopen("B-sample.in", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int tt;
	scanf("%d", &tt);
	for(int t = 0; t < tt; ++t) {
		printf("Case #%d: ", t + 1);
		solve();
	}

	return 0;
}
