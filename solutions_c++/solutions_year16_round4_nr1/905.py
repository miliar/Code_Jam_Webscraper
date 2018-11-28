#include <algorithm>
#include <assert.h>
#include <chrono>
#include <functional>
#include <numeric>
#include <math.h>
#include <memory.h>
#include <stdint.h>
#include <time.h>
#include <utility>

#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdio.h>

#include <bitset>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <vector>
#include <unordered_map>
#include <unordered_set>

#define ff first
#define ss second
#define pb push_back
#define sqr(x) ((x) * (x))
#define countbits __builtin_popcountll
#define print(a)            cerr << (a) << '\n'
#define dbg(a)              cerr << #a << " = " << (a) << '\n'
#define dbg2(a, b)          cerr << #a << " = " << (a) << " " << #b << " = " << (b) << '\n'
#define dbg3(a, b, c)       cerr << #a << " = " << (a) << " " << #b << " = " << (b) << " " << #c << " = " << (c) << '\n'
#define dbg4(a, b, c, d)    cerr << #a << " = " << (a) << " " << #b << " = " << (b) << " " << #c << " = " << (c) << " " << #d << " = " << (d) << '\n'
#define dbg5(a, b, c, d, e) cerr << #a << " = " << (a) << " " << #b << " = " << (b) << " " << #c << " = " << (c) << " " << #d << " = " << (d) << " " << #e << " = " << (e) << '\n'
#define PI 3.1415926535897932384626433

using std::cerr;
using std::cin;
using std::cout;

using std::bitset;
using std::deque;
using std::map;
using std::pair;
using std::queue;
using std::set;
using std::string;
using std::vector;
using std::unordered_map;
using std::unordered_set;

using std::abs;
using std::max;
using std::min;

using std::sort;
using std::swap;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ull, ull> pul;

void init() {
    #ifndef LOCAL
    comment this line
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    #endif
    cin.tie(0);
    std::iostream::sync_with_stdio(0);
    cout << std::fixed << std::setprecision(10);
    cerr << std::fixed << std::setprecision(10);
    srand(std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::high_resolution_clock::now().time_since_epoch()).count());
}
const char kek[3] = {'R', 'P', 'S'};
string check(int n, int r, int p, int s, int ft) {
    vector<int> arr((1 << (n + 1)) + 1);
    arr[1] = ft;
    for (int i = 2; i < (1 << (n + 1)); ++i) {
        int x = arr[i >> 1];
        if (x == 0) {
            if (i & 1) arr[i] = 2;
            else arr[i] = 0;
        } else if (x == 1) {
            if (i & 1) arr[i] = 0;
            else arr[i] = 1;
        } else {
            if (i & 1) arr[i] = 2;
            else arr[i] = 1;
        }
    }
    string ans;
    int rr = 0, ss = 0, pp = 0;
    for (int i = (1 << n); i < (1 << (n + 1)); ++i) {
        ans += kek[arr[i]];
        rr += (arr[i] == 0);
        pp += (arr[i] == 1);
        ss += (arr[i] == 2);
    }
    if (rr != r || ss != s || pp != p) return "a";
    // dbg(ans);
    for (int pw = 1; pw < n; ++pw) {
        for (int i = 0; i < (1 << n); i += ((1 << (pw + 1)))) {
            string one, two;
            for (int j = i; j < i + (1 << pw); ++j) {
                // dbg(j);
                one += ans[j];
                two += ans[j + (1 << pw)];
            }
            if (one > two)
                for (int j = i; j < i + (1 << pw); ++j)
                    swap(ans[j], ans[j + (1 << pw)]);
            // dbg4(pw, i, one, two);
        }
        // dbg(ans);
    }

    return ans;
}

int main() {
    init();


    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        int n, r, s, p;
        cin >> n >> r >> p >> s;
        string a = check(n, r, p, s, 0);
        string b = check(n, r, p, s, 1);
        string c = check(n, r, p, s, 2);
        string d = min(min(a, b), c);
        // print("ok");
        // dbg4(a, b, c, d);
        if (d == "a") cout << "Case #" << tt << ": IMPOSSIBLE\n";
        else cout << "Case #" << tt << ": " << d << '\n';
        // print("kek");
    }


    #ifdef LOCAL
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}
