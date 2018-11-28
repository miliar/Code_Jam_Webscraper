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

int len, c, ss;

void solve(int test) {
	cin >> len >> c >> ss;
	cout << "Case #" << test << ": ";
	for (int i = 1; i <= len; i++) {
		ll id = i;
		for (int j = 2; j <= c; j++) {
			id = (id - 1) * 1ll * len + i;
		}
		cout << id << ' ';
	}
	cout << endl;
}

int main() {
	#ifdef Nick
	freopen(fname"in","r",stdin);
	freopen(fname"out","w",stdout);
	#endif
	int t;
	scanf("%d", &t);
	for (int it = 1; it <= t; it++)
		solve(it);
	return 0;
}
