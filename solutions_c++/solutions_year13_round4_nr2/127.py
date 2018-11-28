#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <cmath>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

#define X first
#define Y second

typedef long long ll;
typedef vector <int> vi;

ll worst_score(ll x, ll n) {
	ll lesser_cnt = x;
	ll pos = 0;
	while (lesser_cnt > 0) {
		lesser_cnt = (lesser_cnt - 1) / 2;
		pos += n / 2;
		n /= 2;
	}
	return pos;
}

ll best_score(ll x, ll n) {
	ll greater_cnt = n - x - 1;
	while (greater_cnt > 0) {
		greater_cnt = (greater_cnt - 1) / 2;
		n /= 2;
	}
	return n - 1;
}

ll find1(ll n, ll p) {
	ll win = 0, lose = n;
	while (lose - win > 1) {
		ll x = (lose + win) / 2;
		if (worst_score(x, n) < p)
			win = x;
		else
			lose = x;
	}
	return win;
}

ll find2(ll n, ll p) {
	ll win = 0, lose = n;
	while (lose - win > 1) {
		ll x = (lose + win) / 2;
		if (best_score(x, n) < p)
			win = x;
		else
			lose = x;
	}
	return win;
}

int main() {
	int TT;
	cin >> TT;
	for (int T = 1; T <= TT; ++T) {
		ll N, p;
		cin >> N >> p;
		ll n = (1ll << N);

		cout << "Case #" << T << ": " << find1(n, p) << " " << find2(n, p) << endl;
	}
	return 0;
}