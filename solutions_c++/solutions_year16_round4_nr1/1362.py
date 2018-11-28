#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>
using namespace std;
#define N 14

int ans[1<<N], tans[1<<N];
int cnt[3], tmp[3], n;
int sum[1<<N][3], val[1<<N];

queue<pair<int,int> >Q;
int f;

void build(int u, int d) {
    val[d] = u;
    if (d >= (1<<n)) {
        int ro = d-(1<<n);
        ans[ro] = u;
        for (int i = 0;i < 3;i++) sum[d][i] = 0;
        sum[d][u] = 1;
        return;
    }
    build(u, d<<1);
    build((u+1)%3, d<<1|1);
    for (int i = 0;i < 3;i++) sum[d][i] = sum[d<<1][i]+sum[d<<1|1][i];
}

int c;
void out(int d) {
    if (d >= (1<<n)) {
        ans[c++] = val[d];
        return;
    }
    int i;
    for (i = 0;i < 3;i++) {
        if (sum[d<<1][i] > sum[d<<1|1][i]) {
            out(d<<1);
            out(d<<1|1);
            return;
        }else if (sum[d<<1|1][i] > sum[d<<1][i]) {
            out(d<<1|1);
            out(d<<1);
            return;
        }
    }
    out(d<<1);
    out(d<<1|1);
}

bool bfs(int st) {
    while (!Q.empty()) Q.pop();
    Q.push(make_pair(st, 1));
    int nst = (1<<n);
    int cnt1 = 0;
    build(st, 1);
    for (int i = 0;i < nst;i++) {
        tmp[ans[i]]++;
    }
    for (int i = 0;i < 3;i++) {
        if (tmp[i] != cnt[i]) return false;
    }
    c = 0;
    out(1);
    if (!f) {
        for (int i = 0;i < nst;i++) {
            tans[i] = ans[i];
        }
    }else {
        for (int i = 0;i < nst;i++) {
            if (ans[i] < tans[i]) break;
            else if (ans[i] == tans[i]) continue;
            else return true;
        }
        for (int i = 0;i < nst;i++) {
            tans[i] = ans[i];
        }
    }
    return true;
}

int main() {
    freopen("A-large.in", "r", stdin);
   freopen("1.out", "w", stdout);
    int T, r, p, s, i, j;
    int ca = 1;
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d%d%d", &n, &r, &p, &s);
        cnt[0] = p, cnt[1] = r, cnt[2] = s;
       // printf("%d %d %d\n", cnt[0], cnt[1], cnt[2]);
        f = 0;
        for (i = 0;i < 3;i++) {
            tmp[0] = tmp[1] = tmp[2] = 0;
            if (bfs(i)) f = 1;
        }
        printf("Case #%d: ", ca++);
        if (!f) {
            puts("IMPOSSIBLE");
        }else {
            int st = 1<<n;
            for (i = 0;i < st;i++) {
                if (tans[i] == 0) printf("P");
                else if (tans[i] == 1) printf("R");
                else printf("S");
             }
            puts("");
        }
    }
}
