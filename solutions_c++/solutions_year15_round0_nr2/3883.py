#include <stdio.h>
#include <queue>
#include <algorithm>

using namespace std;

const int MAXN = 1100;

int P[MAXN];


int main()
{
    int T;

    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);


    scanf("%d", &T);

    for (int cn = 1; cn <= T; cn++) {
        int D;

        scanf("%d", &D);

        int lim = 0;
        for (int i = 0; i < D; i++) {
            scanf("%d", &P[i]);
            lim = max(lim, P[i]);
        }

        int ans = lim;
        for (int i = 1; i <= lim; i++) {
            int cnt = 0, need = 0;
            for (int j = 0; j < D; j++) {
                if (P[j] > i) {
                    need++;
                    if (P[j] - i > i) {
                        cnt += P[j] - i;
                    }
                }
            }
            if (cnt != 0) {
                need += (cnt - 1) / i;
            }
            ans = min(need + i, ans);

            

        }
        
        printf("Case #%d: %d\n", cn, ans);
        
    }

    return 0;
}
