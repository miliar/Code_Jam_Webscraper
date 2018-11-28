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

set <int> S;

inline void add(int x) {
	while (x) {
		S.insert(x % 10); x /= 10;
	}
}

int main() { // _
	#ifdef lcl
		freopen(fname".in", "r", stdin);
		freopen(fname".out", "w", stdout);
	#endif

	int t, Case = 0; scanf("%d", &t);

	while (t--) {
		int n; scanf("%d", &n);
		S.clear();
		if (!n) {
			printf("Case #%d: INSOMNIA\n", ++Case);
			continue;
		}
		bool ch = false;
		for (int i = 1; i <= 100; ++i) {
			add(n * i);
			if ((int)S.size() == 10) {
				ch = true;
				printf("Case #%d: %d\n", ++Case, n * i);
				break;
			}
		}
		if (!ch) {
			printf("Case #%d: INSOMNIA\n", ++Case);
			continue;
		}
	}

	return 0;
}
