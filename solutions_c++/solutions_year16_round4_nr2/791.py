#pragma comment (linker, "/STACK:128000000")
#include <iostream>
#include <cstdio>
#include <fstream>
#include <functional>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <bitset>
#include <ctime>
#include <sstream>
#include <stack>
#include <cassert>
#include <list>
#include <deque>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef long long li;
typedef long long i64;
typedef pair <int, int> pi;
typedef vector <int> vi;
typedef double ld;
typedef vector<int> vi;
typedef pair <int, int> pi;

void solve();

//int timer = 0;
#define FILENAME ""

int main() {
    string s = FILENAME;
#ifdef YA
    //assert(!s.empty());
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //cerr<<FILENAME<<endl;
    //assert (s != "change me please");
    clock_t start = clock();
#else
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    //freopen(FILENAME ".in", "r", stdin);
    //freopen(FILENAME ".out", "w", stdout);
    cin.tie(0);
#endif
    cout.sync_with_stdio(0);
    cout.precision(10);
    cout << fixed;
    int t = 1;

    cin >> t;
    for (int i = 1; i <= t; ++i) {
        //++timer;
        cerr << i << endl;
        cout << "Case #" << i << ": ";
        solve();
    }
#ifdef YA
    cerr << "\n\n\n" << (clock() - start) / 1.0 / CLOCKS_PER_SEC << "\n\n\n";
#endif
    return 0;
}

void solve() {
    int n, k;
    cin >> n >> k;
    vector <ld> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    ld ans = 0;

    for (int mask = 0; mask < (1 << n); ++mask) {
        vector <ld> cur;
        for (int i = 0; i < n; ++i) {
            if ((1 << i) & mask) {
                cur.push_back(a[i]);
            }
        }
        if (cur.size() != k) {
            continue;
        }
        ld sum = 0;
        for (int mask2 = 0; mask2 < (1 << k); ++mask2) {
            ld curx = 1.0;
            int cursum = 0;
            for (int i = 0; i < k; ++i) {
                if ((1 << i) & mask2) {
                    curx *= (1.0 - cur[i]);
                    ++cursum;
                }
                else {
                    curx *= cur[i];
                    --cursum;
                }
            }
            if (cursum == 0) {
                sum += curx;
            }
        }
        ans = max(ans, sum);
    }
    cout << ans << endl;
}