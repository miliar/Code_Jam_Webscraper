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

string s;

void rev(int l, int r) {
	for (int i = l, j = r; i < j; i++, j--)
		swap(s[i], s[j]);
}

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> s;
	int ans = 0;
	for (int i = 1; i < sz(s); i++)
		if (s[i] != s[i - 1]) {
			for (int j = 0; j < i; j++)
				s[j] = (s[j] == '+' ? '-' : '+');
			ans++;
		}
	if (s[sz(s) - 1] == '-')
		ans++;
	cout << ans << endl;
	return;
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
