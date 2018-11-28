#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int T, A, N;
int a[10005];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        scanf("%d%d", &A, &N);
        for (int i = 0; i < N; ++i) {
            scanf("%d", &a[i]);
        }
        sort(a, a + N);
        int now = 0;
        int ans = 2100000000;
        if (A == 1) {
            ans = N;
        } else {
            for (int i = 0; now < N; ++i) {
                while (A > a[now]) {
                    A += a[now++];
                    if (now == N) break;
                }
                ans = min(ans, N - now + i);
                A = A * 2 - 1;
            }
        }
        printf("Case #%d: %d\n", test, ans);
    }
    return 0;
}

