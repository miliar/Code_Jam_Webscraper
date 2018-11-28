#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int p[1005], n;

int check(int x) {
    for (int i = x; i >= 1; --i) {
        int K = 0;
        for (int j = 1; j <= n; ++j) {
            K += (p[j] + i - 1) / i - 1;
            if (K + i > x) break;
        }
        //if (x == 1) printf("%d %d %d\n", i, K, p[1]);
        if (K + i <= x) return 1;
        if (K > x) return 0;
    }
    return 0;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, tcase = 0;
    scanf("%d", &T);
    while (T--) {
        int L = 0;
        scanf("%d", &n);
        for (int i = 1; i <= n; ++i) {
            scanf("%d", &p[i]);
            L = max(L, p[i]);
        }
        int head = 0, tail = L;
        while (head < tail - 1) {
            int mid = head + tail >> 1;
            if (check(mid)) tail = mid;
            else head = mid;
        }
        printf("Case #%d: %d\n", ++tcase, tail);
    }
    return 0;
}
