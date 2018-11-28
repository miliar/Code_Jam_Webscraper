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

const int MAXN = 100100;

typedef int TRESULT;

const string V[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

string s;

bool add(vector<int>& a, const string& s, int cost) {
    bool ok = true;
    forn(i, s.size()) {
        const int c = s[i] - 'A';
        a[c] += cost;
        ok = ok && a[c] >= 0;
    }
    return ok;
}

bool go(vector<int>& a, int cur, int num, vector<char>& s) {
    if (num == 0) {
        return true;
    }

    if (cur == 10 || num < 0) {
        return false;
    }

    if (go(a, cur + 1, num, s)) {
        return true;
    }

    s.pb('0' + cur);
    bool ok = add(a, V[cur], -1);
    if (ok && go(a, cur, num - int(V[cur].size()), s)) {
        return true;
    }
    add(a, V[cur], +1);
    s.pop_back();

    return false;
}

string stupid() {
    vector<int> a(26, 0);
    forn(i, s.size()) {
        a[s[i] - 'A']++;
    }

    vector<char> ans;
    cerr << "X " << go(a, 0, int(s.size()), ans) << endl;
    return string(all(ans));
}

string process(map<char, int>& st, char c, int digit) {
    const int num = st[c];
    assert(num >= 0);
    forn(i, V[digit].size()) {
        st[V[digit][i]] -= num;
        assert(st[V[digit][i]] >= 0);
    }
    return string(num, '0' + digit);
}

void solve(bool skipThisTest) {
    if (true) {
        cerr << "\tinput mode: read test." << endl;
        cin >> s;
        if (skipThisTest) return;
    } else {
        cerr << "\tinput mode: generated test." << endl;
        // generate test.
    }

    string ans = "";
    map<char, int> st;
    forn(i, s.size()) {
        st[s[i]]++;
    }

    ans += process(st, 'Z', 0);
    ans += process(st, 'W', 2);
    ans += process(st, 'U', 4);
    ans += process(st, 'X', 6);
    ans += process(st, 'G', 8);
    ans += process(st, 'F', 5);
    ans += process(st, 'S', 7);
    ans += process(st, 'H', 3);
    ans += process(st, 'I', 9);
    ans += process(st, 'N', 1);
    sort(all(ans));
    cout << ans << endl;

    cerr << "\tclever answer is '" << ans << "'." << endl;
    if (s.size() <= 40) {
        string stupidAnswer = stupid();
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
