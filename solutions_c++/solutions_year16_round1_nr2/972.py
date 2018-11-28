#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#pragma comment(linker, "/STACK:64000000")

template<class T> inline T sqr (T x) {return x * x;}

typedef unsigned uint;
typedef long long lng;
typedef unsigned long long ulng;
typedef long double ld;
typedef pair<int, int> PII;
typedef pair<lng, int> PLI;
typedef pair<lng, lng> PLL;
typedef pair<int, PII> PIII;
typedef pair<lng, PII> PLII;
#define FAIL ++*(int*)0
#define left asdleft
#define right asdright
#define mp make_pair
#define pb push_back
#define clr(ar,val) memset(ar, val, sizeof(ar))
#define sz(C) (int)((C).size())
#define all(C) (C).begin(), (C).end()
#define RR 151
#define X first
#define Y second
const int INF = 1000*1000*1000;
const lng LINF = INF * 1ll * INF;
const double EPS = 1e-9;

#define TASK "B"

vector<int> doit(vector<vector<int>> src) {
    map<int, int> cnt;
    for (const auto &a : src) {
        for (int x : a) {
            ++cnt[x];
        }
    }
    vector<int> ans;
    for (auto p : cnt) {
        if (p.Y % 2 == 1) {
            ans.push_back(p.X);
        }
    }
    sort(all(ans));
    if (sz(ans) != (sz(src) + 1) / 2) exit(66);
    return ans;
}

void solve() {
    int n;
    cin >> n;
    vector<vector<int>> src(2 * n - 1, vector<int>(n));
    for (int i = 0; i < 2 * n - 1; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> src[i][j];
        }
    }
    auto ans = doit(src);
    for (int x : ans) {
        cout << x << ' ';
    }
    cout << endl;
}

void stress() {
    for (int n = 2; n <= 50; ++n) {
        cerr << n << endl;
        for (int t = 0; t < 1000; ++t) {
            int md = (n * n);
            vector<vector<int>> a(n, vector<int>(n));
            int left = 1;
            for (int i = 0; i < n; ++i) {
                a[i][i] = rand() % md + left;
                left = a[i][i] + 1;

                int l1 = left;
                for (int j = i + 1; j < n; ++j) {
                    a[i][j] = rand() % md + l1;
                    l1 = a[i][j] + 1;
                }
                int l2 = left;
                for (int j = i + 1; j < n; ++j) {
                    a[j][i] = rand() % md + l2;
                    l2 = a[j][i] + 1;
                }
                left = max(l1, l2);
            }
            vector<vector<int>> src;
            for (int i = 0; i < n; ++i) {
                src.push_back(a[i]);
                src.emplace_back();
                for (int j = 0; j < n; ++j) {
                    src.back().push_back(a[j][i]);
                }
            }
            random_shuffle(all(src));
            auto ans = src.back();
            src.pop_back();
            
            auto res = doit(src);
            if (ans != res) {
                cerr << "FAIL" << endl;
                /*cerr << "HAVE: " << res << endl;
                cerr << "NEED: " << ans << endl;*/
                exit(123);
            }
        }
    }
    cerr << "PASSED" << endl;
}

//#define DEBUG
//#define SMALL
#define LARGE

int main() {
#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
#ifdef SMALL                                   
    freopen(TASK "-small-attempt0.in", "r", stdin);
    freopen(TASK "-small-attempt0.out", "w", stdout);
#endif
#ifdef LARGE
    freopen(TASK "-large.in", "r", stdin);
    freopen(TASK "-large.out", "w", stdout);
#endif

	//stress();

	int T;
	char buf[32];
    fgets(buf, sizeof buf, stdin);
    sscanf(buf, "%d", &T);
    for (int test = 1; test <= T; ++test) {
        fprintf(stderr, "Test %d is in progress...", test);
        printf("Case #%d: ", test);
        solve();
        fprintf(stderr, "done.\n");
    }


    return 0;
}
