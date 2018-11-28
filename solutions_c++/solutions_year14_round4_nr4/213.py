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

int n, m, answ, ans;

string s[105];

void load() {
	scanf ("%d%d\n", &n, &m);
	for (int i = 0;i < n;i++) {
		cin >> s[i];
	}
}

vector <int> a[105];

int calc (int id) {
	set <string> all;
	for (int i = 0;i < (int)a[id].size();i++) {
		int t = a[id][i];
		for (int l = 0;l <= (int)s[t].size();l++) {
			all.insert (s[t].substr (0, l));
		}
	}
	return all.size();
}

void go (int pos) {
	if (pos == n) {
		int cur = 0;
		for (int i = 0;i < m;i++) {
			cur += calc (i);
		}
		if (cur > answ) {
			answ = cur;
			ans = 0;
		}
		if (answ == cur) ans++;
		return;
	}

	for (int i = 0;i < m;i++) {
		a[i].push_back (pos);
		go (pos + 1);
		a[i].pop_back ();
	}
}

void solve(int test) {
	answ = 0, ans = 0;
	go (0);
	printf ("Case #%d: %d %d\n", test, answ, ans);
}

int main() {
 	freopen ("a.in", "r", stdin);

 	int t;
 	scanf ("%d\n", &t);

 	for (int i = 1;i <= t;i++) {
 		cerr << i << endl;
 		load();
 		solve(i);
 	}

 	return 0;
}