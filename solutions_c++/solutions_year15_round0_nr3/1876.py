#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
const int MAXN = 10005;
int ma[5][5], l, n, a[MAXN];
char str[MAXN];
int main() {
    int T;
    scanf("%d", &T);
    ma[1][1] = 1; ma[1][2] =  2; ma[1][3] =  3; ma[1][4] =  4;
    ma[2][1] = 2; ma[2][2] = -1; ma[2][3] =  4; ma[2][4] = -3;
    ma[3][1] = 3; ma[3][2] = -4; ma[3][3] = -1; ma[3][4] =  2;
    ma[4][1] = 4; ma[4][2] =  3; ma[4][3] = -2; ma[4][4] = -1;
    for (int ca = 1; ca <= T; ++ca) {
        bool fi(0), fj(0), fk(0);
        scanf("%d%d\n", &l, &n);
        scanf("%s", str);
        for (int i = 0; i < l; ++i) {
            if (str[i] == 'i') a[i] = 2;
            if (str[i] == 'j') a[i] = 3;
            if (str[i] == 'k') a[i] = 4;
        }
        int now(1);
        for (int i = 0; i < l * n; ++i) {
            int t = i % l, y;
            if (now > 0) y = 1; else y = -1;
            now = y * ma[abs(now)][a[t]];
            if (now == 2) fi = 1;
            if (fi == 1 && now == 4) fj = 1;
            if (i == l * n - 1 && now == -1) fk = 1;
        }
        printf("Case #%d: ", ca);
        if (fk && fj) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}

