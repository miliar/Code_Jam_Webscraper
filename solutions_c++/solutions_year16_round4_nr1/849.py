#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cassert>
#include <map>
#include <string>
#include <iomanip>
#include <set>
#include <queue>
#include <ctime>
#include <vector>
using namespace std;

#define FOR(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define sz(v) (int)(v).size()
#define mp make_pair
#define all(v) (v).begin(), (v).end()
typedef double LD;
//typedef long long LL;

const int N = 1 << 12;

int n;
int prea[12];
int preb[12];
int prec[12];

string calc(int round, int R, int P, int S) {
    int cnt = n >> round;
    assert(cnt == R + P + S);
    if (cnt == 1) {
        if (R == 1) return "R";
        if (S == 1) return "S";
        if (P == 1) return "P";
    }

    if (R + P - S < 0 || (R + P - S) % 2 == 1) return "";
    if (-R + P + S < 0 || (-R + P + S) % 2 == 1) return "";
    if (R - P + S < 0 || (R - P + S) % 2 == 1) return "";

    int a = (R + P - S) / 2;
    int b = (R + S - P) / 2;
    int c = (P + S - R) / 2;

    prea[round] = a;
    preb[round] = b;
    prec[round] = c;

    int newR = b;
    int newP = a;
    int newS = c;

    string st = calc(round + 1, newR, newP, newS);
    if (st == "") return "";
    string ret;
    FOR(i, sz(st)) {
        if (st[i] == 'R') ret += "RS";
        if (st[i] == 'P') ret += "PR";
        if (st[i] == 'S') ret += "PS";
    }
    return ret;
}

string sort(string st) {
    for (int r = 0; (1 << r) < sz(st); ++r) {
        string ret = "";
        for (int i = 0; i < sz(st); i += 2 * (1 << r)) {
            string a = st.substr(i, 1 << r);
            string b = st.substr(i + (1 << r), (1 << r));
            if (a < b) ret += a, ret += b;
            else ret += b, ret += a;
        }
        st = ret;
    }
    return st;
}

void solve() {
    
    int T;
    scanf("%d", &T);
    //cin >> T;
    for (int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);

        int R, P, S;
        scanf("%d%d%d%d", &n, &R, &P, &S);
        n = 1 << n;

        string st = calc(0, R, P, S);
        if (sz(st)) printf("%s\n", sort(st).c_str());
        else printf("IMPOSSIBLE\n");
    }
}

void testgen() {
    FILE *f = fopen("input.txt", "w");
    srand(time(0));
    fclose(f);
}

int  main(int argc, char* argv[]) {
#ifdef harhro94
    //testgen();
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    #define task "estimate"
    //freopen(task".in", "r", stdin);
    //freopen(task".out", "w", stdout);
#endif

    solve();

#ifdef harhro94
    cerr << "\ntime = " << clock() / 1000.0 << endl;
#endif
    return 0;
}