#define _CRT_SECURE_NO_WARNINGS
#include <functional>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <sstream>
#include <complex>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <ctime>
#include <set>
#include <map>

#define ll long long
#define ld long double
#define mp make_pair
#define TASKNAME "monument"


const int inf = 2 * 1e9;
const int mod = 1e9 + 7;
const ll infll = (ll)1e18;
const ld eps = 1e-9;

const int dx[] = { 1, 0, -1, 0 };
const int dy[] = { 0, -1, 0, 1 };

using namespace std;

ll trans(string s, ll k) {
	ll res = 0;
	for (ll i = 0; i < s.size(); i++) {
		if (s[i] == '1')
			res += ceil(pow((ld)k, (ld)i));
	}
	return res;
}

string tostr(ll n) {
	string res(16, '0');
	for (ll i = 0; i < 16; i++) {
		if (n & (1LL << i))
			res[i] = '1';
	}
	return res;
}

ll getd(ll n) {
	ll res = 1;
	for (ll i = 2; i * i <= n; i++) {
		if (n % i == 0) {
			res = i;
			break;
		}
	}
	return res;
}

void solve() {
	ll n;
	cin >> n;
	ll cnt;
	cin >> cnt;
	ll t = 0;
	for (ll i = (1 << 15) + 1; i < (1 << 16); i++) {
		if (t == cnt)
			break;
		if (i % 2 == 0)
			continue;
		bool ok = true;
		vector<ll> ans(11);
		for (ll k = 2; k <= 10 && ok; k++) {
			ll t = getd(trans(tostr(i), k));
			if (t > 1)
				ans[k] = t;
			else ok = false;
		}
		if (ok) {
			t++;
			string ss = tostr(i);
			cout << string(ss.rbegin(), ss.rend()) << " ";
			for (ll k = 2; k <= 10; k++)
				cout << ans[k] << " ";
			cout << endl;
		}
	}
}

int main() {
#ifdef __DEBUG__
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	clock_t start = clock();
#else
	//assert(freopen(TASKNAME".in", "r", stdin));
	//assert(freopen(TASKNAME".out", "w", stdout));
#endif
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cerr << "Test #" << t + 1 << " in progress\n";
		cout << "Case #" << t + 1 << ":\n";
		solve();
		cout << endl;
		cerr << "Test #" << t + 1 << " done\n";
}

#ifdef __DEBUG__
	fprintf(stderr, "\nTime: %Lf\n", ((clock() - start) / (ld)CLOCKS_PER_SEC));
#endif
	return 0;
}