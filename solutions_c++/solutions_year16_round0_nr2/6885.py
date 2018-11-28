#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
#include <bitset>
#include <unordered_set>
#include <unordered_map>

#define forn(i, n) for (int i = 0; i < (n); i++)
#define fore(i, l, r) for (int i = l; ((l) < (r) ? i <= (r) : i >= (r)); ((l) < (r) ? i++ : i--))
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)((a).size())
#define mp make_pair

using namespace std;

typedef long long li;
typedef long double ld;

template<typename X> inline X abs(const X& a) { return a < 0 ? -a : a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

template<typename A, typename B> inline ostream& operator<< (ostream& out, const pair<A, B>& p) { return out << "(" << p.x << ", " << p.y << ")"; }
template<typename T> inline ostream& operator<< (ostream& out, const vector<T>& a) { out << "["; forn(i, sz(a)) { if (i) out << ','; out << ' ' << a[i]; } return out << " ]"; }
template<typename T> inline ostream& operator<< (ostream& out, const set<T>& a) { return out << vector<T>(all(a)); }
template<typename T> inline ostream& operator<< (ostream& out, pair<T*, int> a) { return out << vector<T>(a.x, a.x + a.y); }

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int MAXN = 200001;

unordered_set <int> used;

inline void check(li x) {
	while (x > 0) {
		used.insert(x % 10);
		x /= 10;
	}
}

int main() {
#ifdef _DEBUG
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	srand(time(NULL));
	ld startTime = gett();
	int T;
	cin >> T;
	fore(test, 1, T) {
		cout << "Case #" << test << ": ";
		string s;
		cin >> s;
		int ans = 0;

		fore(i, s.size() - 1, 0) {
			if (s[i] == '-') {
				ans++;
				fore(j, 0, i) {
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		}
		cout << ans << endl;
	}
	cerr << "Time: " << gett() - startTime << " ms" << endl;
}