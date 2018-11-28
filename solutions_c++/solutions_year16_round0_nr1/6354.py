#include <cstdio>
#include <iostream>
#include <cstring>
#define MAX 1000000+1
#define ll long long
using namespace std;
bool vis[10];

bool check(ll n) {
    while (n != 0) {
        int t = n % 10;
        vis[t] = true;
        n /= 10;
    }
    int cnt = 0;
    for (int i = 0; i <= 9; i++) {
        if (vis[i]) {
            cnt++;
        }
    }
    if (cnt == 10) return true;
    return false;
}
int main() {
    int T;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);

    for (int kase = 1; kase <= T; kase++) {
        printf("Case #%d: ", kase);
        memset(vis, 0, sizeof(vis));

        int inc;
        scanf("%d", &inc);
        ll t = 0;
        bool f = false;
        int i;

        for (i = 1; i <= MAX; i++) {
            t += inc;
            if (check(t)) {
                f = true;
                break;
            }
        }

        if (f) printf("%I64d\n", t);
        else {
            printf("INSOMNIA\n");
        }
    }

    return 0;
}
