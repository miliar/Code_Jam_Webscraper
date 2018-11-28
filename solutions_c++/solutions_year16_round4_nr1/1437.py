#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int t, n, r[3], ans[5555][5555];

char get(int x) {
    if (x == 0) return 'R';
    if (x == 2) return 'S';
    return 'P';
}

int sb(int x) {
    if (x == 0) return 2;
    if (x == 1) return 0;
    return 1;
}

void build(int x) {
    ans[n][0] = x;
    int cnt = 1;
    for (int i = n; i >= 1; i--){
        for (int j = 0; j < cnt; j++) {
            ans[i - 1][j * 2] = ans[i][j];
            ans[i - 1][j * 2 + 1] = sb(ans[i][j]);
        }
        cnt *= 2;
    }
   // for (int i = 0; i < (1<<n); i++) printf("%d", ans[0][i]);
  //  printf("\n");
}

bool judge(){
    int tmp[3];
    memset(tmp, 0, sizeof(tmp));
    for (int i = 0; i < (1<<n); i++) {
        tmp[ans[0][i]]++;
    //    printf("%c", get(ans[0][i]));
    }//
   // printf("\n");
    for (int i = 0; i < 3; i++) if (r[i] != tmp[i]) return false;
    return true;
}

bool big(int l1, int r1, int l2, int r2) {
    while (l1 <= r1 && l2 <= r2) {
        if (ans[0][l1] != ans[0][l2]) return get(ans[0][l1]) > get(ans[0][l2]);
        l1++; l2++;
    }
    return 0;
}

void gao(int l, int r) {
    if (l >= r) return;
    int mid = (l + r)>>1;
    gao(l, mid);
    gao(mid + 1, r);
    //printf("%d %d %d\n", l, r, big(l, mid, mid + 1, r));
    if (big(l, mid, mid + 1, r)) {
        int sb = mid + 1;
        for (int i = l; i <= mid; i++) {
            swap(ans[0][i], ans[0][sb]);
            sb++;
        }
    }
}

char cao[3][5555];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int cas = 0;
    scanf("%d", &t);
    while (t--) {
        int tot = 0;
        scanf("%d", &n);
        int flag = 0;
        for (int i = 0; i < 3; i++) scanf("%d", &r[i]);
        for (int i = 0; i < 3; i++) {
            build(i);
            if (judge()) {
                flag = 1;
                gao(0, (1<<n) - 1);
                for (int i = 0; i < (1<<n); i++) {
                    cao[tot][i] = get(ans[0][i]);
                }
                cao[tot][(1<<n)] = 0;
                tot++;
            }
        }
        printf("Case #%d: ", ++cas);
        if (!flag) printf("IMPOSSIBLE\n");
        else {
            int vv = 0;
            for (int i = 1; i < tot; i++) {
                if (strcmp(cao[vv], cao[i]) > 0) vv = i;
            }
            printf("%s\n", cao[vv]);
        }

    }
    return 0;
}
