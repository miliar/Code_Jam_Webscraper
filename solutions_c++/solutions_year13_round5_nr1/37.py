#include <stdio.h>
#include <algorithm>
using namespace std;
long long c[40], m;
long long a[40];
int an;
int flag;
double pd(long long z){
    long long cost = 0;
    long long win = 0;
    int num = 0;
    flag = 0;
    an = 0;
    for (int i = 0; i < 37; i++){
        if (c[i] <= z){
            cost += z - c[i];
            num++;
            win += (z - c[i]) * 36;
            a[an++] = (z - c[i]) * 36;
        }
    }
    if (cost > m){
        flag = 1;
        return 0.0;
    }
    if (an == 0){
        flag = -1;
        return 0.0;
    }
    sort(a, a + an);
    double re = 1.0 * win / num - cost;
    for (int i = 0; i < an - 1; i++){
        cost++;
        if (cost > m) break;
        win -= a[i];
        num--;
        re = max(re, 1.0 * win / num - cost);
    }
    return re;
}
int main(){
    long long l, r;
    int i, T, ri = 1, n;
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%I64d%d", &m, &n);
        for (i = 0; i < 40; i++) c[i] = 0;
        for (i = 0; i < n; i++){
            scanf("%I64d", &c[i]);
        }
        double ans = 0;
        l = 0, r = 10000000000000ll;
        if (ri == 4){
          //  for (i = 0; i < 1000; i++) printf("%.8f\n", pd(i));
        }
        while (l + 2 < r){
            long long p = l + (r - l) / 3, q = r - (r - l) / 3;
            double fp = pd(p);
            if (flag == -1){
                l = p;
                continue;
            }
            if (flag == 1){
                r = p;
                continue;
            }
            double fq = pd(q);
            if (flag == -1){
                l = q;
                continue;
            }
            if (flag == 1){
                r = q;
                continue;
            }
            if (fp > fq) r = q;
            else l = p;
        }
        ans = 0;
        ans = max(ans, pd(l));
        ans = max(ans, pd(l + 1));
        ans = max(ans, pd(r - 1));
        ans = max(ans, pd(r));
        printf("Case #%d: %.10f\n", ri++,ans);
    }
    return 0;
}
