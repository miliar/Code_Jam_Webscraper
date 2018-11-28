#include <iostream>
#include <cstdio>
#include <cassert>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <climits>

using namespace std;

#ifdef LOCAL
#define dbg(x) cerr << #x " = " << x << endl;
#include "pretty_print.h"
#else
#define dbg(x)
#endif

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;

#define snd second
#define fst first

template <typename T> T sqr(T x) { return x * x; }
template <typename T> T abs(T x) { return x < 0? -x : x; }
template <typename T> T gcd(T a, T b) { return b? gcd(b, a % b) : a; }
template <typename T> bool chmin(T &x, const T& y) { if (x > y) { x = y; return true; } return false; }
template <typename T> bool chmax(T &x, const T& y) { if (x < y) { x = y; return true; } return false; }

map <string, int> m;
map <string, int> _m;

void inv(string& s, const int x) {
    reverse(s.begin(), s.begin() + x);
    for (int i = 0; i < x; ++i) {
        s[i] = s[i] == '-'? '+' : '-';
    }
}

int rec(string s) {
    if (m.count(s)) {
        return m[s];
    }
    if (s.find('-') == string::npos) {
        return 0;
    }
    int& res = m[s];
    int i = s.size();
    res = 2 * i;
    while (s[i - 1] == '+') {
        --i;
    }
    while (i > 0) {
        inv(s, i);
        res = min(res, rec(s) + 1);
        inv(s, i);
        --i;
    }
    return res;
}

int rec2(string s) {
    if (_m.count(s)) {
        return _m[s];
    }
    if (s.find('-') == string::npos) {
        return 0;
    }
    int& res = _m[s];
    int i = s.size();
    res = 2 * i;
    while (s[i - 1] == '+') {
        --i;
    }
    if (s[0] == '+') {
        for (int j = 1; j <= i; ++j) {
            if (s[j] == '-') {
                inv(s, j);
                inv(s, i);
                res = min(res, rec2(s) + 2);
                inv(s, i);
                inv(s, j);
                break;
            }
        }
    } else {
        inv(s, i);
        res = min(res, rec2(s) + 1);
        inv(s, i);
    }
    return res;
}

int main(int /* argc */, char** /* argv */)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifdef LOCAL
    assert(freopen("inp", "r", stdin));
    assert(freopen("out", "w", stdout));
    #endif
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        string s;
        cin >> s;
        int ans = rec2(s);
        if (s.size() < 20) {
            int result = rec(s);
            cerr << s << endl;
            if (ans != result) {
                cerr << "ERROR: " << s << ", found " << ans << ", expected " << result <<  endl;
            }
        }
        cout << ans << endl;
    }
    cerr << "Time execute: " << clock() / (double)CLOCKS_PER_SEC << " sec" << endl;
    return 0;
}
