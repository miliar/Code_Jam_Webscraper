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
#include <numeric>

using namespace std;

#define sqr(a) ((a)*(a))
#define two(a) (1 << (a))
#define has(mask, a) ((mask) & two(a) ? 1 : 0)

int n, x, was[10004], s[10004];

void load() {
	cin >> n >> x;
	for (int i = 0;i < n;i++) {
		scanf ("%d", &s[i]);
	}
	sort (s, s + n);
}

void solve(int test) {
	int ans = 0;

	multiset <int> a;
	for (int i = n - 1;i >= 0;i--) {
		if (a.lower_bound (s[i]) == a.end()) {
			ans++;
			a.insert (x - s[i]);
		} else {
			set <int>::iterator it = a.lower_bound (s[i]);
			a.erase (it);
		}
	}

	printf ("Case #%d: %d\n", test, ans);
}

int main() {
	#ifdef MY_LOCAL
 		freopen ("a.in", "r", stdin);
 	#endif

 	int t;
 	cin >> t;
 	for (int i = 0;i < t;i++) {
 		load();
 		solve(i + 1);
 	}

 	return 0;
}