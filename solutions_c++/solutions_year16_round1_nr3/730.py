#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define N 100000000

bool pri[N] = {0};
int p[N], b[20], size = 0, n, tn;
int ans[60];

bool cal(int bit) {
    long long tm = 0;
    int i;
    for (i = tn-1;i >= 0;i--) {
        tm = tm*bit+b[i];
    }
    int flag = 0;
    for (i = 0;1ll*p[i]*p[i]<=tm;i++) {
        if (tm%p[i] == 0) {
            ans[bit] = p[i];
            flag = 1;
            break;
        }
    }
    return flag;
}

void out() {
    int i;
    for (i = tn-1;i >= 0;i--) printf("%d", b[i]);
    if (n == 32) {
        for (i = tn-1;i >= 0;i--) printf("%d", b[i]);
    }
    for (i = 2;i < 11;i++) printf(" %d", ans[i]);
    puts("");
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T, j, i, ca = 1;
    long long k;
    for (i = 2;i < N;i++) {
        if (pri[i]) continue;
        p[size++] = i;
        for (j = i+i;j < N;j+=i) pri[j] = true;
    }
   // printf("%d\n", size);
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &n, &j);
        long long tm = 1ll;
        tn = n;
        if (n == 32) tn = 16;
        k = 1+(tm<<tn-1);
        int cnt = 0;
        printf("Case #%d:\n", ca++);
        for (k;cnt < j;k++) {
            for (i = 0;i < tn;i++) {
                if (k&(1<<i)) b[i] = 1;
                else b[i] = 0;
            }
            if (!b[0]) continue;
            for (i = 2;i < 11;i++) {
                if (!cal(i)) break;
            }
            if (i == 11) {
                cnt++;
                out();
            }
        }
    }
}
