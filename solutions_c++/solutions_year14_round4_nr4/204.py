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

const int N = 15;

int n, m;

string s[N];
int cur[N];

int t[N * N][30];
int sze = 0;

inline bool read() {
	n = nextInt();
	m = nextInt();

	forn(i, n) {
	 	char buf[15];

	 	assert(scanf("%s", buf));

	 	s[i] = string(buf);  

	}

 	return true;
}

int cnt[5];

int tans = -1;
int cntAns = 0;

void add_string(string tv) {
 	int curIt = 0;

 	forn(i, sz(tv)) {
 		int pv = tv[i] - 'A';

 		if (t[curIt][pv] == -1) {
 		 	t[curIt][pv] = sze;
 		 	curIt = sze;
 		 	sze++;	
 		} else {
 			curIt = t[curIt][pv]; 	
 		}
 	}	
}

int build(int value) {
 	memset(t, -1, sizeof t);
    sze = 1;

 	forn(i, n) {
 	 	if (cur[i] == value) {
 	 	 	add_string(s[i]);
 	 	}
 	}

 	return sze;
}

void go(int s) {
	if (s == n) {
		forn(i, m) 
			if (!cnt[i])
				return;
		int ans = 0;
		forn(i, m)
			ans += build(i + 1);

		if (ans > tans) {
		 	tans = ans;
		 	cntAns = 0;
		}

		if (tans == ans) {
		 	cntAns ++;
		}

		return;
	}

	forn(i, m) {
		cnt[i]++;
		cur[s] = i + 1;
		go(s + 1);
		cnt[i]--;
	}	

}	
            
inline void solve() {                    
	memset(cnt, 0, sizeof cnt);
	tans = -1;
	cntAns = 0;
	go(0);

	cout << tans << ' ' << cntAns << endl;	
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
		 	cerr << test  + 1 << endl;
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