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

const int MAXN = 210;

int n, k;
long double m[MAXN][MAXN];
long double a[MAXN];

long double get(vector<long double>& x) {
    forn(i, x.size() + 2) {
        forn(j, x.size() + 2) {
            m[i][j] = 0;
        }
    }

    m[0][0] = 1;
    forn(i, x.size()) {
        forn(j1, i + 1) {
            int j2 = i - j1;
            m[j1 + 1][j2] += m[j1][j2] * x[i];
            m[j1][j2 + 1] += m[j1][j2] * (1 - x[i]);
        }
    }

    return m[x.size() / 2][x.size() / 2];
}

long double gen(int v, vector<long double>& x) {
    if (int(x.size()) == k) {
        return get(x);
    }
    if (v == n) {
        return 0;
    }

    long double ans = gen(v + 1, x);
    x.push_back(a[v]);
    ans = max(ans, gen(v + 1, x));
    x.pop_back();
    return ans;
}

long double stupid() {
    vector<long double> x;
    return gen(0, x);
}

long double clever() {
    vector<long double> aa(a, a + n);
    sort(all(aa));
    long double ans = 0;
    forn(fs, k + 1) {
        vector<long double> aaa;
        aaa.insert(aaa.begin(), aa.begin(), aa.begin() + fs);
        aaa.insert(aaa.begin(), aa.end() - (k - fs), aa.end());
        assert(aaa.size() == k);
        ans = max(ans, get(aaa));
    }
    return ans;
}

void solve(bool skipThisTest) {
    if (true) {
        cerr << "\tinput mode: read test." << endl;
        n = nextInt();
        k = nextInt();
        forn(i, n) {
            cin >> a[i];
        }
        if (skipThisTest) return;
    } else {
        n = 16;
        k = (rand() % (n / 2 + 1)) * 2;
        forn(i, n) {
            a[i] = (rand() % 1000) / 1000.0;
        }
        cerr << "\tinput mode: generated test." << endl;
        // generate test.
    }

    long double ans = clever();
    cout << ans << endl;

    cerr << "\tclever answer is '" << ans << "'." << endl;
    if (n <= 16) {
        long double stupidAnswer = stupid();
        cerr << "\tstupid answer is '" << stupidAnswer << "'." << endl;
        assert(fabs(ans - stupidAnswer) < EPS);
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
