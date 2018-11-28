#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
using namespace std;
#define SZ(v) ((int)(v).size())
#define SQR(x) ((x) * (x))
#define EPS 1e-9
const int maxint = -1u>>1;
const int maxn = 16 + 1;

int used[maxn];

void tag() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            int x;
            scanf("%d", &x);
            if (i + 1 == n) ++used[x];
        }
    }
}

int main() {
    freopen("a.out", "w", stdout);
    int t, ca = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: ", ++ca);
        memset(used, 0, sizeof(used));
        for (int i = 0; i < 2; ++i) {
            tag();
        }
        int cnt = 0, ans = 0;
        for (int i = 1; i <= 16; ++i) {
            if (used[i] == 2) {
                ++cnt;
                ans = i;
            }
        }
        if (cnt == 0) {
            printf("Volunteer cheated!\n");
        } else if (cnt == 1) {
            printf("%d\n", ans);
        } else {
            printf("Bad magician!\n");
        }
    }
    return 0;
}

