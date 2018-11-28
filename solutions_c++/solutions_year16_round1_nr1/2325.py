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

string s;
string ans;
int T;
string dp[1111];

void solve () {
	dp[0] = s[0];
	for (int i = 1; i < (int) s.size (); i++) {
		dp[i] = max (s[i] + dp[i - 1], dp[i - 1] + s[i]);
	}

	ans = s;

	for (int i = 1; i < (int) s.size (); i++) {
		ans = max (ans, s[i] + dp[i - 1] + s.substr (i + 1, s.size () - i));
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
		cin >> s;
		ans = "";
		solve ();
		cout << "Case #" << tc << ": " << ans << "\n";
	}
	
#ifdef TIMER
	Tm.stop ();
	Tm.print_time (stderr);
#endif

	return 0;
}