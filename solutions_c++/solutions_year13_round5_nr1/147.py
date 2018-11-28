#include <stdio.h>
#include <string.h>
#include <algorithm>

long long Min(long long a, long long b) {
    return a<b?a:b;
}

void calc(long long val[], long long fil[], double &ans) {
    double res = 0;
    for (int i=0; i<37; i++) res -= fil[i];
    long long min = 1ll<<62, mic = 0, sif = 0;
    for (int i=0; i<37; i++) {
        if (val[i] + fil[i] < min) {
            min = val[i] + fil[i];
            mic = 1;
            sif = fil[i];
        } else if (val[i] + fil[i] == min) mic++, sif += fil[i];
    }
    res += sif * 36.0 / mic;
    if (res > ans) ans = res;
}

int main() {
    int casN;
    scanf("%d", &casN);
    int n;
    long long val[100], fil[100], B;
    for (int casI = 0; casI < casN; casI++) {
        scanf("%lld%d", &B, &n);
        memset (val, 0, sizeof(val));
        memset (fil, 0, sizeof(fil));
        for (int i=0; i<n; i++) scanf("%lld", &val[i]);
        std::sort(val, val+37);
        double ans = 0;
        for (int i=0; i<36; i++) {
            if (val[i] == val[i+1]) continue;
            if (B < i+1) {
                for (int j=i; B>0; j--) {
                    fil[j] ++;
                    B--;
                    calc(val, fil, ans);
                }
                break;
            }
            long long d = Min(B / (i+1), val[i+1] - val[i] - 1);
            if (d > 0) {
                for (int j=0; j<=i; j++) fil[j] += d-1;
                B -= d*(i+1);
                for (int j=i; j>=0; j--) {
                    fil[j]++;
                    calc(val, fil, ans);
                }
            }
            if (B < i+1) {
                i--;
                continue;
            }
            for (int j=i; j>=0; j--) {
                fil[j] ++;
                calc(val, fil, ans);
            }
            B -= i+1;
            
        }

        printf("Case #%d: %.8lf\n", casI+1, ans);
    }
    return 0;
}
