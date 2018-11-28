#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define foreach(it, S) for (__typeof (S.begin()) it = S.begin(); it != S.end(); it++)
#define all(x) x.begin(), x.end()
#define endl '\n'
#define _ ios_base :: sync_with_stdio(false); cin.tie(NULL);

#ifdef inputf
	#define fname ""
#else
	#define fname "" // <- Here
#endif

#ifndef lcl
#	define cerr if (0) cout
#endif

const double eps = 1e-9;
const int MaxN = int(2e5) + 256;
const int MOD = int(1e9) + 7;

template <typename T> inline T gcd(T a, T b) {
	return b ? gcd (b, a % b) : a;
}

inline bool Palindrome(const string& s) {
	return equal(s.begin(), s.end(), s.rbegin());
}

int d[MaxN][3];
int n;

int main() { // _
	#ifdef lcl
		freopen(fname".in", "r", stdin);
		freopen(fname".out", "w", stdout);
	#endif

	int t, Case = 0; scanf("%d", &t);

	while (t--) {
		char s[150]; scanf("\n%s", s + 1); n = strlen(s + 1);
		int cur = 0;
		memset(d, 0, sizeof d);
		for (int i = 1; i <= n; ++i) {
			if (s[i] == '+') {
				d[i][1] = d[i - 1][1];
				d[i][0] = d[i - 1][1] + 1;
			} else {
				d[i][0] = d[i - 1][0];
				d[i][1] = d[i - 1][0] + 1;
			}
		}
		printf("Case #%d: %d\n", ++Case, d[n][1]);
	}

	return 0;
}
