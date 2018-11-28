#include <cstdio>
#include <iostream>
#include <algorithm>
#define ll long long
using namespace std;

bool seen[10]; 
int cnt;

void go(ll a) {
	while (a > 0) {
		if (seen[a%10] == 0) {
			cnt++;
			seen[a%10] = 1;
		}
		a /= 10;
	}
}

ll solve(ll a) {
	for (int i = 0; i < 10; i++) seen[i] = 0;
	cnt = 0;
	for (int i = 1; i <= 200; i++) {
		go(i*a);
		if (cnt == 10) {
			return i*a;
		}
	}
	return -1;
}	

int main() {
	ll T; scanf("%lld", &T);
	for (int k = 1; k <= T; k++) {
		ll d;
		scanf("%lld", &d);
		ll ans = solve(d);
		if (ans == -1) {
			printf("Case #%d: INSOMNIA\n", k);
		}
		else {
			printf("Case #%d: %lld\n", k, solve(d));
		}
	}
	return 0;
}