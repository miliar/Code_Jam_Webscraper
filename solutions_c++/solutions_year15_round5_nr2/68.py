#include <cstdio>

int m, k;
int s[1024];
int d[1024];

int p[1024], n[1024];

void read() {
    scanf("%d%d", &m, &k);
    for (int i = 1; i <= m - k + 1; i++) {
        scanf("%d", &s[i]);
        if (i > 1) {
            d[i - 1] = s[i] - s[i - 1];
        }
    }
}

void solve() {
    int sum = s[1];
    int ans = 0;

    for (int i = 1; i <= k; i++) {
        p[i] = n[i] = 0;
    }

    for (int i = 1; i <= k; i++) {
        int cur = 0;
        for (int j = i; j <= m - k; j += k) {
            cur += d[j];
            if (cur > p[i]) p[i] = cur;
            if (cur < n[i]) n[i] = cur;
        }

        if (p[i] - n[i] > ans) {
            ans = p[i] - n[i];
        }
    }

    int cnt = 0;
    int ex = 0;

    sum = sum % k;
    for (int i = 1; i <= k; i++) {
        sum = (sum + n[i] % k + k) % k;
        if (p[i] - n[i] == ans) {
            ++ cnt;
        } else {
            ex += ans - (p[i] - n[i]);
        }
    }

    //printf ("%d %d %d\n", sum, k, cnt);

    if (!(sum == 0 || ex >= sum)) 
        ++ ans;

    printf ("%d\n", ans);
    
}

int main() {
    int cases;
    
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++) {
        read();
        printf ("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
