#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <memory.h>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long ll;

int test = 1;
vector<ll> G;

void solve() {
	ll a, b;
	scanf("%lld %lld", &a, &b);
	printf("Case #%d: %d\n", test++, upper_bound(G.begin(), G.end(), b)-lower_bound(G.begin(), G.end(), a));
}

void init() {
	for(int i=1; i<=1000; i++) {
		ll t = i;
		string str = to_string(t);
		string tmp = str;
		reverse(tmp.begin(), tmp.end());
		if( str == tmp ) {
			t = i*i;
			str = to_string(t);
			tmp = str;
			reverse(tmp.begin(), tmp.end());
			if( tmp == str ) G.push_back(i*i);
		}
	}
}
int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	init();
	int TC;
	scanf("%d", &TC);
	while(TC-->0) solve();
	return 0;
}
