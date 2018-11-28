#include <cstdio>
#include <algorithm>


int a[1000000];
long long b[1000000];

long long getSum(int l, int r) {
    return b[r] - b[l] + a[l];
}

int  main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++ cas) {
        int n, p, q, r, s;
        scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
        long long sum = 0;
        for (int i = 0; i < n; ++ i) {
            a[i] = ((long long) i * p + q) % r + s;
            sum += a[i];
        }
        b[0] = a[0];
        for (int i = 1; i < n; ++ i)
            b[i] = b[i - 1] + a[i];
        long long ans = sum;
        long long suma = 0;
        for (int i = 0; i < n; suma += a[i ++]) {
            int l = i, r = n - 1;
            while (l < r) {
                int mid = (l + r) / 2;
                if (getSum(i, mid) >= suma)
                    r = mid;
                else
                    l = mid + 1;
            }
            long long sumb = getSum(i, l);
            ans = std :: min(ans, std :: max(suma, std :: max(sumb, sum - suma - sumb)));
            l = i, r = n - 1;
            while (l < r) {
                int mid = (l + r) / 2;
                if (getSum(i, mid) * 2 >= sum - suma)
                    r = mid;
                else
                    l = mid + 1;
            }
            sumb = getSum(i, l);
            ans = std :: min(ans, std :: max(suma, std :: max(sumb, sum - suma - sumb)));
            if (l > i) {
                sumb = getSum(i, l - 1);
                ans = std :: min(ans, std :: max(suma, std :: max(sumb, sum - suma - sumb)));
            }
        }
        printf("Case #%d: %.15f\n", cas, 1 - (double) ans / sum);
    }
    return 0;
}
