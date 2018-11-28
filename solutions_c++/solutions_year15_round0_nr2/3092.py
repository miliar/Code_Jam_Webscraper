#include <stdio.h>
#include <algorithm>
#define NMax 1010

using namespace std;

int Tes;
int N;
int P[NMax];

int main() {

    freopen("in", "r", stdin);
    freopen("out", "w", stdout);

    scanf("%d", &Tes);

    for ( int Case = 1; Case <= Tes; ++ Case ) {

        int MaxP = 0, C;
        int res;

        scanf("%d", &N);
        for ( int i = 1; i <= N; ++ i )
            scanf("%d", &P[i]);

        MaxP = P[1];
        for ( int i = 1; i <= N; ++ i )
            MaxP = max( MaxP, P[i]);

        res = MaxP;

        for ( int i = 1; i <= MaxP; ++ i ) {

            int cost = 0;

            for ( int j = 1; j <= N; ++ j )
                cost += (P[j] - 1) / i;

            res = min(res, cost + i);

        }

        printf("Case #%d: %d\n", Case, res);

    }

    return 0;
}
