#include <stdio.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int T, t, i, j, k, n;
int p[1000];
int r[1000], rn, rem, m;

int main() {
    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        scanf("%d", &n);
        for (i = 0; i < n; i++) scanf("%d", &p[i]);
        for (i = 0; i < n; i++) r[i] = i;
        m = 0;
        do {
            for (i = 3; i <= n; i++) {
                for (j = 0; j < i; j++) {
                    if (p[r[j]]-1 == r[(j+1) % i] || p[r[j]]-1 == r[(j-1 + i) % i]) continue;
                    break;
                }
                if (j < i) continue;
                if (m < i) m = i;
            }
        } while (next_permutation(r, r + n));
        printf("%d\n", m);
    }
    return 0;
}
