#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <sstream>
#include <complex>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long       li;
typedef vector<li>      vi;
typedef complex<double> pt;
typedef pair<pt, pt>    line;
typedef pair<li, li>    pi;
typedef vector<string>  vs;

#define rep(i,to)       for(li i=0;i<((li)to);i++)
#define foreach(it,set) for(__typeof((set).begin()) it=(set).begin();it!=(set).end();it++)
#define all(v)          v.begin(), v.end()

inline li bit(li n){ return 1LL<<n; }
template <class T> ostream& operator<<(ostream& os, vector<T> x){
  foreach(it, x) os << *it << ' ';
  return os;
}
template <class T> inline void dbg(T x){
  // return;
  cerr << x << endl; 
}

li vx[8] = {1, -1, 0,  0, -1, 1,  1, -1};
li vy[8] = {0,  0, 1, -1, -1, 1, -1,  1};

void solve(int caseNum) {
    int n, m;
    cin >> n >> m;

    vector<vector<int> > b(n, vector<int>(m, 0)), cut(n, vector<int>(m, 0));
    vector<pair<int, pair<int, int> > > q;
    rep(i, n) rep(j, m) {
	cin >> b[i][j];
	q.push_back(make_pair(b[i][j], make_pair(i, j)));
    }
    
    sort(all(q));

    foreach(it, q) {
	int h = it->first;
	int x = it->second.first;
	int y = it->second.second;

	bool ok = true;
	rep(j, m) {
	    if (b[x][j] != h && cut[x][j] == 0) ok = false;
	}
	if (ok) { 
	    rep (j, m) cut[x][j] = 1;
	}

	ok = true;
	rep(i, n) {
	    if (b[i][y] != h && cut[i][y] == 0) ok = false;
	}
	if (ok) { 
	    rep (i, n) cut[i][y] = 1;
	}
    }

    bool ok = true;
    rep(i, n) rep(j, m) ok &= cut[i][j];

    string ans = ok ? "YES" : "NO";
    cout << "Case #" << caseNum << ": " << ans << endl;
    return;
}

int main() {
    int n;
    cin >> n;
    rep(i, n) solve(i + 1);
    return 0;
}
