#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <utility>
#include <cstdlib>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <memory.h>
#include <ctime>
#include <cctype>

using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define mp make_pair
#define fs first
#define sc second
#define pb push_back
#define all(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))

typedef long double ld;
typedef long long ll;
typedef unsigned char uc;
typedef unsigned int ui;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;

const ld pi = 3.141592653589793238462643l;

ll calc (ll n, ll p) {
	if (p == 0) {
		return p;
	}
	if (p == (1ll << n)) {
		return p;
	}
	ll ans = 0;
	forn (i, n) {
		ans += (1ll << i);
		p -= (1ll << (n - 1 - i));
		if (p <= 0) {
			break;
		}
	}
	return ans;
}

void solve () {
	ll n, p;
	cin >> n >> p;
	cout << calc(n, p) - 1 << ' ' << (1ll << n) - calc(n, (1ll << n) - p) - 1 << endl;
}

int main () {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);	
	int t;
	cin >> t;
	forn (i, t) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}
