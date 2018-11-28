#include <cstdio>
#include <cstdlib>
#include <algorithm>

#define MAXN 1005

int n;
int P[MAXN];
int cal(int key) {
    int res = 0;
    for (int i = 0; i < n; ++i) {
        if (P[i] <= key) continue;
        else {
            res += P[i] / key;
            if (P[i] % key == 0) --res;
        }
    }
    return res + key;
}
int main() {
    int ncas, cnt = 0;
    
    //freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w", stdout);

    scanf("%d", &ncas);
    while (ncas--) {
        int max_P = -1;
        scanf("%d", &n);

        for (int i = 0; i < n; ++i){
            scanf("%d", &P[i]);
            max_P = std::max(max_P, P[i]);
        }

        int ans = max_P;
        for (int i = 1; i <= max_P; ++i) {
            ans = std::min(ans, cal(i));
        }

        printf("Case #%d: %d\n", ++cnt, ans);
    }
    return 0;
}
