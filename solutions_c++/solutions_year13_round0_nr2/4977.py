#include <algorithm>
#include <cstdio>

int T, N, M, x, y, tab[10000], ctab[10000], maxi, gut;

using std::min;
using std::max;

int main() {
    scanf("%d", &T);
    for (int t = 0; t < T; ++t) {
        scanf("%d %d", &N, &M);
        for (y = 0; y < N; ++y) {
            for (x = 0; x < M; ++x) {
                scanf("%d", tab + y * M + x);
                ctab[y * M + x] = 0;
            }
        }
        for (y = 0; y < N; ++y) {
            maxi = 0;
            for (x = 0; x < M; ++x) {
                maxi = max(maxi, tab[y * M + x]);
            }
            for (x = 0; x < M; ++x) {
                ctab[y * M + x] = maxi;
            }
        }
        for (x = 0; x < M; ++x) {
            maxi = 0;
            for (y = 0; y < N; ++y) {
                maxi = max(maxi, tab[y * M + x]);
            }
            for (y = 0; y < N; ++y) {
                ctab[y * M + x] = min(maxi, ctab[y * M + x]);
            }
        }
        gut = 1;
        for (x = 0; x < N * M; ++x) {
            if (tab[x] != ctab[x]) {
                gut = 0;
                break;
            }
        }
        printf("Case #%d: %s\n", t + 1, gut ? "YES" : "NO");
    }
    return 0;
}
