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


int main (void) {
	ios_base::sync_with_stdio(false);

	int t;	cin >> t;
	for (int k = 1; k <= t; k++) {
		string s;
		cout << "Case #" << k << ": ";
		cin >> s;
		bool f = 0;
		ll res = 0;
		for (int i = s.size() - 1; i >= 0; i--) {
			if (!f and s[i] == '-') {
				f = 1;
				res++;
			} else if (f and s[i] == '+') {
				f = 0;
				res ++;
			}
		}
		cout << res << endl;
	}

	return 0;
}
