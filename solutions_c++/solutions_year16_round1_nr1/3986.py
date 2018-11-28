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

int used[MaxN], timer;

int main() { _
	#ifdef lcl
		freopen(fname".in", "r", stdin);
		freopen(fname".out", "w", stdout);
	#endif

	int t; cin >> t;
	int Case = 0;

	while (t--) {
		string s; cin >> s;

		++timer;
		char lst = 'A';
		cout << "Case #" << ++Case << ": "; 
		for (int i = 0; i < (int)s.size(); ++i) {
			if (s[i] >= lst) {
				used[i] = timer;
				// cerr << "HERE " << s << " : " << s[i] << " " << lst << endl;
				lst = s[i];
			}
		}
		for (int i = (int)s.size() - 1; i >= 0; --i) {
			if (used[i] == timer) {
				cout << s[i];
			}
		}
		for (int i = 0; i < (int)s.size(); ++i) {
			if (used[i] != timer)
				cout << s[i];
		}
		cout << endl;
	}

	return 0;
}
