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

inline int nextInt() { int x; if (scanf("%d", &x) != 1) throw; return x; }
inline int64 nextInt64() { int64 x; if (scanf(LLD, &x) != 1) throw; return x; }
inline double nextDouble() { double x; if (scanf("%lf", &x) != 1) throw; return x; }

const int INF = (int)1E9;
const int64 INF64 = (int64)1E18;
const long double EPS = 1E-9;
const long double PI = 3.1415926535897932384626433832795;

const int MAXN = 100100;

long double V, X, s[MAXN], x[MAXN];
int n;

long double sum(const vector<pair<long double, long double> >& a, long double v) {
    long double sumv = 0, sumt = 0;
    forn(i, a.size()) {
        long double cur = min(v, a[i].second);
        sumt += a[i].first * cur;
        sumv += cur;
        v -= cur;
    }

    return sumt / sumv;
}

long double solve(long double t) {
    vector<pair<long double, long double> > a;
    long double summ = 0;
    forn(i, n) {
        a.pb(mp(x[i], t * s[i]));
        summ += t * s[i];
    }

    if (summ < V) {
        return false;
    }

    sort(all(a));
    long double tmin = sum(a, V);
    reverse(all(a));
    long double tmax = sum(a, V);
    return tmin <= X && X <= tmax;
}

long double stupid() {
    long double ans = 1E40;
    forn(i, n) {
        if (abs(X - x[i]) < EPS) {
            ans = min(ans, V / s[i]);
        }
    }

    if (n > 1 && abs(x[0] - x[1]) < EPS && abs(x[0] - X) < EPS) {
        ans = min(ans, V / (s[0] + s[1]));
    }

    if (n > 1 && abs(x[0] - x[1]) > EPS && ans > 1E20) {
        long double v0 = V * (X - x[1]) / (x[0] - x[1]), v1 = V - v0;
        if (v0 > -EPS && v1 > -EPS) {
            ans = min(ans, max(v0 / s[0], v1 / s[1]));
        }
    }

    return ans;
}

void solve(bool skipThisTest) {
    if (true) {
        cerr << "\tinput mode: read test." << endl;
        cin >> n >> V >> X;
        forn(i, n) {
            cin >> s[i] >> x[i];
        }
        // read test.
        if (skipThisTest) return;
    } else {
        cerr << "\tinput mode: generated test." << endl;
        n = 2;
        V = (rand() % 10000 + 1) / 100.0;
        X = (rand() % 10000 + 1) / 100.0;
        forn(i, n) {
            s[i] = (rand() % 10000 + 1) / 100.0;
            x[i] = (rand() % 10000 + 1) / 100.0;
        }
    }

    long double l = 0, r = 1E50;
    forn(i, 600) {
        long double mid = (l + r) * 0.5;
        if (solve(mid)) {
            r = mid;
        } else {
            l = mid;
        }
    }

    long double ans = (l + r) / 2;

    long double sumS = 0;
    forn(i, n) {
        if (abs(X - x[i]) < EPS) {
            sumS += s[i];
        }
    }

    if (sumS > EPS) {
        ans = min(ans, V / sumS);
    }

    if (ans > 1E20) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << ans << endl;
    }

    cerr << "\tclever answer is '" << ans << "'." << endl;
    if (n <= 2) {
        long double stupidAnswer = stupid();
        cerr << "\tstupid answer is '" << stupidAnswer << "'." << endl;
        if (ans > 1E20 && stupidAnswer < 1E20) {
            throw;
        }

        if (ans < 1E20 && stupidAnswer > 1E20) {
            throw;
        }

        if (ans < 1E20 && stupidAnswer < 1E20) {
            assert(abs(ans - stupidAnswer) < 1E-7);
        }
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

    cout.precision(14);
    cout.setf(ios::fixed);

    cerr.precision(14);
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
