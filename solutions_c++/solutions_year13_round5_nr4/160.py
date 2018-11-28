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

int n, was[1 << 20];

double dp[1 << 20];

string s;

void load() {
	cin >> s;
	n = s.size();
}

int get (int mask, int pos) {
 	for (int a = pos;;a++) {
 	 	a %= n;
 	 	if (!has (mask, a)) return a;
 	}
}

double go (int mask) {
 	if (mask == two (n) - 1) return 0;

 	double &res = dp[mask];
 	if (was[mask]) return res;
 	res = 0;
 	was[mask] = 1;

 	for (int i = 0;i < n;i++) { 	
 	 	int t = get (mask, i);
 	 	//cerr << i << " " << t << " " << n - (t - i + n) % n << endl;
 	 	res += go (mask | two (t)) + n - (t - i + n) % n;
 	}
 	res /= 1.0 * n;

 	return res;
}

void solve(int test) {
	memset (was, 0, sizeof (was));

	int start = 0;
	for (int i = 0;i < (int)s.size();i++) {
	 	if (s[i] == 'X') {
	 	 	start |= two (i);
	 	 }
	}

	printf ("Case #%d: %.10lf\n", test, go (start));
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