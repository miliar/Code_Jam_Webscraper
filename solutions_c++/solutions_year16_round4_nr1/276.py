#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <queue>
#include <math.h>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
#include <list>
#include <ctype.h>
#include <cassert>
#include <stack>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <ctime>
#include <functional>
#include <ctime>
#include <limits>
#include <tuple>
#include <complex>


using namespace std;

#define snd second
#define fst first
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define left _left
#define right _right

const ld pi = acos(-1.0l);

template<typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
    return x * x;
}

template<typename T>
void chmin(T &x, T y) {
    x = min(x, y);
}

template<typename T>
void chmax(T &x, T y) {
    x = max(x, y);
}

template<typename U, typename V>
ostream &operator<<(ostream &s, const pair<U, V> &x) {
    s << "(" << x.fst << ", " << x.snd << ")";
    return s;
}

template<typename U>
ostream &operator<<(ostream &s, const vector<U> &x) {
    s << "[";
    bool was = false;
    for (auto it : x) {
        if (was) {
            s << ", ";
        }
        was = true;
        s << it;
    }
    s << "]";
    return s;
}

template<typename U>
ostream &operator<<(ostream &s, const set<U> &x) {
    s << "{";
    bool was = false;
    for (auto it : x) {
        if (was) {
            s << ", ";
        }
        was = true;
        s << it;
    }
    s << "}";
    return s;
}

template<int sz>
ostream operator<<(ostream &s, const bitset<sz> &x) {
    for (int i = 0; i < sz; i++) {
        s << x[i];
    }
    return s;
}


//-----------------------------------------------------------------------------

// 0 - r, 1 - p, 2 - s
int win[3][3] =  {
        0, 0, 1,
        1, 0, 0,
        0, 1, 0,
};

string brute(int r, int pp, int s) {
    int n = r + pp + s;
    vector<int> a;
    for (int i = 0; i < r; i++) {
        a.pb(0);
    }
    for (int i = 0; i < pp; i++) {
        a.pb(1);
    }
    for (int i = 0; i < s; i++) {
        a.pb(2);
    }
    vector<int> p(n);
    iota(p.begin(), p.end(), 0);
    string ans = "Z";
    do {
        vector<int> c;
        for (int x : p) {
            c.pb(a[x]);
        }

        bool good = true;
        while (c.size() > 1) {
            vector<int> d;
            for (int i = 0; i < c.size(); i += 2) {
                if (c[i] == c[i + 1]) {
                    good = false;
                    break;
                }
                if (win[c[i]][c[i + 1]]) {
                    d.pb(c[i]);
                } else {
                    d.pb(c[i + 1]);
                }
            }
            if (!good) {
                break;
            }
            c = d;
        }

        if (good) {
            string c;
            for (int x : p) {
                if (a[x] == 0) {
                    c += 'R';
                } else if (a[x] == 1) {
                    c += 'P';
                } else {
                    c += 'S';
                }
            }
            chmin(ans, c);
        }
    } while (next_permutation(p.begin(), p.end()));
    return ans;
}


bool possible(vector<int> c) {
    bool good = true;
    while (c.size() > 1) {
        vector<int> d;
        for (int i = 0; i < c.size(); i += 2) {
            if (c[i] == c[i + 1]) {
                good = false;
                break;
            }
            if (win[c[i]][c[i + 1]]) {
                d.pb(c[i]);
            } else {
                d.pb(c[i + 1]);
            }
        }
        if (!good) {
            break;
        }
        c = d;
    }
    return good;
}

string smart(int r, int p, int s) {
    if (r < 0 || p < 0 || s < 0) {
        return "";
    }

    if (r + p + s == 1) {
        if (r == 1) {
            return "R";
        } else if (s == 1) {
            return "S";
        } else {
            return "P";
        }
    }


    int n = r + p + s;
    int x = r + s - n / 2;

    auto res = smart(x, r - x, s - x);

    if (res.empty()) {
        return res;
    }

    string ans;
    for (char c : res) {
        if (c == 'R') {
            ans += "RS";
        } else if (c == 'S') {
            ans += "PS";
        } else {
            ans += "PR";
        }
    }

    return ans;
}


string normalize(string s) {
    if (s.size() <= 1) {
        return s;
    }
    auto a = string(s.begin(), s.begin() + s.size() / 2);
    auto b = string(s.begin() + s.size() / 2, s.end());

    a = normalize(a);
    b = normalize(b);

    if ((a + b) < (b + a)) {
        return a + b;
    } else {
        return b + a;
    }
}

int main() {

#ifdef LOCAL
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#endif


    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++) {
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        //auto ans = brute(r, p, s);
        auto ans = normalize(smart(r, p, s));


        cout << "Case #" << tt << ": " << fixed << (ans == "" ? "IMPOSSIBLE" : ans) << endl;
        //cout << "Case #" << tt << ": " << fixed << (ans == "Z" ? "IMPOSSIBLE" : ans) << endl;
    }


    return 0;
}
