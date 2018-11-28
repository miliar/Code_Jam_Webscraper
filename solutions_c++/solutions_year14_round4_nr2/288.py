#include <cstdio>
#include <algorithm>

#define MAX_N 1005
#define INF 1000000005
using namespace std;

int _T, N, a[MAX_N];
int cMin, cMinP;
int lAns, rAns;

bool used[MAX_N];

int ans;


void reset() {
    cMin = INF;
    lAns = rAns = 0;
    ans = 0;
    for (int i = 0; i < MAX_N-1; i++) {
        used[i] = false;
    }
    return;
}

int main() {
    freopen ("q2.in", "r", stdin);
    freopen ("q2.out", "w", stdout);
    scanf ("%d", &_T);
    for (int _z=1; _z <= _T; _z++) {
        printf ("Case #%d: ", _z);
        scanf ("%d", &N);
        reset();
        for (int i = 0; i < N; i++) {
            scanf ("%d", &a[i]);
        }
        for (int i = 0; i < N; i++) {
            cMin = INF;
            for (int p = 0; p < N; p++) {
                if (!used[p]) {
                    if (a[p] < cMin) {
                        cMin = a[p];
                        cMinP = p;
                    }
                }
            }
            lAns = rAns = 0;
            for (int t = cMinP-1; t >= 0; t--) {
                lAns += !used[t];
            }
            for (int t = cMinP+1; t < N; t++) {
                rAns += !used[t];
            }
            ans += min (lAns, rAns);
            used[cMinP] = true;
        }
        printf ("%d\n", ans);
    }
    return 0;
}
