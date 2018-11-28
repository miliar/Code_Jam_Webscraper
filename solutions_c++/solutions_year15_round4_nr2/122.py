#include <set>
#include <map>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

#define MaxN 110
#define eps 1e-7

using namespace std;

int T;
int N;
long double V, X, R[MaxN], C[MaxN];

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int i, j, T0 = 0;
    scanf("%d", &T);
    for( ; T; --T) {
        double Ans = 0;
        cin >> N >> V >> X;
        bool Flags = 0, Flagu = 0, Flagv = 0;
        for(i = 1; i <= N; ++i) {
            cin >> R[i] >> C[i];
            if(C[i] > X)
                Flagu = 1;
            if(C[i] < X)
                Flagv = 1;
            if(C[i] == X)
                Flags = 1;
        }
        if((!Flags) && ((!Flagu) || (!Flagv))) {
            printf("Case #%d: IMPOSSIBLE\n", ++T0);
            continue;
        }
        Ans = 0;
        if(Flags) {
            double V1 = 0;
            for(i = 1; i <= N; ++i)
                if(C[i] == X) {
                    V1 += R[i];
                }
            Ans = V / V1;
        }
        else {
            Ans = R[2] * X - R[2] * C[2];
            Ans /= (R[1] * C[1] - R[1] * X);
            double Ans1 = 1;
            if(Ans >= 1.0) {
                Ans1 = 1 / Ans;
                Ans = 1.0;
            }
            double V1 = Ans * R[1] + Ans1 * R[2];
            Ans = V / V1;
        }
        printf("Case #%d: %.7lf\n", ++T0, Ans);
    }
    return 0;
}

