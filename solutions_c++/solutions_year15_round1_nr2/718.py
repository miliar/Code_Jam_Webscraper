#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

typedef long long ll;
const ll oo = ll(1e16);
int n, b, a[100000];

int ok(ll x){
	ll sum = 0LL;
	for(int i = 0; i < b; ++i){
		sum += x / a[i] + 1;
		if (sum >= n) return 0;
	}
	return 1;
}

void solve(){
	scanf("%d%d", &b, &n);
	for(int i = 0; i < b; ++i) scanf("%d", a + i);
	if (n <= b){
		printf("%d\n", n);
		return;
	}
	ll l = 0LL, r = oo;
	while (l < r){
		ll mid = (l + r + 1) >> 1;
		if (ok(mid)) l = mid;
		else r = mid - 1;
	}
	ll sum = 0LL;
	for(int i = 0; i < b; ++i) sum += l / a[i] + 1;
		//cout << l << ' ' << sum << endl;
	int lastpos = 0;
	for(int i = b - 1; i >= 0; --i)
		if (l % a[i] == 0) lastpos = i;
	while (1){
		++l;
		for(int i = 0; i < b; ++i){
			sum += ((l % a[i]) == 0);
			if (sum >= n){
				printf("%d\n", i + 1);
				return;
			}
		}
		lastpos = 0;
	}
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for(int t = 1; t <= tc; ++t){
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}