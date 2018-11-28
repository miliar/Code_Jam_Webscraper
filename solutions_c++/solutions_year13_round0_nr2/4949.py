#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>
#include <ctime>

using namespace std;

typedef long long int64;
typedef long double ldouble;

#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

#define PROBLEM "B"

const int MAXN = 128;

int a[MAXN][MAXN];
int okr[MAXN], okc[MAXN];

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);

        int n, m;
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scanf("%d", &a[i][j]);
            }
        }

        memset(okr, 0, sizeof okr);
        memset(okc, 0, sizeof okc);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (a[i][j] > okr[i]) {
                    okr[i] = a[i][j];
                }
            }
        }

        for (int j = 0; j < m; j++) {
            for (int i = 0; i < n; i++) {
                if (a[i][j] > okc[j]) {
                    okc[j] = a[i][j];
                }
            }
        }

        bool ok = true;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                ok &= (a[i][j] == okr[i]) || (a[i][j] == okc[j]);
            }
        }

        if (ok) printf("YES");
        else printf("NO");

        printf("\n");
    }

    return 0;
}
