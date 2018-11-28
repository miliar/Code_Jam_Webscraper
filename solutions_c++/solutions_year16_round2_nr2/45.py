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

string a, b;
string c, d;

struct ans {
    string c, d;
    ll x, y;
    ll diff;
    ans(const string &c, const string &d) : c(c), d(d) {
        x = y = 0;
        for (char ch : c) {
            x = x * 10 + ch - '0';
        }
        for (char ch : d) {
            y = y * 10 + ch - '0';
        }
        diff = abs(x - y);
    }
    bool operator < (const ans &rhs) const {
        if (diff != rhs.diff) {
            return diff < rhs.diff;
        } else {
            if (x != rhs.x) {
                return x < rhs.x;
            } else {
                return y < rhs.y;
            }
        }
    }
    bool operator == (const ans &rhs) const {
        return c == rhs.c && d == rhs.d;
    }
};

ans answer("", "");

void rec(int p) {
    if (p == a.size()) {
        answer = min(answer, ans(c, d));
        return;
    }

    bool eq = true;
    for (int i = 0; i < p; i++) {
        eq &= c[i] == d[i];
    }

    if (a[p] == '?' && b[p] == '?') {
        if (eq) {
            c[p] = '0';
            d[p] = '1';
            rec(p + 1);
            c[p] = '0';
            d[p] = '0';
            rec(p + 1);
            c[p] = '1';
            d[p] = '0';
            rec(p + 1);
        } else {
            c[p] = '0';
            d[p] = '9';
            rec(p + 1);
            c[p] = '9';
            d[p] = '0';
            rec(p + 1);
            //c[p] = '0';
            //d[p] = '0';
            //rec(p + 1);
        }
    } else if (a[p] == '?') {
        if (eq) {
            d[p] = b[p];
            if (b[p] > '0') {
                c[p] = b[p] - 1;
            }
            rec(p + 1);
            c[p] = b[p];
            rec(p + 1);
            if (b[p] + 1 <= '9') {
                c[p] = b[p] + 1;
                rec(p + 1);
            }
        } else {
            d[p] = b[p];
            c[p] = '0';
            rec(p + 1);
            c[p] = '9';
            rec(p + 1);
        }
    } else if (b[p] == '?') {
        if (eq) {
            c[p] = a[p];
            if (a[p] > '0') {
                d[p] = a[p] - 1;
            }
            rec(p + 1);
            d[p] = a[p];
            rec(p + 1);
            if (a[p] + 1 <= '9') {
                d[p] = a[p] + 1;
                rec(p + 1);
            }
        } else {
            c[p] = a[p];
            d[p] = '0';
            rec(p + 1);
            d[p] = '9';
            rec(p + 1);
        }
    } else {
        c[p] = a[p];
        d[p] = b[p];
        rec(p + 1);
    }
}

ans brute(string a, string b) {
    int ub = 1;
    for (int i = 0; i < a.size(); i++) {
        ub *= 10;
    }
    auto match = [](const string &a, const string &b) {
        for (int i = 0; i < a.size(); i++) {
            if (!(a[i] == b[i] || a[i] == '?')) {
                return false;
            }
        }
        return true;
    };

    ans answer("", "");
    answer.diff = 2e18;
    for (int i = 0; i < ub; i++) {
        string c;
        int x = i;
        for (int j = 0; j < a.size(); j++) {
            c += '0' + (x % 10);
            x /= 10;
        }
        reverse(c.begin(), c.end());
        if (!match(a, c)) {
            continue;
        }

        for (int j = 0; j < ub; j++) {
            string d;
            int y = j;
            for (int h = 0; h < a.size(); h++) {
                d += '0' + (y % 10);
                y /= 10;
            }
            reverse(d.begin(), d.end());
            if (!match(b, d)) {
                continue;
            }
            answer = min(answer, ans(c, d));
        }
    }
    return answer;
}

void gen() {
    ofstream out("a.in");
    int t = 100;
    out << t << endl;
    for (int i = 0; i < t; i++) {
        int n = 4;
        string a, b;
        for (int j = 0; j < n; j++) {
            if (rand() & 1) {
                a.push_back(rand() % 10 + '0');
            } else {
                a.pb('?');
            }
            if (rand() & 1) {
                b.push_back(rand() % 10 + '0');
            } else {
                b.pb('?');
            }
        }
        out << a << " " << b << endl;
    }
    out.close();
}

int main() {

#ifdef LOCAL
    //gen();
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#endif


    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++) {
        cerr << tt << endl;
        cin >> a >> b;
        c.resize(a.size());
        d.resize(b.size());

        answer.diff = 2e18;

        rec(0);

        //assert(brute(a, b) == answer);

        cout << "Case #" << tt << ": " << answer.c << " " << answer.d << endl;
    }

    return 0;
}
