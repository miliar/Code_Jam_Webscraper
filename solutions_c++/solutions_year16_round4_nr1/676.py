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

struct trip {
	int r, p, s;
	trip () : r (1), p (1), s (1) {}
	trip (int r, int p, int s) : r (r), p (p), s (s) {}

	trip operator + (trip x) {
		return trip (r + x.r, p + x.p, s + x.s);
	}
};

vector<trip> operator + (vector<trip> &a, vector<trip> b) {
	int A = (int) a.size ();
	int B = (int) b.size ();
	a.resize (A + B);
	for (int i = 0; i < B; i++) a[i + A] = b[i];
}

int T;
int R, P, S;
int n;

void load () {
	cin >> n >> R >> P >> S;
}

char get (char c) {
	if (c == 'R') return 'S';
	if (c == 'S') return 'P';
	if (c == 'P') return 'R';
}

vector<string> dp[100][333];
char was[100][333];

bool check (string &s) {
	int r = 0, p = 0, sc = 0;
	for (int i = 0; i < (int) s.size (); i++) {
		r += s[i] == 'R';
		p += s[i] == 'P';
		sc += s[i] == 'S';
	}
	return R >= r && p <= P && S >= sc;
}

vector<string> get (char c, int dpt) {
	if (dpt == n) return vector<string> (1, string (1, c));
	if (was[dpt][(int) c]) return dp[dpt][(int) c];
	was[dpt][(int) c] = 1;
	auto & res = dp[dpt][(int) c];
	res.clear ();

	char t = get (c);

	auto r1 = get (c, dpt + 1);
	auto r2 = get (t, dpt + 1);
	
	for (int i = 0; i < (int) r1.size (); i++) {
		for (int j = 0; j < (int) r2.size (); j++) {
			res.push_back (min (r1[i] + r2[j], r2[j] + r1[i]));
			if (!check (res.back ())) res.pop_back ();
		}
	}	
	return res;
}

void opt (string &ans, string t) {
	if (ans.empty ()) ans = t;
	else ans = min (ans, t);
}

string solve () {
	string res;
	vector<string> r = get ('R', 0);
	for (int i = 0; i < (int) r.size (); i++) {
		if (check (r[i]))
			opt (res, r[i]);
	}
	r = get ('P', 0);
	for (int i = 0; i < (int) r.size (); i++) {
		if (check (r[i]))
			opt (res, r[i]);
	}
	r = get ('S', 0);
	for (int i = 0; i < (int) r.size (); i++) {
		if (check (r[i]))
			opt (res, r[i]);
	}
	if (res.empty ())
		res = "IMPOSSIBLE";
	return res;
}

void clear () {
	memset (was, 0, sizeof (was));
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