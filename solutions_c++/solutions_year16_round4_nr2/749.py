#include <bits/stdc++.h>
#define MAXN 210

using namespace std;

int N, K;
double P[MAXN];
double tmpP[MAXN];

double solveSmall() {
    int cnt = 0;
    double ans = 0;
    for (int i = 0; i < (1 << N); ++i) {
        cnt = 0;
        for (int j = 0; j < N; ++j)
            if (i & (1 << j)) {
                tmpP[cnt++] = P[j];
            }
        if (cnt == K) {
            /* for (int i = 0; i < cnt; ++i) {
                printf("%lf\n", tmpP[i]);
                }*/
            double tmpAns = 0;
            for (int j = 0; j < (1 << cnt); ++j) {
                double tmp = 1;
                int cntNow = 0;
                for (int h = 0; h < cnt; ++h)
                    if ((1 << h) & j) {
                        cntNow++;
                        tmp *= tmpP[h];
                    } else tmp *= (1 - tmpP[h]);
                if (cntNow == K / 2) tmpAns += tmp;
            }
            ans = max(ans, tmpAns);
        }
    }
    return ans;
}

int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int T;
    scanf("%d", &T);
    //T = 100;
    for (int ca = 1; ca <= T; ++ca) {
        
        scanf("%d%d", &N, &K);
        for (int i = 0; i < N; ++i) {
            scanf("%lf", &P[i]);
        }
        //    N = 16; K = 8;
        //for (int i = 0; i < N; ++i) P[i] = 0.5;
        printf("Case #%d: %.7lf\n", ca, solveSmall());
       
    }
    return 0;
}