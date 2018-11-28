#include <cstdio>
#include <cstring>
#include <algorithm>

int T, n, d[10];
double a[10], b[10];
bool flag[10];

int war() {
    for(int i = 0; i < n; ++i) {
        d[i] = i;
    }
    int ans = 0;
    do {
        int tmp = n;
        memset(flag, 0, sizeof(flag));
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                if(!flag[j] && b[j] > a[d[i]]) {
                    flag[j] = true, tmp--;
                    break;
                }
            }
        }
        ans = std::max(ans, tmp);
    } while(std::next_permutation(d, d + n));
    return ans;
}

int deceitfulWar() {
    int ans = 0;
    for(int i = 0, j = 0; i < n; ++i, ++j) {
        while(j < n && a[j] < b[i]) {
            ++j;
        }
        if(j == n) {
            break;
        }
        ans++;
    }
    return ans;
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    for(int test = 1; test <= T; ++test) {
        scanf("%d", &n);
        for(int i = 0; i < n; ++i) {
            scanf("%lf", &a[i]);
        }
        for(int i = 0; i < n; ++i) {
            scanf("%lf", &b[i]);
        }
        std::sort(a, a + n);
        std::sort(b, b + n);
        printf("Case #%d: %d %d\n", test, deceitfulWar(), war());
    }
    return 0;
}
