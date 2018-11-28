#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

void gao(int x, int cnt[]) {
    if (x == 0) {
        cnt[x] = 1; return ;
    }
    while (x != 0) {
        cnt[x % 10] = 1;
        x /= 10;
    }
    return ;
}

int isok(int cnt[]) {
    for (int i = 0; i < 10; i++) {
        if (!cnt[i]) return false;
    }
    return true;
}
int n;
void work(int cas) {
    scanf("%d", &n);
    int ans = -1;
    int cnt[10] = {};
    int now = n;
    for (int i = 0; i <= 100; i++) {
        gao(now, cnt);
        if (isok(cnt)) {
            ans = now; break;
        }
        now += n;
    }
    printf("Case #%d: ", cas);
    if (ans == -1) {
        printf("INSOMNIA\n");
    }else {
        printf("%d\n", ans);
    }
}


int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        work(cas);
    }
    return 0;
}
