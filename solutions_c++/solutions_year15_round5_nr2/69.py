#include <cstdio>
#include <algorithm>
#include <cassert>
using namespace std;
long long floor(long long a, int b) {
    if (a < 0) return -((abs(a) + b - 1) / b);
    else return a / b;
}
long long ceil(long long a, int b) {
    if (a < 0) return -(abs(a) / b);
    else return (a + b - 1) / b;
    // return (a < 0 ? -1 : 1) * ((abs(a)+b-1) / b);
}
int main() {
    int T;
    scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        int n, k;
        scanf("%d%d", &n,&k);
        int sum[n-k+1], mindiff[k], maxdiff[k], minres = 0, diff[n];
        for (int i=0; i<k; i++) mindiff[i] = maxdiff[i] = 0;
        for (int i=0; i<=n-k; i++) scanf("%d", &sum[i]);
        for (int i=1; i<=n-k; i++) {
            int x = (i-1)%k;
            diff[i-1] = sum[i] - sum[i-1] + (i > k ? diff[i-1-k] : 0);
            mindiff[x] = min(mindiff[x], diff[i-1]);
            maxdiff[x] = max(maxdiff[x], diff[i-1]);
            minres = max(minres, maxdiff[x] - mindiff[x]);
        }
        int pos[k];
        for (int i=0; i<k; i++) pos[i] = 0;
        pos[0] = sum[0];
        int res = minres;
        long long A = 0, B = 0;
        for (int i=0; i<k; i++) {
            A += mindiff[i];
            B += maxdiff[i];
        }
        long long L = floor(sum[0] + A, k);
        long long H = max(ceil(sum[0] + B, k), L + minres);
        printf("Case #%d: %lld\n", t, H-L);
    }
    return 0;
}
