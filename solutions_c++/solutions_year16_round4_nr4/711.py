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

int n;
char arr[4][4];
bool can(vector<int> line, uint m, vector<char> used, int k) {
    if (k == n) {
        for (int i = 0; i < n; ++i)
            if (!used[i])
                return false;
        return true;
    }
    int brr[n][n];
    for (int i = 0; i < n; ++i)    
        for (int j = 0; j < n; ++j)
            if (m & (1 << (i * n + j)))
                brr[i][j] = 1;
            else
                brr[i][j] = 0;
    int cur = line[k];
    bool ans = true, ways = false;
    for (int i = 0; i < n; ++i) {
        if (brr[cur][i] && !used[i]) {
            used[i] = true;
            ans &= can(line, m, used, k + 1);
            used[i] = false;
            ways = true;
        }
    }
    ans &= ways;
    return ans; 
}
int check(uint m) {
    // dbg(bitset<4>(m));
    int brr[n][n];
    for (int i = 0; i < n; ++i)    
        for (int j = 0; j < n; ++j)
            if (m & (1 << (i * n + j)))
                brr[i][j] = 1;
            else
                brr[i][j] = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (arr[i][j] == 1 && brr[i][j] == 0)
                return -1;
    vector<int> fc;
    for (int i = 0; i < n; ++i)
        fc.pb(i);
    vector<int> cp = fc;
    // if (m == 156) {
    //     print("");
    //     for (int i = 0; i < n; ++i) {
    //         for (int j = 0; j < n; ++j)
    //             cout << int(brr[i][j]);
    //         cout << '\n';
    //     }
    // }
    do {
        std::next_permutation(fc.begin(), fc.end());
        if (!can(fc, m, vector<char>(n, 0), 0)) return -1;
    } while (fc != cp);
    int cnt = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            if (arr[i][j] == 0 && brr[i][j] == 1)
                ++cnt;
    return cnt;
}

int main() {
    init();

    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        cin >> n;
        for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) cin >> arr[i][j];
        for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) arr[i][j] -= '0';
        int mn = n * n;
        for (uint m = 0; m < (1u << (n * n)); ++m) {
            int x = check(m);
            // if (x!=-1) dbg3(m, bitset<9>(m), x);
            if (x != -1)
                mn = min(x, mn);
        }
        cout << "Case #" << tt << ": " << mn << '\n';
    }




    #ifdef LOCAL
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}
