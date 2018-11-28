#include <bits/stdc++.h>
#include <utility>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

const ll BASE = 10007;
const int MAXN = 100005;

#define filla(a, x) memset(a, x, sizeof(a))
#define rep(i, n) for (int i = 0, sz = (n); i < sz; ++i)
#define foru(i, l, r) for (int i = (l); i <= (r); ++i)
#define ford(i, r, l) for (int i = (r); i >= (l); --i)
#define pb push_back
#define fs first
#define sc second

int n, sl;
int dis[11];
int a[33];

int read()
{
	int x;
	scanf("%d", &x);
	return x;
}

int 	check() {
	for (int base = 2; base <= 10; ++base) {
		ll res = 0;
		for (int i = 0; i < n; ++i) {
			res = res * ll(base) + ll(a[i]);
			// cout << a[i];
		}
		// cout << " " << res << " ";
		int flat = 0;
		ll i = 2; 
		while (i * i <= res) {
			ll t = res / i;
			if (res - t * i == 0) {
				dis[base] = i;
				flat = 1;
				break;
			}
			++i;
		}
		if (!flat) {
			return 0;
		}
	}
	return 1;
}

void 	solve(int i) {
	if (sl == 0)
		return;
	if (i == n-1) {
		if (check()) {
			for (int j = 0; j < n; ++j)
				cout << a[j];
			for (int base = 2; base <= 10; ++base)
				cout << " " << dis[base];
			if (sl > 1)
				cout << "\n";
			--sl;
			if (sl == 0)
				return;
		}
	}
	else {
		a[i] = 0;
		solve(i + 1);
		if (sl == 0)
			return;
		a[i] = 1;
		solve(i + 1);
	}
}


int main()
{
	#ifdef DEBUG
		freopen("C-small-attempt1.in", "r", stdin);
		freopen("C-small-attempt1.out", "w", stdout);
	#endif
	int ntest = read();
	for (int i = 1; i <= ntest; ++i) {
		cin >> n >> sl;
		cout << "Case #" << i << ":\n";
		a[0] = a[n-1] = 1;
		solve(1);
	}
	return 0;
}