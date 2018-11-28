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
int n, k;
double p[333];

void load () {
	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		cin >> p[i];	
	}
}

bool next_combination (vector<int> &a, int n) {
	int k = (int) a.size (); 
	for (int i = k - 1; i >= 0; i--) {
		if (a[i] + k - i < n) {
			a[i]++;
			for (int j = i + 1; j < k; j++) {
				a[j] = a[j - 1] + 1;
			}
			return true;
		}		
	}
	return false;
}
	
double solve () {
	double mx = 0;
	vector<int> q (k);
	for (int i = 0; i < k; i++) {
		q[i] = i;
	}

	do {
		double tot = 0;
		vector<int> pos (k >> 1);
		for (int i = 0; i < (int) pos.size (); i++) {
			pos[i] = i;
		}
		do {
			double p1 = 1;
			set<int> was;
			for (int i = 0; i < (int) pos.size (); i++) {
				was.insert (pos[i]);
			}
			for (int i = 0; i < (int) q.size (); i++) {
				if (was.count (i)) {
					p1 *= p[q[i]];
				}
				else {
					p1 *= 1.0 - p[q[i]];
				}
			}
			tot += p1;
		} while (next_combination (pos, k));
		mx=  max (mx, tot);
	} while (next_combination (q, n));
	
	return mx;
}

void clear () {
}

int main () {
#ifdef LOCAL
	freopen ("file.in", "r", stdin);
	freopen ("file.out", "w", stdout);
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