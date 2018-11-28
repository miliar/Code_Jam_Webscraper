#define _N 110

#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

struct Pieroid {
    int st, ed;
    Pieroid() {}
    Pieroid(int st, int ed) : st(st), ed(ed) {}
} pd[_N * _N];

int cnt, n;

int cal(int s, int e) {
    return (e - s + 1) * n - (e - s) * (e - s + 1) / 2;
}

bool cmp(const Pieroid &p1, const Pieroid &p2) {
    if (p1.st == p2.st) return p1.ed < p2.ed;
    return p1.st < p2.st;
}

int main() {
    int cas, m, o, e, p;
    int loss, curLoss;

    freopen("A-small-attempt1.in", "r", stdin);
    freopen("A-small-attempt1.out", "w", stdout);

    scanf("%d", &cas);
    for (int te = 1; te <= cas; ++te) {
        scanf("%d%d", &n, &m);
        loss = cnt = 0;
        for (int i = 0; i < m; ++i) {
            scanf("%d%d%d", &o, &e, &p);
            for (int j = 0; j < p; ++j) {
                pd[cnt++] = Pieroid(o, e);
            }
        }
        sort(pd, pd + cnt, cmp);

        for (int i = 0; i < cnt; ++i) {
            for (int j = 0; j < cnt; ++j) {
                if (pd[i].st <= pd[j].ed && pd[j].st <= pd[i].ed) {
                    int tmp = cal(pd[i].st, pd[i].ed) + cal(pd[j].st, pd[j].ed) - cal(pd[i].st, pd[j].ed) - cal(pd[j].st, pd[i].ed);
                    if (tmp <= 0) continue;
                    loss += tmp;
                    int s1 = pd[i].st, e1 = pd[i].ed, s2 = pd[j].st, e2 = pd[j].ed;
                    pd[i] = Pieroid(s1, e2);
                    pd[j] = Pieroid(s2, e1);
                }
            }
        }

        printf("Case #%d: %d\n", te, loss);
    }

    return 0;
}
