#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int MAXN = 10000+5;
int T, N, X, S[MAXN];
int main() {
    freopen("A-large (1).in", "r", stdin);
    freopen("b.txt", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d", &N, &X);
        for (int i = 1; i <= N; i++) {
            scanf("%d", &S[i]);
        }
        sort(S+1, S+1+N);
        int ans = 0, p = 1;
        for (int i = N; i >= 1 && p <= i; i--) {
            if (p < i && S[i]+S[p] <= X)
                p++;
            ans++;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
