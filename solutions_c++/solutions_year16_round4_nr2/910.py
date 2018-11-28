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



int main() {
    init();

    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        int n, k;
        cin >> n >> k;
        vector<double> arr(n);
        for (auto &i : arr) cin >> i;
        double mx = 0;
        for (uint mask = 0; mask < (1u << n); ++mask) {
            if (countbits(mask) != k) continue;
            double sum = 0;
            // dbg(bitset<2>(mask));
            for (uint s = mask;; s = (s - 1) & mask) {
                // dbg(bitset<2>(s));
                double cur = 1;
                int yes = 0, no = 0;
                for (int j = 0; j < n; ++j)
                    if (mask & (1 << j)) {
                        if (s & (1 << j)) {
                            cur *= arr[j];
                            ++yes;
                        }
                        else {
                            cur *= (1.0 - arr[j]);
                            ++no;
                        }
                    }
                // dbg3(yes, no, cur);
                if (yes == no)
                    sum += cur;
                if (s == 0) break;
            }
            mx = max(mx, sum);
        }
        cout << "Case #" << tt << ": " << mx << '\n';
    }



    #ifdef LOCAL
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    #endif
    return 0;
}
