#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T, vis[15];
long long n;

void get(long long x) {
    while (x) {
        vis[x % 10] = 1;
        x /= 10;
    }
}

bool judge() {
    for (int i = 0; i <= 9; i++)
        if (!vis[i]) return false;
    return true;
}

long long solve() {
    memset(vis, 0, sizeof(vis));
    long long cnt = 1;
    while (1) {
        get(n * cnt);
        if (judge()) return cnt;
        cnt++;
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%lld", &n);
        printf("Case #%d: ", cas);
        if (n == 0) printf("INSOMNIA\n");
       // n = cas;
        else printf("%lld\n", n * solve());
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
