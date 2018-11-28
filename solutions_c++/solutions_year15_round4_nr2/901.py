#include <bits/stdc++.h>
#define REP(i, x) for(int i = 0; i < (x); i++)
#define FOR(i, x, y) for(int i = (x) i < (y); i++)
#define ER 0.000000000000001
using namespace std;
typedef long long LL;
int n;
long double v, x, r[103], c[103];
int main() {
    int TT; scanf("%d", &TT);
    for(int T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        cin >> n >> v >> x;
        x *= v;
        REP(i, n) {
            cin >> r[i] >> c[i];
            c[i] *= r[i];
            r[i] /= v;
            c[i] /= x;
        }
        if(n == 1) {
            if(abs(c[0] - r[0]) > ER)
                printf("IMPOSSIBLE\n");
            else 
                printf("%.10Lf\n", 1/c[0]);
            continue;
        }
        if(n == 2) {
            long double b1 = (r[0]-c[0])/(r[0]*c[1] - r[1]*c[0]);
            long double b2 = (1 - b1*r[1])/r[0];
//             fprintf(stderr, "                 %Lf           | %Lf    | %Lf, %Lf\n", b2*r[0]+b1*r[1], b2*c[0]+b1*c[1], b1, b2);
            if(abs(c[0] - r[0]) < ER) {
                if(abs(c[1] - r[1]) < ER)
                    printf("%.10Lf\n", 1/(c[0] + c[1]));
                else
                    printf("%.10Lf\n", 1/(c[0]));
                continue;
            }
            if(abs(c[1] - r[1]) < ER) {
                printf("%.10Lf\n", 1/(c[1]));
                continue;
            }
            if(b1 < -ER || b2 < -ER)
                printf("IMPOSSIBLE\n");
            else {
                printf("%.10Lf\n", max(b1, b2));
            }
        }
        else
            printf("\n");
    }
    return 0;
}
