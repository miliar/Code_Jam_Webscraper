#include <cstdio>
#include <algorithm>

using namespace std;

#define ll long long

const int N = 110;

ll k,c,s;

inline void solve () {
	scanf ("%lld %lld %lld", &k, &c, &s);

	if (c == 1) {
		if (s == k) {
			for (ll i = 1;i <= k;i ++) {
				printf ("%lld ", i);
			}
			printf ("\n");
		} else {
			printf ("IMPOSSIBLE\n");
		}
	} else if (s+s >= k) {
		ll step = 1;
		for (int i = 1;i < c;i ++) {
			step *= k;
		}
		for (ll i = 1;i <= k;i += 2) {
			printf ("%lld ", min (step*k, (i-1)*step+i+1));
		}
		printf ("\n");
	} else {
		printf ("IMPOSSIBLE\n");
	}
}

int main () {
	int t;
	scanf ("%d", &t);

	for (int i = 1;i <= t;i ++) {
		printf ("Case #%d: ", i);

		solve ();
	}
}