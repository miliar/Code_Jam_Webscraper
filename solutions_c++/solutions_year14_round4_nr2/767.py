#include <cstdio>
#include <algorithm>

using namespace std;

const int maxn = 1000 + 10;

int a[maxn], num[maxn], b[maxn];
int n, m, tot;

void Build(int val) {
    tot = 0;
    m = 0;
    for (int i = 0; i <n; i++) {
        if (num[i] < val) continue;
        if (num[i] == val) b[m++] = tot;
        tot++;
    }
}

int Cal_best() {
    int cur = 0;
    for (int i = 0; i < m; i++) {
        cur += b[i] - i;
    }
    int best = cur;
    for (int i = m - 1; i >= 0; i--) {
        cur -= b[i] - i;
        cur += tot - 1 - b[i];
        if (cur < best) best = cur;
    }
    return best;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
            num[i] = a[i];
        }
        sort(a, a + n);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (i > 0 && a[i] == a[i - 1]) continue;
            Build(a[i]);
            ans += Cal_best();
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
