#include <cstdio>
#include <cmath>
int main()
{
    freopen("A-small-attempt0.in", "rt", stdin);
    freopen("A.txt", "wt", stdout);
    int Case = 1, T, P, Q;
    scanf("%d", &T);
    while (T--) {
        scanf("%d/%d", &P, &Q);
        printf("Case #%d: ", Case++);
        if (Q%P == 0) {Q/=P; P=1;}

        bool ok = true;
        int q = Q;
        while (q % 2 == 0) q /= 2;
        if (q != 1) printf("impossible\n");
        else {
            int gener = 1;
            int q = Q;
            while (q/2 > P) {q /= 2; ++gener;}

            printf("%d\n", gener);
        }
    }
}
