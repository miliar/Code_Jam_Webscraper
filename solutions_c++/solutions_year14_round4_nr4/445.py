#pragma comment(linker, "/STACK:65000000")
#include <algorithm>
#include <cmath>
#include <cstdio> 
#include <cstring> 
#include <iostream> 
#include <map> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <string> 
#include <vector> 

using namespace std; 

template<class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }

typedef long long lng;
typedef long double ld;
typedef stringstream istr;

#define TynKogep TOPCODER
#define bublic public:
#define pb push_back
#define sz(x) ((int)(x).size())
#define mp make_pair
#define first fi
#define second se
#define clr(a) memset((a),0,sizeof(a))

vector<string> v;
int n, m;
int c[123];
long long ans1, ans2;
set<string> S;

void add(string s) {
    string now = "";
    for(int i = 0; i < s.size(); ++i) {
        S.insert(now);
        now += s[i];
    }
    S.insert(now);
}

void test() {
    int here = 0;
    for(int i = 1; i <= n; ++i) {
        S.clear();
        for(int j = 0; j < m; ++j) {
            if (c[j] == i)
                add(v[j]);
        }
        here += S.size();
    }
    /*for(int i = 0; i < m; ++i) {
        cout << c[i] << " ";
    }
    cout << here << endl;
    */
    if (here > ans1) {
        ans1 = here;
        ans2 = 0;
    }
    if (here == ans1) ++ans2;
}

void rec(int cur, int mx) {
    if (cur == m) {
        if (mx == n)
            test();
        return;
    }
    for(int i = 1; i <= mx; ++i) {
        c[cur] = i;
        rec(cur + 1, mx);
    }
    if (mx < n) {
        c[cur] = mx + 1;
        rec(cur + 1, mx + 1);
    }
}

int main() {
    int T;
    cin >> T;
    for(int TT = 0; TT < T; ++TT) {
        cout << "Case #" << TT + 1 << ": ";
        cin >> m >> n;
        v.clear();
        ans1 = 0;
        for(int i = 0; i < m; ++i) {
            string s;
            cin >> s;
            v.pb(s);
        }
        rec(0, 0);
        for(int i = 2; i <= n; ++i) ans2 *= i;
        cout << ans1 << " " << ans2 << endl;
    }
    return 0;
};
