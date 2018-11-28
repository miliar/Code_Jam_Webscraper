#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
const int MAXN = 1005;
int main() {
    //freopen("b.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int T, n, a[MAXN];
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d", &n);
        int ma(0);
        for (int i = 0; i < n; ++i) {
            scanf("%d", a + i);
            ma = max(ma, a[i]);
        }
        int res(MAXN);
        for (int i = 1; i <= ma; ++i) {
            int ans(0);
            for (int j = 0; j < n; ++j) {
                ans += a[j] / i;
                if (a[j] % i == 0) ans--;
            }
            res = min(res, ans + i);
        }
        printf("Case #%d: %d\n", ca, res);
    }
    return 0;
}

