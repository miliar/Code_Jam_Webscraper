#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

int n, a[10000], b[10000];

void solve() {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &a[i]);
        b[i] = a[i];
    }
    sort(b, b + n);
    int ans = 0;
    int s = 0, t = n - 1;
    for (int p = 0; p < n; ++p) {
        int pos = -1;
        for (int i = s; i <= t; ++i)
            if (a[i] == b[p]) {
                pos = i;
                break;
            }
        assert(pos != -1);
        int left = pos - s, right = t - pos;
        if (left < right) {
            for (int i = pos; i > s; --i) {
                a[i] = a[i - 1];
                ++ans;
            }
            a[s] = b[p];
            ++s;
        } else {
            for (int i = pos; i < t; ++i) {
                a[i] = a[i + 1];
                ++ans;
            }
            a[t] = b[p];
            --t;
        }
    }
    int ss = 0, tt = n - 1;
    while (ss + 1 < n && a[ss] < a[ss + 1])
        ++ss;
    while (tt - 1 >= 0 && a[tt] < a[tt - 1])
        --tt;
    assert(ss == tt);
    printf("%d\n", ans);
}

int main() {
    int numCases;
    scanf("%d", &numCases);
    for (int caseNo = 1; caseNo <= numCases; ++caseNo) {
        printf("Case #%d: ", caseNo);
        solve();
    }
    return 0;
}

