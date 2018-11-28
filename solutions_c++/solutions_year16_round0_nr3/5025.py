#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <bitset>
#include <stack>
#include <algorithm>
#include <iomanip>

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0 ? -a : a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

#define forn(i,n) for (int i = 0; i < int(n); i++)
#define ford(i,n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i,l,r) for (int i = int(l); i <= int(r); i++)
#define all(a) a.begin(), a.end()
#define sz(a) int(a.size())
#define mp make_pair
#define pb push_back
#define ft first
#define sc second
#define x first
#define y second

const ld EPS = 1e-9;
const int INF = int(1e9);
const li INF64 = li(1e18);

int n, m;
            
inline bool read() {        
    cin >> n >> m;
	return true;	
}

int d[11];

li f(string s, int b) {
	li res = 0;
	forn (i, sz(s)) {
		res *= b;
		res += s[i] - '0';
	}
	return res;
}

int get(li x) {
	for (li i = 2; i * i <= x; ++i) {
		if (x % i == 0)
			return i;
	}
	return -1;
}

bool ok (string s) {
	for (int b = 2; b <= 10; ++b) {
		li val = f(s, b);
		d[b] = get(val);
		if (d[b] == -1)
			return false;
	}	
	return true;
}    
                              
void solve() {
	string x;
	x += '1';
	for (int i = 0; i < n - 2; ++i)
		x += '0';
	x += '1';

	while(m) {
		if (ok(x)) {
			m--;
			cout << x;
			for (int i = 2; i <= 10; ++i)
				cout << " " << d[i];
			cout << endl;
		}
		int r = n - 2;
		while(++x[r] == '2')
			x[r--] = '0';
	}
}         

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
   	cerr << setprecision(10) << fixed;
	cout << setprecision(15) << fixed;

	srand(time(NULL));

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
	    cout << "Case #" << i + 1 << ":\n";
		assert(read());
		solve();
	}

#ifdef _DEBUG
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}