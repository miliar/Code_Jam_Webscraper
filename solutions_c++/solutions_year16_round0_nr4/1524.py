#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T, k, c, s;

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int cas = 0;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d%d", &k, &c, &s);
        long long sb = 1;
        for (int i = 1; i < c; i++) sb *= k;
        printf("Case #%d:", ++cas);
        for (long long i = 1; i <= sb * k; i += sb)
            printf(" %lld", i);
        printf("\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
