#include <bits/stdc++.h>
using namespace std;

long long b[1010];
struct node {
    long long minn, maxx;
} a[1010];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n, k;
        scanf("%d%d", &n, &k);
        for(int i = 1; i <= n - k + 1; i++)
            scanf("%I64d", &b[i]);
        for(int i = 1; i <= k; i++) {
            a[i].minn = 0;
            a[i].maxx = 0;
            long long now = 0;
            for(int j = i + k; j <= n; j += k) {
                now = now + b[j - k + 1] - b[j - k];
                a[i].minn = min(a[i].minn, now);
                a[i].maxx = max(a[i].maxx, now);
            }
        }
        long long ans = 1e15;
        for(int i = 1; i <= k; i++) {
            long long valR = a[i].maxx;
            long long sumF = 0, sumC = 0;
            for(int j = 1; j <= k; j++) {
                valR = max(valR, a[j].maxx + a[i].minn - a[j].minn);
                sumF = sumF + a[i].minn - a[j].minn;
            }
            for(int j = 1; j <= k; j++)
                sumC = sumC + valR - (a[j].maxx + a[i].minn - a[j].minn);
            long long cha = ((b[1] - sumF) % k + k) % k;
            if(sumC >= cha)
                ans = min(ans, valR - a[i].minn);
            else
                ans = min(ans, valR - a[i].minn + 1);
        }
        printf("Case #%d: %I64d\n", cas, ans);
        fprintf(stderr, "%d: %I64d\n", cas, ans);
    }
    return 0;
}