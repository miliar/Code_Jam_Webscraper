#ifdef DEBUG
//#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;

int dp[1<<20];
int cnt[1<<20];
double arr[20];
double a[20], b[20];

int count(int x) {
    int ret = 0;
    while (x) {
        if (x & 1) {
            ++ret;
        }
        x >>= 1;
    }
    return ret;
}

int main() {
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    for (int i = 0; i < (1 << 20); ++i) {
        cnt[i] = count(i);
    }
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        int N;
        cin >> N;
        for (int i = 0; i < N; ++i) {
            cin >> arr[i];
            a[i] = arr[i];
        }
        for (int i = 0; i < N; ++i) {
            cin >> arr[i + N];
            b[i] = arr[i + N];
        }
        memset(dp, 0, sizeof dp);
        for (int i = 0; i < N; ++i) {
            for (int mask = 0; mask < (1 << (2 * N)); ++mask) {
                if (cnt[mask & ((1 << N) - 1)] != i || cnt[mask >> N] != i) {
                    continue;
                }
                for (int f = 0; f < N; ++f) {
                    for (int s = 0; s < N; ++s) {
                        if ((mask & (1 << f)) || ((mask & (1 << (s + N))))) {
                            continue;
                        }
                        int nmask = mask | (1 << f) | (1 << (s + N));
                        if (a[f] > b[s]) {
                            dp[nmask] = max(dp[nmask], dp[mask] + 1);
                        } else {
                            dp[nmask] = max(dp[nmask], dp[mask]);
                        }
                    }
                }
            }
        }
        int s = dp[(1 << (2 * N)) - 1];
        sort(a, a + N);
        sort(b, b + N);
        int p1 = 0, p2 = 0;
        while (p2 < N) {
            if (a[p1] < b[p2]) {
                ++p1;
                ++p2;
            } else {
                ++p2;
            }
        }
        int f = N - p1;
        printf("%d %d\n", s, f);
    }
    return 0;
}
