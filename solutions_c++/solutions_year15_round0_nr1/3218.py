#include <stdio.h>
#define NMax 1010

int Tes, Smax;
char s[NMax];

int main() {

    freopen("in", "r", stdin);
    freopen("out", "w", stdout);

    scanf("%d", &Tes);

    for ( int Case = 1; Case <= Tes; ++ Case) {

        int sum = 0, res = 0;
        scanf("%d%s", &Smax, s );

        for ( int i = 0; i <= Smax; ++ i ) {
            if ( sum >= i ) {
                sum += s[i] - '0';
            } else if ( s[i] > '0' ) {
                int additional = i - sum;
                res += additional;
                sum += additional + s[i] - '0';
            }
        }

        printf("Case #%d: %d\n", Case, res);

    }

    return 0;
}
