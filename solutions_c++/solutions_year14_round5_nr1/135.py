#include <stdio.h>
int cas, n, p, q, r, s, loc;
long long sum[1000010], ans;
inline long long max(long long a, long long b) {
    return a<b?b:a;
}
void tr (int p1, int p2) {
    if (p1 < 0 || p2 > n || p1 > p2) return;
    long long nva = max(max(sum[p1], sum[p2] - sum[p1]), sum[n] - sum[p2]);
    if (nva < ans) ans = nva;
}
int main() {
    scanf("%d", &cas);
    for (int iii=0; iii<cas; iii++) {
        scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
        sum[0] = 0;
        for (int i=0; i<n; i++) {
            sum[i+1] = sum[i] + ((long long)i*p+q)%r+s;
        }
        ans = sum[n];
        loc = 0;
        for (int i=0; i<n; i++) {
            while (sum[loc] - sum[i] < sum[n] - sum[loc]) {
                loc ++;
            }
            tr(i, loc-1);
            tr(i, loc);
        }
        //printf("%lld %lld\n", sum[n], ans);
        printf("Case #%d: %.10f\n", iii+1, (double)(sum[n] - ans) /sum[n]);
    }
    return 0;
}