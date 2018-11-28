#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
typedef pair<int, int> ii;

int a[1024], p[1024];
char b[1024];
ii z[1024];

int main() {
    int __;
    scanf("%d", &__);
    forn(_, __) {
        int n;
        scanf("%d", &n);
        forn(i, n) scanf("%d", &a[i]), z[i] = ii(a[i], i);
        sort(z, z + n);
        forn(i, n) p[i] = z[i].second;
        // forn(i, n) printf("  %d %d    %d\n", z[i].first, z[i].second, p[i]);

        memset(b, 0, sizeof b);
        int ans = 0;
        forn(i, n) {
            int ind = p[i];
            int m1 = 0, m2 = 0;
            forn(j, ind) m1 += !b[j];
            for (int j = ind + 1; j < n; j++) m2 += !b[j];
            ans += min(m1, m2);
            b[ind] = true;
            // printf("%d\n", p[i]);
        }

        printf("Case #%d: %d\n", _+1, ans);
    }
    return 0;
}
