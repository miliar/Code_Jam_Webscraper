#include <cstdio>
#include <cstdlib>
#include <cstring>

#define MAXN 1005

int n;
char S[MAXN];
int main() {
    int ncas, cnt = 0;

    //freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);

    scanf("%d", &ncas);
    while (ncas--) {
        scanf("%d%s", &n, S);
        
        int ans = 0, tol = S[0] - '0';

        for (int i = 1; i <= n; ++i) {
            int num = S[i] - '0';
            if (i > tol) {
                ans += i - tol;
                tol = i;
            }
            tol += num;
        }

        printf("Case #%d: %d\n", ++cnt, ans);
    }
    return 0;
}
