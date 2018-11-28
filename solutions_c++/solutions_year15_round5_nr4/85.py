#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>


typedef long long ll;
typedef long double ld;

using namespace std;

const int MAXN = 20000;

ll e[MAXN];
ll cnt[MAXN];
int k;
ll ans[MAXN];


void slv(int l, int n) {
	if (n == l) {
		return;
	}
	int go = 0;
	for (int i = 0; i < k; ++i)
		if (cnt[i]) {
			go = e[i];
			--cnt[i];
			break;
		}
	ans[l] = go;
	if (go == 0) {
		for (int i = 0; i < k; ++i)
			cnt[i] /= 2;
	}
	else {
		int nx = 0;
		for (int i = 0; i < k; ++i) {
			if (cnt[i]) {
				while (e[nx] < e[i] + go)
					++nx;
				cnt[nx] -= cnt[i];
			}
		}
	}
	slv(l + 1, n);
}

void solve() {
	scanf("%d", &k);
	for (int i = 0; i < k; ++i) {
		scanf("%lld", &e[i]);
	}
	ll sum = 0;
	for (int i = 0; i < k; ++i)
		scanf("%lld", &cnt[i]), sum += cnt[i];
	int n = 1;
	while ((1ll << n) < sum)
		++n;
	--cnt[0];

	slv(0, n);

	for (int i = 0; i < n; ++i) {
		cout << ans[i] << " ";
	}
	cout << "\n";

}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int i = 1; i <= tt; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}


