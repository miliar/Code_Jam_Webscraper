#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

int s[10010];

int main() {
    int t, n, x;
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &t);
    for (int ca = 1; ca <= t; ca ++ ) {
        scanf("%d%d", &n, &x);
        for (int i = 0; i < n; i ++ )
            scanf("%d", &s[i]);
        sort(s, s + n);
        int en = 0, cnt = 0;
        for (int i = n - 1; i >= en; i -- ) {
            if (s[i] + s[en] <= x) {
                en ++ ;
            }
            cnt ++ ;
        }
        printf("Case #%d: %d\n", ca, cnt);
    }
    return 0;
}
