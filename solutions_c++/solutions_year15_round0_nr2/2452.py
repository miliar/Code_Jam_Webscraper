#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_D = 1000;

int T;
int D;
int P[1 + MAX_D];

int answer;

int main(void) {
    int t;
    int i;

    // citirea datelor
    scanf("%d", &T);
    for (t = 1; t <= T; ++t) {
        scanf("%d ", &D);
        for (i = 0; i < D; ++i) {
            scanf("%d", &P[i]);
        }

        // calcularea solutiei
        int maxP = 0;
        for (i = 0; i < D; ++i) {
            maxP = max(maxP, P[i]);
        }
        int p;
        int special;
        answer = maxP;
        for (p = 1; p < maxP; ++p) {
            special = 0;
            for (i = 0; i < D; ++i) {
                special += P[i] / p;
                if (P[i] % p == 0) {
                    special--;
                }
            }
            if (answer > p + special) {
                answer = p + special;
            }
        }

        // afisarea solutiei
        printf("Case #%d: %d\n", t, answer);
    }
    return 0;
}
