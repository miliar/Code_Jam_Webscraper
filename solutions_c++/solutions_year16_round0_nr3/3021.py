#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>

using namespace std;

const int MAX = 10000000;

typedef long long ll;

ll er[MAX];
map<ll, ll> er2;
set<ll> p;

ll div(ll a) {
	if (a < MAX) {
		return er[a];
	}
	else {
		if (er2.count(a) > 0) {
			return er2[a];
		}
		for (set<ll>::iterator it = p.begin(); it != p.end() && (*it)*(*it) <= a; it++) {
			if (a % *it == 0) {
				er2[a] = *it;
				return *it;
			}
		}
		er2[a] = 0;
		return 0;
	}
}

ll toBase(ll a, int b) {
	if (b == 2) {
		return a;
	}
	ll r = 0;
	ll bb = 1;
	while (a > 0) {
		if (a & 1 == 1) {
			r += bb;
		}
		bb *= b;
		a = (a >> 1);
	}
	return r;
}

int main() {
#ifdef _DEBUG
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	memset(er, 0, MAX * sizeof(int));
	for (int i = 2; i < MAX; i++) {
		if (er[i] == 0) {
			p.insert(i);
			for (int j = 2 * i; j < MAX; j += i) {
				er[j] = i;
			}
		}
	}

	int skip, n, j;
	cin >> skip >> n >> j;
	vector<ll> r;
	vector<vector<ll> > rr;
	ll a = (1 << (n - 1)) | 1;
	while (r.size() < j) {
		bool bad = false;
		vector<ll> rri;
		for (int i = 2; i <= 10 && !bad; i++) {
			//cout << a << ' ' << i << endl;
			ll d = div(toBase(a, i));
			bad = (d == 0);
			rri.push_back(d);
		}
		if (!bad) {
			r.push_back(a);
			rr.push_back(rri);
		}
		a += 2;
	}
	cout << "Case #1: " << endl;
	for (int i = 0; i < j; i++) {
		for (int j = 1 << (n - 1); j > 0; j = j >> 1) {
			cout << ((r[i] & j) > 0);
		}
		for (int j = 0; j < 9; j++) {
			cout << " " << rr[i][j];
		}
		cout << endl;
	}
	return 0;
}