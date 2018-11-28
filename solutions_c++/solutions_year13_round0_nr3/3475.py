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

bool isPalindrome(li n) {
    ostringstream oss;
    oss << n;
    string digit = oss.str(), rev = digit;
    reverse(all(rev));
    return digit == rev;
}

vector<int> palins;

void solve(int caseNum) {
    li ans = 0, a, b;
    cin >> a >> b;

    rep(i, palins.size()) {
	li x = palins[i] * palins[i];
	if (a <= x && x <= b && isPalindrome(x)) ++ans;
    }
    cout << "Case #" << caseNum << ": " << ans << endl;
    return;
}

int main() {
    for (li i = 1; i <= 1e7; ++i) if (isPalindrome(i)) palins.push_back(i);
    cerr << "# palins: " << palins.size() << endl;

    int n;
    cin >> n;
    rep(i, n) solve(i + 1);
    return 0;
}
