#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <vector>

#if LOCAL
	#define DO_NOT_SEND
#endif

typedef long long LL;

int IntMaxVal = (int) 1e20;
int IntMinVal = (int) -1e20;
LL LongMaxVal = (LL) 1e20;
LL LongMinVal = (LL) -1e20;

#define FOR(i, a, b) for(int i = a; i < b ; ++i)
#define FORD(i, a, b) for(int i = a; i >= b; --i)

template<typename T> inline void minimize(T &a, T b) { a = std::min(a, b); }
template<typename T> inline void maximize(T &a, T b) { a = std::max(a, b); }

#define all(v) v.begin(),v.end()

using namespace std;

#define endl '\n'
template<typename T> struct argument_type;
template<typename T, typename U> struct argument_type<T(U)> { typedef U type; };
#define next(t, i) argument_type<void(t)>::type i; cin >> i;
#define nextVector(t, v, size) vector< argument_type<void(t)>::type > v(size); { for (int i = 0 ; i < size ; i++) cin >> v[i]; }

#define range(name, start, count) vector<int> name(count); { for (int i = 0 ; i < count ; i++) name[i] = i + start; }

template <typename T1, typename T2> istream& operator >>(istream& is, pair<T1, T2>& s) { is >> s.first >> s.second; return is; }
template <typename T> ostream& operator << (ostream& os, const vector<T> &v) { for (int i = 0 ; i < v.size() ; i++) os << v[i] << ' '; os << endl; return os; }
template <typename T1, typename T2> ostream& operator <<(ostream& s, pair<T1, T2>& t) { s << t.first << ' ' << t.second; return s; }
template <typename T> vector<T> readVector(int n) { vector<T> res(n); for (int i = 0 ; i < n ; i++) cin >> res[i]; return res; }

int main() {
	srand (time(NULL));
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    // #ifdef ONLINE_JUDGE
    freopen("input.in", "rt", stdin);
    // #endif	
	
	next(int, t);
	int ttt = 1;
	while (t --> 0) {
		next(int, n);
		
		auto a = readVector<int>(n);
		vector<int> perm(n);
		FOR (i, 0, n) perm[i] = i;
		int mx = IntMinVal;
		int imx = 0;
		for (auto x : a) maximize(mx, x);
		while (a[imx] != mx) imx++;
		int ans = IntMaxVal;
		do {
			int mxPos = 0;
			while (perm[mxPos] != imx) mxPos++;
			bool isOk = true;
			FOR (i, 0, mxPos) {
				int i1 = perm[i];
				int i2 = perm[i + 1];
				if (a[i1] > a[i2]) isOk = false;
			}
			FOR (i, mxPos + 1, n) {
				int i1 = perm[i - 1];
				int i2 = perm[i];
				if (a[i1] < a[i2]) isOk = false;
			}
			if (!isOk) continue;
			
			int swaps = 0;
			vector<int> curPerm(n);
			FOR (i,0, n) curPerm[i] = i;
			FOR (i, 0, n) {
				
				int pos = i;
				while (curPerm[pos] != perm[i]) pos++;
				while (pos > i) {
					swap(curPerm[pos], curPerm[pos - 1]);
					pos--;
					swaps++;
				}
			}
			minimize(ans, swaps);
		} while (next_permutation(all(perm)));
		cout << "Case #" << ttt << ": " << ans << endl;
		ttt++;
	}
}