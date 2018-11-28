#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <list>
#include <iomanip>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <ctime>

#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)
#define sz(a) int(a.size())

using namespace std;

const int INF = 1e9;

typedef long long li;
typedef long double ld;

typedef pair<li, li> pt;
#define ft first
#define sc second
#define x first
#define y second

int n;
string s;

bool read() {
	if (!(cin >> n >> s))
		return false;
	return true;
}

void solve() {
	
	int cur = 0, ans = 0;
	forn (i, n + 1) {
		while(cur < i)
			cur++, ans++;
		cur += s[i] - '0';
	}
	cout << ans << endl;
}

int main() {
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	
	int t;
	cin >> t;
	forn (i, t) {
		read();
		cout << "Case #" << i + 1 << ": "; 
		solve();
	}
    
    return 0;
}