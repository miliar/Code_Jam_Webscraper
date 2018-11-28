#include "bits/stdc++.h"

typedef long long ll;
typedef unsigned long long ull;
typedef double dbl;

using namespace std;

#ifdef LOCAL
#include "debug.h"
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define Print(...) (void)42;
#define eprintf(...) (void)42;
#endif

int T;
int n;
int ans;
int p[1111];

void solve () {
	for (int mask = 1; mask < 1 << n; mask++) {
		vector<int> T;

		for (int j = 0; j < n; j++) {
			if ((mask >> j) & 1)
				T.push_back (j);
		}

		if ((int) T.size () <= ans) continue;

		do {
			int cnt = 0;
			for (int i = 0; i < (int) T.size (); i++) {
				int l = (i - 1 + T.size ()) % T.size ();
				int r = (i + 1) % T.size ();
				if (p[T[i]] == T[l] || p[T[i]] == T[r]) {
					cnt++;
				}
			}
			if (cnt == (int) T.size ()) ans = max (ans, (int) T.size ());
		} while (next_permutation (T.begin (), T.end ()) && (int) T.size () > ans);
	}
}

int main () {
#ifdef LOCAL
	freopen ("file.in", "r", stdin);
	freopen ("file.out", "w", stdout);
#else
	//freopen (".in", "r", stdin);
	//freopen (".out", "w", stdout);
#endif 

#ifdef TIMER
	timer Tm;
	Tm.start ();
#endif

	ios_base::sync_with_stdio (false);
	
	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> p[i];
			p[i]--;
		}
		ans = 0;
		solve ();
		cout << "Case #" << tc << ": " << ans << "\n";
		clog << tc << endl;
	}
	
#ifdef TIMER
	Tm.stop ();
	Tm.print_time (stderr);
#endif

	return 0;
}