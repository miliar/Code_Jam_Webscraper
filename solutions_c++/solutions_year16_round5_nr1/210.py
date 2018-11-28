#ifdef NALP_PROJECT
#pragma hdrstop
#else
#define _SECURE_SCL 0
#endif

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:200000000")

#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <utility>
#include <cassert>

#include <set>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <bitset>
#include <memory.h>

#include <iostream>
#include <fstream>
#include <sstream>

#ifdef _WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

using namespace std;

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define y1 YYY1
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()

template<typename T> inline T Abs(T x) { return (x >= 0) ? x : -x; }
template<typename T> inline T sqr(T x) { return x * x; }
template<typename T> inline string toStr(T x) { stringstream st; st << x; string s; st >> s; return s; }
template<typename T> inline int bit(T mask, int b) { return (b >= 0 && (mask & (T(1) << b)) != 0) ? 1 : 0; }
template<typename T1, typename T2> std::ostream& operator<<(std::ostream &out, const pair<T1, T2>& a) { out << "(" << a.first << ", " << a.second << ")"; return out; }
template<typename T> std::ostream& operator<<(std::ostream &out, const vector<T>& a) { out << "[" << a.size() << "]{ "; forn(i, a.size()) { out << a[i] << " "; } out << "}"; return out; }

inline int nextInt() { int x; if (scanf("%d", &x) != 1) throw; return x; }
inline int64 nextInt64() { int64 x; if (scanf(LLD, &x) != 1) throw; return x; }
inline double nextDouble() { double x; if (scanf("%lf", &x) != 1) throw; return x; }

const int INF = (int)1E9;
const int64 INF64 = (int64)1E18;
const long double EPS = 1E-9;
const long double PI = 3.1415926535897932384626433832795;

const int MAXN = 21100;

int n, d1[MAXN], d2[MAXN/100][MAXN/100];
int c[2][MAXN], j[2][MAXN];
string s;

inline int getcost(char l, char r) {
    if (l == r) return 10;
    return 5;
}

int get(int* s, int l, int r) {
    int ans = s[r];
    if (l > 0) ans -= s[l - 1];
    return ans;
}

int solve3(int l, int r) {
    int co = get(c[0], l, r);
    int ce = get(c[1], l, r);
    int jo = get(j[0], l, r);
    int je = get(j[1], l, r);
    int g = min(co, ce) + min(jo, je);
    return g * 10 + (r - l + 1 - 2*g) / 2 * 5;
}

int solve2(int l, int r) {
    assert((l + r) % 2 == 1);
    return solve3(l, r);

    if (l > r) return 0;
    int& ans = d2[l][r];
    if (ans != -1) return ans;

    ans = solve2(l + 1, r - 1) + getcost(s[l], s[r]);
    for(int mid = l + 1; mid < r; mid += 2) {
        ans = max(ans, solve2(l, mid) + solve2(mid + 1, r));
    }

    assert(ans == solve3(l, r));

    return ans;
}

int solve1(int v) {
    if (v == n) return 0;
    int& ans = d1[v];
    if (ans != -1) return ans;

    ans = solve1(v + 1);
    for (int u = v + 1; u < n; u += 2) {
        ans = max(ans, solve2(v, u) + solve1(u + 1));
    }

    return ans;
}

int stupid() {
    memset(d1, 255, sizeof d1);
    memset(d2, 255, sizeof d2);

    memset(c, 0, sizeof c);
    memset(j, 0, sizeof j);

    forn(i, n) {
        if (s[i] == 'C') {
            c[i % 2][i] = 1;
        } else {
            j[i % 2][i] = 1;
        }

        if (i > 0) {
            c[0][i] += c[0][i - 1];
            c[1][i] += c[1][i - 1];
            j[0][i] += j[0][i - 1];
            j[1][i] += j[1][i - 1];
        }
    };

//    for(int l = 2; l <= n; l += 2) {
//        cerr << l << endl;
//        forn(i, n) {
//            int ii = l + i - 1;
//            if (ii < n) {
//                solve2(i, ii);
//            }
//        }
//    }

    return solve1(0);
}

void solve(bool skipThisTest) {
    if (true) {
        cerr << "\tinput mode: read test." << endl;
        cin >> s;
        n = int(s.size());
        if (skipThisTest) return;
    } else {
        cerr << "\tinput mode: generated test." << endl;
        n = 20000;
        s = "";
        forn(i, n) {
            s += string("CJ")[rand() % 2];
        }
    }

    int ans = stupid();
    cout << ans << endl;

    cerr << "\tclever answer is '" << ans << "'." << endl;
    if (n <= 1000) {
        int stupidAnswer = stupid();
        cerr << "\tstupid answer is '" << stupidAnswer << "'." << endl;
        assert(ans == stupidAnswer);
    }
}

int main(int argc, char * argv[]) {
#ifdef NALP_PROJECT
    freopen("input.txt", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
#else
#endif

    int minTest = 1, maxTest = INF;
    if (argc == 3) {
        minTest = atoi(argv[1]);
        maxTest = atoi(argv[2]);
    }

    cout.precision(10);
    cout.setf(ios::fixed);

    cerr.precision(10);
    cerr.setf(ios::fixed);

    srand((unsigned int)time(0));
    int tests = nextInt();
    clock_t totalStartTime = clock();
    for(int test = 1; test <= tests; test++) {
        clock_t startTime = clock();
        cerr << "Case #" << test << endl;
        bool skipThisTest = (test < minTest || test > maxTest);
        if (!skipThisTest) cout << "Case #" << test << ": ";
        solve(skipThisTest);

        char formattedTime[100];
        clock_t time = clock() - startTime;
        sprintf(formattedTime, "%d.%03d", int(time / CLOCKS_PER_SEC), int(time % CLOCKS_PER_SEC));
        cerr << "time for test is " << formattedTime << " s." << endl << endl;
    }

    char formattedTime[100];
    clock_t totalTime = clock() - totalStartTime;
    sprintf(formattedTime, "%d.%03d", int(totalTime / CLOCKS_PER_SEC), int(totalTime % CLOCKS_PER_SEC));
    cerr << string(20, '=') << endl;
    cerr << "TOTAL TIME IS " << formattedTime << " s." << endl;

    return 0;
}
