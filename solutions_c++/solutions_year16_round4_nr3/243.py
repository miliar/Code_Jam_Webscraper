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
int n, m;
char mas[111][111];
int tt[111][111];
int C[333];

int go (int i, int j, int t) {
	if (i == 0) {
		return tt[i][j];
	}
	if (j == 0) return tt[i][j];
	if (i == n + 1)
		return tt[i][j];
	if (j == m + 1) return tt[i][j];

	if (mas[i][j] == '\\') {
		if (t == 0)
			return go (i, j + 1, 3);
		if (t == 1) 
			return go (i - 1, j, 2);
		if (t == 2)
			return go (i, j - 1, 1);
		return go (i + 1, j, 0);
	}
	if (t == 0)
		return go (i, j - 1, 1);
	if (t == 1) 
		return go (i + 1, j, 0);
	if (t == 2)
		return go (i, j + 1, 3);
	return go (i - 1, j, 2);
}

void load () {
	cin >> n >> m;
	int cur = 1;
	for (int i = 1; i <= m; i++) {
		tt[0][i] = cur++;
	}
	for (int i = 1; i <= n; i++) {
		tt[i][m + 1] = cur++;
	}
	for (int i = m; i >= 1; i--) {
		tt[n + 1][i] = cur++;
	}
	for (int i = n; i >= 1; i--) {
		tt[i][0] = cur++;
	}
	for (int i = 0, last = -1, a; i < n + m + n + m; i++) {
		cin >> a;
		if (last != -1) {
			C[a] = last;
			C[last] = a;
			last = -1;
		}
		else {
			last = a;
		}
	}
}	

void build (int mask) {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			int t = (mask >> (i * m + j)) & 1;
			if (t) {
				mas[i + 1][j + 1] = '\\';
			}
			else {
				mas[i + 1][j + 1] = '/';
			}
		}
	}
}

bool check () {
	int cur = 1;
	for (int i = 1; i <= m; i++) {
		if (C[cur] != go (1, i, 0))
			return false;
		cur++;
	}
	for (int i = 1; i <= n; i++) {
		if (C[cur] != go (i, m, 1)) 
			return false;
		cur++;
	}
	for (int i = m; i >= 1; i--) {
		if (C[cur] != go (n, i, 2)) 
			return false;
		cur++;
	}
	for (int i = n; i >= 1; i--) {
		if (C[cur] != go (i, 1, 3)) 
			return false;
		cur++;
	} 
	return true;
}

string solve () {
	string ans;
	for (int i = 0; i < 1 << (n * m); i++) {
		build (i);
		if (check ()) {
			for (int i = 1; i <= n; i++) {
				ans += '\n';
				for (int j = 1; j <= m; j++) {
					ans += mas[i][j];
				}
			}
			return ans;
		}
	}
	return "\nIMPOSSIBLE";
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