#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second

typedef unsigned long long ull;
typedef unsigned int ui;
typedef long long ll;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

const int N = 102;
ll k, c, s;
bool foi[N];
vector <ll> res;

void go (ll l, ll at, ll nv) {
	ll dest;
	ll newat;

	foi[at] = 1;

	if (nv == c) {
		res.pb(l);
		return;
	}

	if (at == k) {
		dest = l * k;
		newat = at;
	} else {
		newat = at + 1;
		dest = (l-1) * k + at + 1;
	}

	go (dest, newat, nv + 1);
}

int main (void) {
	ios_base::sync_with_stdio(false);

	int t;	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		cin >> k >> c >> s;
		memset(foi, 0, sizeof foi);
		for (int j = 1; j <= k; j++) {
			if (!foi[j]) go(j,j,1);
		}

		if ((int)res.size() > s) {
			cout << "IMPOSSIBLE";
		} else {
			for (int j = 0; j < (int)res.size(); j++)
				cout << res[j] << " ";
		}
		cout << endl;
		if (res.size()) res.clear();
	}

	return 0;
}
