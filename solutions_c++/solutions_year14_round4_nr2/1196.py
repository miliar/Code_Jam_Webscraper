#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <cstring>
using namespace std;

#define N 1005

int n, x[N], y[N], after[N], before[N];
int z[N];

void copy() {
    for (int i = 0; i < n; i++)
        y[i] = x[i];
}

bool check() {
    if (n == 1)
        return true;
    int p = 1;
    while (p < n && y[p] > y[p - 1])
        p++;
    if (p == n)
        return true;
    while (p < n && y[p] < y[p - 1])
        p++;
    return p == n;
}

int solve() {
    if (!check())
        return 0x3f3f3f3f;
    int result = 0;
    for (int i = 0; i < n; i++)
        z[i] = x[i];

    for (int i = 0, j; i < n; i++) {
        for (j = 0; j < n; j++) {
            if (z[j] == y[i])
                break;
        }
        if (j < i) {
            for (int k = j; k + 1 <= i; k++) {
                swap(z[k], z[k + 1]);
                result++;
            }
        } else {
            for (int k = j; k - 1 >= i; k--) {
                swap(z[k], z[k - 1]);
                result++;
            }
        }
    }
    return result;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif

    int cas, ans = 0;
    scanf("%d", &cas);
    for (int _cas = 1; _cas <= cas; _cas++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &x[i]);
        ans = 0x3f3f3f3f;
        copy();
        sort(y, y + n);
        do {
            ans = min(ans, solve());
        } while (next_permutation(y, y + n));
        printf("Case #%d: %d\n", _cas, ans);
    }
    return 0;
}
