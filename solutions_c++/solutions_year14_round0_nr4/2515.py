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

#define rep(i,to)       for(li i=0;i<((li)to);++i)
#define foreach(it,set) for(__typeof((set).begin()) it=(set).begin();it!=(set).end();it++)
#define all(v)          v.begin(), v.end()

template <class T> inline void minu(T& x, T y) { x = min(x, y); }
template <class T> inline void maxu(T& x, T y) { x = max(x, y); }

inline li bit(li n){ return 1LL<<n; }
template <class T> ostream& operator<<(ostream& os, vector<T> x){
    foreach(it, x) os << *it << ' ';
    return os;
}

li dx[8] = {1, -1, 0,  0, -1, 1,  1, -1};
li dy[8] = {0,  0, 1, -1, -1, 1, -1,  1};

int calc(const vector<double>& a, const vector<double>& b, int n) {
   int dw;
    for (dw = n; dw > 0; --dw) {
        bool ok = true;
        int dl = n - dw;
        rep(i, dw) {
            if (a[dl + i] < b[i]) ok = false;
        }
        if (ok) break;
    }
    return dw;
}
void solve(int caseNum) {
    int n;
    cin >> n;
    vector<double> a(n), b(n);
    rep(i, n) {
        cin >> a[i];
    }
    rep (i, n) {
        cin >> b[i];
    }

    sort(all(a));
    sort(all(b));


    cout << "Case #" << caseNum << ": " << calc(a, b, n) << " " << n - calc(b, a, n) << endl;
    return;
}

int main() {
    int n;
    cin >> n;
    rep(i, n) solve(i + 1);
    return 0;
}
