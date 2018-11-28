#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <bitset>
#define _USE_MATH_DEFINES
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <assert.h>
#include <stdlib.h>
using namespace std;

void smain();
int main(){
#ifdef TASK
    //freopen(TASK".in","rt",stdin);
    freopen("/Users/ramis/Downloads/A-large.in.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
    const clock_t start = clock();
#endif
    smain();
#ifdef TASK
    cerr << "\nTotal Execution Time: " << float( clock () - start ) /  CLOCKS_PER_SEC << endl;
#endif
    return 0;
}

#ifndef M_PI
#define M_PI 3.14159265358979311599796346854418516
#endif
#define forn(i,n) for (int i=0;i<n;i++)
#define rforn(i,n) for (int i=n-1;i>=0;i--)
#define int long long
#define LL long long
#define mp(a,b) make_pair(a,b)
#define INF 2305843009213693951LL
#define MOD 1000000007
#define EPS 1E-9
#define N 1000001
/* --------- END TEMPLATE CODE --------- */

int n, R, P, S;

inline char winner(char a, char b) {
    if (a == 'P') {
        if (b == 'S') return b;
        if (b == 'R') return a;
        assert(false);
    } else if (a == 'S') {
        if (b == 'P') return a;
        if (b == 'R') return b;
        assert(false);
    } else if (a == 'R') {
        if (b == 'P') return b;
        if (b == 'S') return a;
        assert(false);
    }
    assert(false);
}

string cur;
bool valid(string a) {
    int tr = R, tp = P, ts = S;
    for (auto c : a) {
        if (c == 'R') tr -= 1;
        else if (c == 'S') ts -= 1;
        else tp -= 1;
    }
    if (tr != 0 || ts != 0 || tp != 0) return false;
    string b;
    b.reserve(a.size());
    while (a.length() != 1) {
        int m = (int)a.size();
        b.clear();
        for (int i = 0; i < m; i += 2) {
            if (a[i] == a[i + 1]) return false;
            b.push_back(winner(a[i], a[i + 1]));
        }
        swap(a, b);
    }
    return true;
}
bool dfs(int k, int p, int r, int s) {
    if (k == 0) return valid(cur);
    if (p > 0) {
        cur.push_back('P');
        if (dfs(k - 1, p - 1, r, s)) return true;
        cur.pop_back();
    }
    if (r > 0) {
        cur.push_back('R');
        if (dfs(k - 1, p, r - 1, s)) return true;
        cur.pop_back();
    }
    if (s > 0) {
        cur.push_back('S');
        if (dfs(k - 1, p, r, s - 1)) return true;
        cur.pop_back();
    }
    return false;
}

string naive() {
    cur.clear();
    if (dfs(1 << n, P, R, S)) return cur;
    return "IMPOSSIBLE";
}

string calc(int k, char w) {
    if (k == 1) return string(1, w);
    char l;
    if (w == 'R') l = 'S';
    else if (w == 'S') l = 'P';
    else l = 'R';
    string a = calc(k / 2, w), b = calc(k / 2, l);
    if (a < b) return a + b;
    return b + a;
}
string solve() {
    string a = calc(1 << n, 'R');
    string b = calc(1 << n, 'S');
    string c = calc(1 << n, 'P');
    string res;
    if (valid(a)) res = a;
    if (valid(b)) {
        if (res.empty() || b < res) res = b;
    }
    if (valid(c)) {
        if (res.empty() || c < res) res = c;
    }
    if (res.empty()) return "IMPOSSIBLE";
    return res;
}

void smain() {
    cin >> n;
    forn(t, 0) {
        n = rand() % 4 + 1;
        int m = 1 << n;
        R = rand() % m;
        P = rand() % (m - R);
        S = m - R - P;
        assert(S + R + P == m);
        string res = solve();
        string ans = naive();
        assert(res == ans);
        cerr << res << endl;
    }
    for (int cas = 1; cin >> n >> R >> P >> S; ++cas) {
        string res = solve();
        cout << "Case #" << cas << ": " << res << endl;
        cerr << "Case #" << cas << ": " << res << endl;
    }
}
