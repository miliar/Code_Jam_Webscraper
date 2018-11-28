#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <ctime>

using namespace std;

#define sqr(a) ((a)*(a))
#define two(a) (1 << (a))
#define has(mask, a) ((mask) & two(a) ? 1 : 0)

long long  n, p;

void load() {
	cin >> n >> p;
}

bool can1 (long long a) {
 	long long left = a, cur = 0;

 	int i = n - 1;

 	while (true) {                 	
 		if (left == 0) {
 		 	return cur < p;
 		}

 		cur += (1ll << i);
 		i--;
 		left = (left - 1) / 2;
 	}

 	return false;
}

bool can2 (long long a) {
 	long long left = (1ll << n) - a - 1, cur = 0;

 	int i = n - 1;

 	while (true) {
 	 	if (left == 0) {
 	 		return (1ll << n) - cur - 1 < p;
 	 	}

 	 	cur += (1ll << i);
 	 	i--;
 	 	left = (left - 1) / 2;
 	}
 	return false;
}

void solve(int test) {
	long long ans1 = 0, ans2 = 0, lo = 0, ri = (1ll << n) - 1;

	while (lo <= ri) {
	 	long long mid = (lo + ri) / 2;

	 	if (can1 (mid)) {
	 	 	ans1 = max (ans1, mid);
	 	 	lo = mid + 1;
	 	} else {
	 	 	ri = mid - 1;
	 	}
	}

	lo = 0, ri = (1ll << n) - 1;

	while (lo <= ri) {
	 	long long mid = (lo + ri) / 2;

	 	if (can2 (mid)) {
	 	 	ans2 = max (ans2, mid);
	 	 	lo = mid + 1;
	 	} else {
	 	 	ri = mid - 1;
	 	}
	}

	printf ("Case #%d: %lld %lld\n", test, ans1, ans2);
}

int main() {
 	freopen ("a.in", "r", stdin);
 	freopen ("a.out", "w", stdout);

 	int t;
 	scanf ("%d\n", &t);

 	for (int i = 1;i <= t;i++) {
 		load();
 		solve(i);
 	}

 	return 0;
}