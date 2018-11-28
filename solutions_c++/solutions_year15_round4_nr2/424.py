#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> pii;
#define A first
#define B second

int main() {
    ll t; scanf("%lld", &t);
    for (ll kase=1; kase<=t; kase++) {
        printf("Case #%lld: ", kase);
        ll N;
        scanf("%lld", &N);
        ll V, X;
        pii v, x;
        scanf("%lld.%lld %lld.%lld", &v.A, &v.B, &x.A, &x.B);
        V = v.A*10000 + v.B;
        X = x.A*10000 + x.B;
        if (N == 1) {
            ll R, C;
            pii r, c;
            scanf("%lld.%lld %lld.%lld", &r.A, &r.B, &c.A, &c.B);
            R = r.A*10000 + r.B;
            C = c.A*10000 + c.B;
            if (C == X) {
                printf("%0.8f\n", V/(double)R);
            } else {
                printf("IMPOSSIBLE\n");
            }
        } else if (N == 2) {
            ll R1, C1;
            pii r1, c1;
            scanf("%lld.%lld %lld.%lld", &r1.A, &r1.B, &c1.A, &c1.B);
            R1 = r1.A*10000 + r1.B;
            C1 = c1.A*10000 + c1.B;
            ll R2, C2;
            pii r2, c2;
            scanf("%lld.%lld %lld.%lld", &r2.A, &r2.B, &c2.A, &c2.B);
            R2 = r2.A*10000 + r2.B;
            C2 = c2.A*10000 + c2.B;
            if ((C1 > X && C2 > X) || (C1 < X && C2 < X)) {
                printf("IMPOSSIBLE\n");
            } else {
                if (C1 == X && C2 == X) {
                    printf("%0.8f\n", V/double(R1 + R2));
                } else if (C1 == X) {
                    printf("%0.8f\n", V/double(R1));
                } else if (C2 == X) {
                    printf("%0.8f\n", V/double(R2));
                } else {
                    double frac = (C1 - X) / double(X - C2); // V2 / V1
                    double vvv1 = V / double(1 + frac);
                    double vvv2 = V - vvv1;
                    double t1 = vvv1/R1;
                    double t2 = vvv2/R2;
                    printf("%0.8f\n", max(t1, t2));
                }
            }
        }
    }
    return 0;
}
