#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define mp make_pair
#define pb push_back
typedef long long ll;

int N, K, X[100];
ll P, R;
bool check(ll x) {
	ll l = x;
	for (int i=0; i<N; i++) {
		if (X[i] == 1) {
			l -= 1;
			l /= 2;
		} else {
			if (l > 0) return false;
		}
	}
	return true;
}

bool check2(ll x) {
	ll l = x;
	ll r = R - x - 1;
	for (int i=0; i<N; i++) {
		//printf("%d %lld %lld %d\n", i, l, r, X[i]);
		if (X[i] == 0) {
			if (r <= 0) return false;
			r -= 1;
			r /= 2;
		} else {
			if (r > 0) return true;
			
			if (r <= l) {
				l -= r;
				l /= 2;
			} else {
				r = l + (r - l) / 2;
				l = 0;
			}
		}
		
	}
	return true;
}

int main() {
	int i, j, T, TC = 1;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%lld", &N, &P); P -= 1;
		for (i=N-1; i>=0; i--) {
			X[i] = P%2;
			P /= 2;
		}

		for (K=0; K<N & X[K] == 1; K++);
		//printf("%d\n", K);

		R = 1;
		for (i=0; i<N; i++) R *= 2;

		//printf("-%d\n", check2(5));
		//break;

		ll l=0, r = R - 1;
		ll ans1 = r;
		while (l <= r) {
			//printf("%lld %lld\n", l, r);
			ll mid = (l + r) / 2;
			if (check(mid)) {
				ans1 = mid;
				l = mid + 1;
			} else r = mid - 1;
		}

		l=0, r = R - 1;
		ll ans2 = l;
		while (l <= r) {
			//printf("%lld %lld\n", l, r);
			ll mid = (l + r) / 2;
			if (check2(mid)) {
				ans2 = mid;
				l = mid + 1;
			} else r = mid - 1;
		}

		printf("Case #%d: %lld %lld\n", TC++, ans1, ans2);
	}
}