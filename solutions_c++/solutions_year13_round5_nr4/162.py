#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <memory>
#include <map>
#include <queue>
#include <vector>
#include <set>
#include <string>

using namespace std;

const int kMaxN = 21;
const double kEps = 1e-10;
char s[kMaxN];
double pr[1 << kMaxN], f[1 << kMaxN];

void solve() {
    int n = strlen(s);
    for (int i = 0; i < (1 << n); ++i) {
        pr[i] = 0.0;
        f[i] = 0.0;
    }
    int s0 = 0;
    for (int i = 0; i < n; ++i)
        if (s[i] == 'X')
            s0 |= 1 << i;
    pr[s0] = 1;
    for (int i = 0; i < (1 << n) - 1; ++i) {
        if (pr[i] < kEps)
            continue;
        for (int j = 0; j < n; ++j) {
            int k = j, cnt = 0;
            while ((i & (1 << k)) != 0) {
                k = (k + 1) % n;
                ++cnt;
            }
            const double tp = pr[i] * 1.0 / n;
            const int s1 = i | (1 << k);
            assert(cnt < n);
            assert(s1 > i);
            pr[s1] += tp;
            f[s1] += (f[i] / pr[i] + (n - cnt)) * tp; 
        }
    }
    assert(fabs(pr[(1 << n) - 1] - 1) < kEps);
    printf("%.15lf", f[(1 << n) - 1]);
}

int main() {
    int numCases;
    scanf("%d", &numCases);
    for (int caseNo = 1; caseNo <= numCases; ++caseNo) {
        scanf("%s", s);
        printf("Case #%d: ", caseNo);
        solve();       
        printf("\n");
    }
    return 0;
}
