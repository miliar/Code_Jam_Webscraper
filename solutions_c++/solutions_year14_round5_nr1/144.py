#include <stdio.h>
#include <algorithm>
using namespace std;
long long c[1000010], tot;
int n;
bool pd(long long z){
    int num = 0, i;
    long long t = 0;
    for (i = 0; i < n; i++){
        if (t + c[i] > z){
            num++;
            if (num == 3) return false;
            t = c[i];
        }else t += c[i];
    }
    return true;
}
int main(){
    int T, ri = 1, p, q, r, s, i;
    long long l, rr, z;
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d%d%d%d%d", &n, &p, &q, &r, &s);
        tot = 0;
        l = 0;
        for (i = 0; i < n; i++){
            c[i] = (1ll * i * p + q) % r + s;
            tot += c[i];
            l = max(l, c[i]);
        }
        l--; rr = tot;
        while (l + 1 < rr){
            z = (l + rr) >> 1;
            if (pd(z)) rr = z;
            else l = z;
        }
        printf("Case #%d: %.12f\n", ri++, 1.0 - 1.0 * rr / tot);
    }
    return 0;
}
