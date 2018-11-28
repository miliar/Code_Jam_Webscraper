#include <bits/stdc++.h>

#define pb push_back
#define f first
#define s second
#define mp make_pair
#define sz(a) int((a).size())
#ifdef _WIN32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fname "."
#define pi pair < int, int >

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

const int MAX_N = (int)1e5 + 123;
const double eps = 1e-6;
const int inf = (int)1e9 + 123;

using namespace std;

int n, cnt;

bool bit(int num, int x) {
	return (num & (1 << x)) > 0;
}

vector < int > st;

int do_it(ll x) {
	for (int i = 2; 1ll * i * i <= x; i++)
		if (x % i == 0)
			return i;
	return -1;
}

bool check(int x, vector < int > &q) {
  st.clear();
	for (int i = 0; i < n; i++)
		st.pb(bit(x, i));
	for (int i = 2; i <= 10; i++) {
		ll nw = 0, pw = 1;
		for (int j = 0; j < n; j++) {
			nw += 1ll * pw * st[j];
			pw = 1ll * pw * i;
		}
		ll x = do_it(nw);
		if (x == -1)
			return 0;
		q.pb(x);
	}		
	return 1;
}

void out(int mask) {
	for (int i = n - 1; i >= 0; i--)
		cout << bit(mask, i);
}

void solve(int test) {
	scanf("%d%d", &n, &cnt);
	vector < int > q;
	printf("Case #%d:\n", test);
	for (int mask = 0; mask < (1 << n); mask++) {
		if (!cnt)
			return;
		q.clear();
		if (bit(mask, 0) && bit(mask, n - 1)) {
			if (check(mask, q)) {
			  cnt--;
				out(mask);
				cout << ' ';
				for (auto i : q)
					cout << i << ' ';
				cout << endl;
			}
		}	
	}
}

int main() {
	#ifdef Nick
	freopen(fname"in","r",stdin);
	freopen(fname"out","w",stdout);
	#endif
	int t;
	scanf("%d", &t);
	for (int test = 1; test <= t; test++)
		solve(test);
	return 0;
}
