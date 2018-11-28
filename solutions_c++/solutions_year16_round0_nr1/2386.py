#include <bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef pair<int, int> pii;

const int MAXN = 1000100;

ll ans[MAXN];

int f(ll val) {
	int res = 0;
	do {
		res |= 1 << (val % 10);
	} while (val /= 10);
	return res;
}

int n, T;

void load() {
	cin >> n;
}

void solve(int tc) {
	cout << "Case #" << tc << ": ";
	if (!n) {
		cout << "INSOMNIA" << endl;
	} else {
		cout << ans[n] << endl;
	}
}

int main() {
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(false);
	for (int i = 1; i <= 1000000; ++i) {
		n = i;//cin >> n;
		int mask = 0;
		for (int j = 1; ; ++j) {
			mask |= f(j * 1ll * n);
			if (mask == (1 << 10) - 1) {
				ans[i] = j * 1ll * n;
				break;
			}
		}
	}
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		load();
		solve(tc);
    }                            
	return 0;
}