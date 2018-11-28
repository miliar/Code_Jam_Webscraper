#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <climits>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>
#include <algorithm>
#include <assert.h>
#include <unordered_map>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector < long long > vll;
typedef pair <long long, long long> pll;
typedef pair <int, int> pii;
typedef vector < int > vii;
typedef complex < double > Point;

#define csl ios_base::sync_with_stdio(false); cin.tie(NULL)
#define mp make_pair
#define fst first
#define snd second
#define prev PREV
ll t, n, m, u, v, q, r, ql, qr, k, l, s, w, h, c, z, d, y, x, a;
const int N = 1e5 + 500;
const int K = 1e6 + 500;
const int LN = 20;
const long long mod = 1e9 + 7;
const long long INF = 1LL << 52LL;
const bool JUDGE = false;
ll p;
string str;
queue < pair < char, int > > Q;
string solve(int n, int r, int p, int s) {
    Q = queue < pair <char, int> > ();
    Q.push(mp('p', 0));
    str = "";
    int R = 0, P = 0, S = 0;
    while (!Q.empty()) {
        pair <char, int> f = Q.front();
        Q.pop();
        if (f.snd == n) {
            str += f.fst;
            if (f.fst == 'r') R++;
            else if (f.fst == 'p') P++;
            else S++;
            continue;
        }
        else {
            if (f.fst == 'r') {
                Q.push(mp('r', f.snd + 1));
                Q.push(mp('s', f.snd + 1));
            } else if (f.fst == 'p') {
                Q.push(mp('p', f.snd + 1));
                Q.push(mp('r', f.snd + 1));
            } else {
                Q.push(mp('p', f.snd + 1));
                Q.push(mp('s', f.snd + 1));
            }
        }
    }
    if (R == r && P == p && S == s)
        return str;
    str = "";
    Q.push(mp('r', 0));
    R = 0, P = 0, S = 0;
    while (!Q.empty()) {
        pair <char, int> f = Q.front();
        Q.pop();
        if (f.snd == n) {
            str += f.fst;
            if (f.fst == 'r') R++;
            else if (f.fst == 'p') P++;
            else S++;
            continue;
        }
        else {
            if (f.fst == 'r') {
                Q.push(mp('r', f.snd + 1));
                Q.push(mp('s', f.snd + 1));

            } else if (f.fst == 'p') {
                Q.push(mp('p', f.snd + 1));
                Q.push(mp('r', f.snd + 1));

            } else {
                Q.push(mp('p', f.snd + 1));
                Q.push(mp('s', f.snd + 1));

            }
        }
    }
    if (R == r && P == p && S == s)
        return str;
    str = "";
    Q.push(mp('s', 0));
    R = 0, P = 0, S = 0;
    while (!Q.empty()) {
        pair <char, int> f = Q.front();
        Q.pop();
        if (f.snd == n) {
            str += f.fst;
            if (f.fst == 'r') R++;
            else if (f.fst == 'p') P++;
            else S++;
            continue;
        }
        else {
            if (f.fst == 'r') {
                Q.push(mp('r', f.snd + 1));
                Q.push(mp('s', f.snd + 1));

            } else if (f.fst == 'p') {
                Q.push(mp('p', f.snd + 1));
                Q.push(mp('r', f.snd + 1));

            } else {
                Q.push(mp('p', f.snd + 1));
                Q.push(mp('s', f.snd + 1));

            }
        }
    }
    if (R == r && P == p && S == s)
        return str;
    else return "impossible";
}
int main() {
    csl;
    if (JUDGE) {
        freopen("angry.in", "r", stdin);
        freopen("angry.out", "w", stdout);
    }
    cin >> t;
    for (int ii = 1; ii <= t; ++ii) {
        cin >> n >> r >> p >> s;
        str = "";
        cout << "Case #" << ii << ": ";
        str = solve(n, r, p, s);
        for (int i = 0; i < str.size(); ++i)
            str[i] += 'A' - 'a';
        if (str != "IMPOSSIBLE")
        for (int i = 1; i < str.size(); i <<= 1) {
            for (int j = 0; j < str.size(); j += (i << 1)) {
                bool swap = false;
                for (int k = 0; k < i; ++k) {
                    if (str[j + k] == str[j + i + k]) continue;
                    if (str[j + k] < str[j + i + k]) {
                        break;
                    } else {
                        swap = true; break;
                    }
                }
                if (swap)
                    for (int k = 0; k < i; ++k)
                        std::swap(str[j + k], str[j + i + k]);
            }
        }
        cout << str;
        cout << '\n';
    }
    return 0;
}















