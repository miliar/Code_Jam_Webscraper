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


int read()
{
	int x;
	scanf("%d", &x);
	return x;
}

void	update(ll x, int a[10], int &cnt) {
	while (x) {
		if (a[x % 10] == 0)
			++cnt;
		a[x % 10] = 1;
		x /= 10;
	}
}

void 	find(int x) {
	if (x == 0) {
		cout << "INSOMNIA";
		return;
	}
	int a[10];
	for (int i = 0; i < 10; ++i)
		a[i] = 0;	
	int cnt = 0;
	ll y;
	for (int i = 1; ; ++i){
		y = ll(x) * i;
		// cout << " - " << y;
		update(y, a, cnt);
		// cout << " " << cnt << " - ";
		if (cnt == 10) {
			// cout << " " << i << " ";
			break;
		}
	}
	cout << y;
}

int main()
{
	#ifdef DEBUG
		freopen("A-large.in", "r", stdin);
		freopen("A-large.out", "w", stdout);
	#endif

	int n = read();
	for (int i = 1; i <= n; ++i) {
		int x = read();
		cout << "Case #" << i << ": ";
		find(x);
		if (i < n)
			cout << "\n";
	}

	return 0;
}