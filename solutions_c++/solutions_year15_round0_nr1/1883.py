#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, tcase = 0;
    scanf("%d", &T);
    while (T--) {
        int n;
        scanf("%d", &n);
        int ans = 0, tmp = 0;
        for (int i = 0; i <= n; ++i) {
            int x;
            while (x = getchar(), !isdigit(x));
            x -= '0';
            if (x == 0) continue;
            if (tmp < i) {
                ans += i - tmp;
                tmp = i;
            }
            tmp += x;
        }
        printf("Case #%d: %d\n", ++tcase, ans);
    }
    return 0;
}
