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

vector <string> v;

inline bool Less(double a, double b) {
	return a + eps < b;
}

bool f(vector <int> p) {
	int cnt = 0;
	for (auto it : p)
		cnt += it;
	if (!cnt) {
		for (auto it : v)
			printf("%s ", it.c_str());
		return true;
	}
	for (int i = 0; i < (int)p.size(); ++i) {
		if (p[i] > 0) {
			--p[i];
			v.push_back(string(1, (char)(i + 'A')));
			--cnt;

			double x = 100.0 / cnt;
			bool ok = true;
			for (int j = 0; ok && j < (int)p.size(); ++j)
				if (Less(50.0, x * p[j]))
					ok = false;
			if (ok && f(p))
				return true;
			++cnt;
			v.pop_back();
			++p[i];
		}
	}
	for (int i = 0; i < (int)p.size(); ++i) {
		if (p[i] > 1) {
			p[i] -= 2;
			v.push_back(string(2, (char)(i + 'A')));
			cnt -= 2;

			double x = 100.0 / cnt;
			bool ok = true;
			for (int j = 0; ok && j < (int)p.size(); ++j)
				if (Less(50.0, x * p[j]))
					ok = false;
			if (ok && f(p))
				return true;
			cnt += 2;
			v.pop_back();
			p[i] += 2;
		}
	}
	for (int i = 0; i < (int)p.size(); ++i) if (p[i] > 0) {
		for (int k = i + 1; k < (int)p.size(); ++k) if (p[k] > 0) {
			--p[i];
			--p[k];
			v.push_back(string(1, (char)(i + 'A')));
			v.back() += string(1, (char)(k + 'A'));
			cnt -= 2;

			double x = 100.0 / cnt;
			bool ok = true;
			for (int j = 0; ok && j < (int)p.size(); ++j)
				if (Less(50.0, x * p[j]))
					ok = false;
			if (ok && f(p))
				return true;
			cnt += 2;
			v.pop_back();
			++p[i];
			++p[k];
		}
	}
	return false;
}

int main() { // _
	#ifdef lcl
		freopen(fname".in", "r", stdin);
		freopen(fname".out", "w", stdout);
	#endif

	int t, Case = 1; scanf("%d", &t);

	while (t--) {
		int n; scanf("%d", &n);
		vector <int> p(n + 1);
		for (int i = 0; i < n; ++i)
			scanf("%d", &p[i]);
		v.clear();
		printf("Case #%d: ", Case++);
		f(p);
		puts("");
	}

	return 0;
}
