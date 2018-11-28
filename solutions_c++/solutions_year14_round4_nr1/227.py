#undef NDEBUG
#ifdef gridnevvvit
#define _GLIBCXX_DEBUG
#endif

#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>

#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <vector>
#include <string>
#include <deque>
#include <bitset>
#include <algorithm>
#include <utility>
                  
#include <functional>
#include <limits>
#include <numeric>
#include <complex>

#include <cassert>
#include <cmath>
#include <memory.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>   

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int,int> pt;
typedef pair<ld, ld> ptd;
typedef unsigned long long uli;

#define pb push_back
#define mp make_pair
#define mset(a, val) memset(a, val, sizeof (a))
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define ft first
#define sc second
#define sz(a) int((a).size())
#define x first
#define y second

template<typename X> inline X abs(const X& a) { return (a < 0 ? -a : a); }
template<typename X> inline X sqr(const X& a) { return (a * a); }
template<typename T> inline string toStr(T x) { stringstream st; st << x; string s; st >> s; return s; }
template<typename T> inline int hasBit(T mask, int b) { return (b >= 0 && (mask & (T(1) << b)) != 0) ? 1 : 0; }
template<typename X, typename T>inline ostream& operator<< (ostream& out, const pair<T, X>& p) { return out << '(' << p.ft << ", " << p.sc << ')'; }

inline int nextInt() { int x; if (scanf("%d", &x) != 1) throw; return x; }
inline li nextInt64() { li x; if (scanf("%I64d", &x) != 1) throw; return x; }
inline double nextDouble() { double x; if (scanf("%lf", &x) != 1) throw; return x; }

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define fore(i, a, b) for(int i = int(a); i <= int(b); i++)
#define ford(i, n) for(int i = int(n - 1); i >= 0; i--)
#define foreach(it, a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)

const int INF = int(1e9);
const li INF64 = li(INF) * li(INF);
const ld EPS = 1e-9;
const ld PI = ld(3.1415926535897932384626433832795);

const int N = 10000 + 100;

int n, x;
int s[N];


inline bool read() {
 	n = nextInt();
 	x = nextInt();

   	forn(i, n)
   		s[i] = nextInt();

 	return true;
}
               
inline void solve() {                    
	sort(s, s + n);

	int lf = 0;
	int rg = (n / 2) + 1;

	while (rg - lf > 1) {
	 	int mid = (lf + rg) / 2;

	 	bool ok = true;

	 	forn(i, mid) {
	 	 	if (s[i] + s[2 * mid - i - 1] > x) 
	 	 		ok = false;
	 	}



	 	if (ok) lf = mid;
	 	else rg = mid;
	}

	cout << n - lf << endl;
}

int main() 
{

#ifdef gridnevvvit
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
    
	srand(time(NULL));

	cout << setprecision(10) << fixed;
	cerr << setprecision(5) << fixed;
	
	bool multipleTestCases = true;

	if (multipleTestCases) {
		
		int testCnt;

		assert(scanf("%d", &testCnt) == 1);

		forn(test, testCnt) {
		 	printf("Case #%d: ", test + 1);
		 	assert(read());
         	solve();
		}
	 	
	}
	else {
	 	assert(read());
	 	solve();
	}

#ifdef gridnevvvit
	cerr << "===Time: " << clock()  << "===" << endl;
#endif

} 