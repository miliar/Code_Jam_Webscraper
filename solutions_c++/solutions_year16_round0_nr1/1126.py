#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

bool vis[10];
int cnt;

bool cal(int b) {
    while (b) {
        if (vis[b%10] == 0) {
            vis[b%10] = 1;
            cnt++;
        }
        b/=10;
    }
    return cnt == 10;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, n, i, j, ca = 1;
    scanf("%d", &T);
    while (T--) {
        scanf("%d", &n);
        printf("Case #%d: ", ca++);
        if (n == 0) {
            puts("INSOMNIA");
            continue;
        }
        cnt = 0;
        memset(vis, false, sizeof(vis));
        for (i = n;!cal(i);i+=n);
        printf("%d\n", i);
    }
}
