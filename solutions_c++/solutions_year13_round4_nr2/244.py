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

li dx[8] = {1, -1, 0,  0, -1, 1,  1, -1};
li dy[8] = {0,  0, 1, -1, -1, 1, -1,  1};

li n, p;
bool guaranteed (li t) {
    li stronger = t;
    li acc = 0;
    li worstr = 0;
    rep(i, n) {
        acc += bit(i);
        if (acc <= stronger) {
            worstr += bit(n-1-i);
        }
    }
    return worstr < p;
}

bool possible (li t) {
    li weaker = bit(n) - t - 1;
    li acc = 0;
    li bestr = 0;
    rep(i, n) {
        acc += bit(i);
        if (acc > weaker) {
            bestr += bit(n-1-i);
        }
    }
    return bestr < p;
}

void solve() {
    cin >> n >> p;

    li l = 0, r = bit(n);
    while (r - l > 1) {
        li m = (l + r) / 2;
        if (guaranteed(m)) {
            l = m;
        } else {
            r = m;
        }
    }
    li gur = l;

    l = 0, r = bit(n);
    while (r - l > 1) {
        li m = (l + r) / 2;
        if (possible(m)) {
            l = m;
        } else {
            r = m;
        }
    }
    li pos = l;
    
    static int casenum = 1;
    cout << "Case #" << casenum++ << ": " << gur << " " << pos << endl;
    return;
}

int main() {
    int t;
    cin >> t;
    while (t--) solve();
    return 0;
}
