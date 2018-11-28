#include<cstdio>
#include<cstring>
#include<algorithm>
#include<queue>
using namespace std;

int ans[5000], tans[5000], sum[5000][3], val[5000], cnt[3], tmp[3];
int n, flag, c;
queue<pair<int,int> >Q;

void build(int u, int rt) {
    val[rt] = u;
    if (rt >= (1<<n)) {
        int ro = rt-(1<<n);
        ans[ro] = u;
        for (int i = 0;i < 3;i++) sum[rt][i] = 0;
        sum[rt][u] = 1;
        return;
    }
    build(u, rt<<1);
    build((u+1)%3, rt<<1|1);
    for (int i = 0;i < 3;i++)
        sum[rt][i] = sum[rt<<1][i]+sum[rt<<1|1][i];
}

void print(int rt) {
    if (rt >= (1<<n)) {
        ans[c++] = val[rt];
        return;
    }
    int i;
    for (i = 0;i < 3;i++) {
        if (sum[rt<<1][i] > sum[rt<<1|1][i]) {
            print(rt<<1);
            print(rt<<1|1);
            return;
        }else if (sum[rt<<1|1][i] > sum[rt<<1][i]) {
            print(rt<<1|1);
            print(rt<<1);
            return;
        }
    }
    print(rt<<1);
    print(rt<<1|1);
}

bool bfs(int st) {
    int nst = (1<<n), cnt1 = 0, i;
    while (!Q.empty()) Q.pop();
    Q.push(make_pair(st, 1));
    build(st, 1);
    for (i = 0;i < nst;i++) {
        tmp[ans[i]]++;
    }
    for (i = 0;i < 3;i++) {
        if (tmp[i] != cnt[i]) return false;
    }
    c = 0;
    print(1);
    if (!flag) {
        for (i = 0;i < nst;i++) {
            tans[i] = ans[i];
        }
    }else {
        for (i = 0;i < nst;i++) {
            if (ans[i] < tans[i]) break;
            else if (ans[i] == tans[i]) continue;
            else return true;
        }
        for (i = 0;i < nst;i++) {
            tans[i] = ans[i];
        }
    }
    return true;
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int t, r, p, s, i, j, cas = 1;
    scanf("%d", &t);
    while (t--) {
        scanf("%d%d%d%d", &n, &r, &p, &s);
        cnt[0] = p, cnt[1] = r, cnt[2] = s;
        flag = 0;
        for (i = 0;i < 3;i++) {
            tmp[0] = tmp[1] = tmp[2] = 0;
            if (bfs(i)) flag = 1;
        }
        printf("Case #%d: ", cas++);
        if (!flag) {
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
