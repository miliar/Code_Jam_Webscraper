#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <vector>
#include <string>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;
#define bitAt(x, k) (((x) >> (k)) & 1)
typedef long long LL;
typedef long double LD;
const int MOD = 1000000000 + 7;
const int INF = 1000000000;
const double EPS = 1e-9;
const double PI = acos(-1.0);
const int N = 1005;

int n, a[N], b[N];

void solve() {
    scanf("%d", &n);
    for (int i = 1; i <= n; ++i) {
        scanf("%d", &a[i]);
    }
    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        int L = 0, R = 0;
        for (int j = 1; j < i; ++j) {
            if (a[j] > a[i]) {
                ++L;
            }
        }
        for (int j = i + 1; j <= n; ++j) {
            if (a[j] > a[i]) {
                ++R;
            }
        }
        ans += min(L, R);
    }
    /*for (int i = 1; i <= n; ++i) {
        int tmp = abs(i - k);
        for (int j = 1; j <= n; ++j) {
            b[j] = a[j];
        }
        if (k < i) {
            for (int j = k; j < i; ++j) {
                swap(b[j], b[j + 1]);
            }
        } else {
            for (int j = k; j > i; --j) {
                swap(b[j], b[j - 1]);
            }
        }
        if (tmp >= ans) {
            continue;
        }
        for (int j = 1; j < i - 1 && tmp < ans; ++j) {
            for (int l = j + 1; l < i && tmp < ans; ++l) {
                if (b[j] > b[l]) {
                    ++tmp;
                }
            }
        }
        if (tmp >= ans) {
            continue;
        }
        for (int j = i + 1; j < n && tmp < ans; ++j) {
            for (int l = j + 1; l <= n && tmp < ans; ++l) {
                if (b[j] < b[l]) {
                    ++tmp;
                }
            }
        }
        if (tmp < ans) {
            ans = tmp;
        }
    }*/
    printf("%d\n", ans);
}

int main() {
    int test;
    scanf("%d", &test);
    for (int kase = 1; kase <= test; ++kase) {
        printf("Case #%d: ", kase);
        solve();
    }
    return 0;
}
