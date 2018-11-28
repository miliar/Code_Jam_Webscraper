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

char get_win(char a, char b) {
    assert(a != b);
    return ((a == 'R' && b == 'S') || (a == 'S' && b == 'P') || (a == 'P' && b == 'R'))? a : b;
}

const int MAXN = 13;

map <ll, char> m;

char rec(int r, int p, int s)
{
    //cout << r << " " << p << " " << s << " " << endl;
    if (r < 0 || p < 0 || s < 0) {
        return 0;
    }

    if (r + p + s == 1) {
        if (r) return 'R';
        if (s) return 'S';
        if (p) return 'P';
    }

    ll state = 0;
    (state += r) <<= MAXN;
    (state += p) <<= MAXN;
    (state += s) <<= MAXN;

    if (m.find(state) != m.end()) {
        return m[state];
    }
    char& res = m[state];
    res = 0;

    for (int i = 0; i <= r && i <= p; ++i) {
        int _p = i;

        if (p - i > s) {
            continue;
        }
        int _s = p - i;

        if (r - i != s - _s) {
            continue;
        }
        int _r = r - i;
        res = rec(_r, _p, _s);
        if (res) {
            break;
        }
    }
    //cout << r << " " << p << " " << s << " " << (char)res << endl;
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
        int n, p, r, s;
        cin >> n >> r >> p >> s;
        char res = rec(r, p, s);
        if (!res) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }
        //cout << (char)res << endl;
        string a = string(1, res);
        for (int i = 0; i < n; ++i) {
            string b = "";
            for (int j = 0; j < (int)a.size(); ++j) {
                switch (a[j]) {
                    case 'P': b += "PR"; break;
                    case 'S': b += "PS"; break;
                    case 'R': b += "RS"; break;
                }
            }
            a = b;
        }
        for (int i = 0; i < n; ++i) {
            vector <string> v;
            for (int j = 0; j < (1 << n); j += (1 << i)) {
                v.push_back(a.substr(j, 1 << i));
            }
            a = "";
            for (int j = 0; j < (int)v.size(); j += 2) {
                if (v[j] > v[j + 1]) {
                    swap(v[j], v[j + 1]);
                }
                a += v[j];
                a += v[j + 1];
            }
        }
        cout << a;
        cout << endl;
    }

    cerr << "Time execute: " << clock() / (double)CLOCKS_PER_SEC << " sec" << endl;
    return 0;
}
