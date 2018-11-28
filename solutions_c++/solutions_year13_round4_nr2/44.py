#include <cstdio>
#include <cstring>

typedef long long ll;

int T, n;
ll N, P;

ll gao1(ll pm) {
    ll ret = 0;
    for (int i = 0; i < n; ++i) {
        if (pm != 0) {
            ret = ret << 1 | 1;
            pm = (pm - 1) / 2;
        } else {
            ret = ret << 1;
        }
    }
    return ret;
}

ll gao2(ll pm) {
    ll ret = 0;
    ll t = N;
    for (int i = 0; i < n; ++i) {
        if (pm != t - 1) {
            ret = ret << 1;
            pm = t / 2 - (t - pm - 2) / 2 - 1;
        } else {
            ret = ret << 1 | 1;
            pm = pm / 2;
        }
        t /= 2;
    }
    return ret;
}

int main() {
    scanf("%d", &T);
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        scanf("%d%lld", &n, &P);
        N = 1LL << n;
        ll r1, r2;
        {
            ll pl = 0, pr = N;
            while (pl + 1 < pr) {
                ll pm = pl + (pr - pl) / 2;
                if (gao1(pm) < P) {
                    pl = pm;
                } else {
                    pr = pm;
                }
            }
            r1 = pl;
        }
        {
            ll pl = 0, pr = N;
            while (pl + 1 < pr) {
                ll pm = pl + (pr - pl) / 2;
                if (gao2(pm) < P) {
                    pl = pm;
                } else {
                    pr = pm;
                }
            }
            r2 = pl;
        }
        printf("Case #%d: %lld %lld\n", caseNum, r1, r2);
    }
    return 0;
}
