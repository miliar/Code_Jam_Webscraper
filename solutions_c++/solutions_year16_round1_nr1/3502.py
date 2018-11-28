#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
const ld EPS = (ld) 1e-10;
const ll MOD = (ll) 1e9 + 7;
const int INF = (int) 2e9;
const int N = 2050;

int n, m;
int en[N];
string s;

void solve(int num) {
	cin >> s;
	char first = s[0];
	for (int i = 1; i < s.size(); ++i) {
		if (s[i] >= first) {
			en[i] = false;
			first = s[i];
		} else en[i] = true;
	}
	string g("");
	for (int i = s.size() - 1; i >= 0; --i) {
		if (!en[i]) g += s[i];
	}
	for (int i = 0; i < s.size(); ++i) {
		if (en[i]) g += s[i];
	}
	cout << "Case #" << num << ": " << g << '\n';
}

int main() {
	ios_base::sync_with_stdio(0);
#ifdef KOBRA
	freopen("toster", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
#else
#endif
	int cases;
	cin >> cases;
	for (int i = 0; i < cases; ++i) {
		solve(i + 1);
	}
	return 0;
}
