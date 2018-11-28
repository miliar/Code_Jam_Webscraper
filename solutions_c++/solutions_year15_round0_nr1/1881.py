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

int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int n, T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        int now(0), ans(0);
        scanf("%d ", &n);
        for (int i = 0; i <= n; ++i) {
            char c;
            scanf("%c", &c);
            int t = c - '0';
            if (now < i) ans += i - now;
            now = t + max(now, i);
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}

