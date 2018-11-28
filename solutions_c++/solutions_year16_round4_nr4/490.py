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
string mas[4];
int ttt[4];
int cn[4];
vector<char> pos;
char was[4];
int ans;

void load () {
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> mas[i];
		ttt[i] = 0;
		for (int j = 0; j < n; j++) {
			mas[i][j] -= '0';
			ttt[i] |= ((int) mas[i][j]) << j;
		}
	}
}

bool can (int i, int j) {
	return (cn[i] >> j) & 1;  
}

bool check (int ps = 0) {
	if (ps == n) {
		return false;
	}
	bool res = false;
	int cnt = 0;
	int cn = 0;
	for (int i = 0; i < n && !res; i++) {
		if (was[i]) continue;
		if (can (pos[ps], i)) {
			cn++;
			was[i] = 1;
			res |= (check (ps + 1));
			was[i] = 0;
		}
	}
	res |= cn == 0;
	return res;
}

void build (int p = 0, int add = 0) {
	if (p == n) {
		pos.resize (n);
		for (int i = 0; i < n; i++) {
			pos[i] = i;
		}
		do {
		if (check ()) return;
		} while (next_permutation (pos.begin (), pos.end ()));
		ans = min (ans, add);
		return;
	}
	for (int i = 0; i < 1 << 4; i++) {
		cn[p] = ttt[p] | i;
		build (p + 1, add + __builtin_popcount (i));
	} 
}

int solve () {
	ans = 1e9;
	pos.resize (n);
	
	build ();

	return ans;
}

void clear () {
}

int main () {
#ifdef LOCAL
	freopen ("file.in", "r", stdin);
	freopen ("file.out", "w", stdout);
	//freopen ("file.log", "w", stderr);
#else
	freopen (".in", "r", stdin);
	freopen (".out", "w", stdout);
#endif 

#ifdef TIMER
	timer Tm;
	Tm.start ();
#endif

	ios_base::sync_with_stdio (false);

	cin >> T;
	cout.precision (15);
	cout << fixed << showpoint;

	for (int tc = 1; tc <= T; tc++) {
		load ();
		cout << "Case #" << tc << ": " << solve () << endl;
		clear ();
		clog << tc << endl;
	}

#ifdef TIMER
	Tm.stop ();
	Tm.print_time (stderr);
#endif

	return 0;
}