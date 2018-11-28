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

ll n;
set <int> s;

void go (ll x) {

	while (x) {
		s.insert(x%10);
		x /= 10;
	}

}

int main (void) {
	ios_base::sync_with_stdio(false);

	ll t;	cin >> t;
	for (int j = 1; j <= t; j++) {
		cin >> n;
		cout << "Case #" << j << ": ";
		if (!n) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		for (ll i = n; ; i += n) {
			go(i);
			if (s.size() == 10) {
				cout << i << endl;
				break;
			}
		}
		s.clear();
	}

	return 0;
}
