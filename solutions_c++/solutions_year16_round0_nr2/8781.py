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

string s;
            
inline bool read() {        
    cin >> s;
	return true;	
}               
                      
int ans[11][1 << 11];

int f(int x, int len) {
	int t = x ^ ((1 << len) - 1);
	int ans = 0;
	forn (i, len) {
		ans <<= 1;
		ans += t & 1;
		t >>= 1;		
	}	
	return ans;
}

void print(int x, int len) {
	for (int i = len - 1; i >= 0; --i)
		cerr << ((x >> i) & 1);
}

void calc(int len) {
	int mask = (1 << len) - 1;
	vector<bool> used(1 << len, false);
	used[mask] = true;
	ans[len][mask] = 0;
	queue<int> q;
	q.push(mask);
	while(!q.empty()) {
		int v = q.front();
		q.pop();
		forn (i, len) {
			int t = v >> i;
			int nv = v - (t << i) + (f(t, len - i) << i);
			if (!used[nv]) {
				used[nv] = true;
				ans[len][nv] = ans[len][v] + 1;
				q.push(nv);
			}
		}	
	}	
}

void solve() {
	int mask = 0;
	forn (i, sz(s)) {
		mask <<= 1;
		mask += (s[i] == '+');
	} 
	cout << ans[sz(s)][mask] << endl;
}         

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	for (int i = 1; i <= 10; ++i)
		calc(i);

	cerr << setprecision(10) << fixed;
	cout << setprecision(15) << fixed;

	srand(time(NULL));

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
	    cout << "Case #" << i + 1 << ": ";
		assert(read());
		solve();
	}

#ifdef _DEBUG
	cerr << "TIME: " << clock() << endl;
#endif

	return 0;
}