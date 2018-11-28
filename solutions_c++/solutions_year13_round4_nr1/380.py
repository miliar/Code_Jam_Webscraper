#include <algorithm>
#include <cstdio>
#include <map>

using namespace std;

typedef long long LL;
typedef map<int, LL>::iterator MIT;

const int MOD = 1000002013;

map<int, LL> h;

int main() {
	freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cs = 1; cs <= t; ++cs) {
        int n, m, cur = 0;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < m; ++i) {
            int x, y, p;
            scanf("%d%d%d", &x, &y, &p);
            h[x] += p, h[y] -= p;
            (cur += (LL(y - x) * n - LL(y - x) * (y - x - 1) / 2) % MOD * p % MOD) %= MOD;
        }
        int ans = 0;
        LL lst = 0;
        for (MIT it = h.begin(); it != h.end(); ++it)
            lst = it->second += lst;
        while (true) {
            bool f = true;
            for (MIT it = h.begin(); it != h.end(); ++it)
                if (it->second) {
                    f = false;
                    int bg = it->first, ed;
                    LL tmp = it->second;
                    for (MIT it2 = it; it2 != h.end(); ++it2)
                        if (!it2->second) {
                            ed = it2->first;
                            break;
                        }
                        else
                            tmp = min(tmp, it2->second);
                    for (MIT it2 = it; it2 != h.end(); ++it2)
                        if (!it2->second)
                            break;
                        else
                            it2->second -= tmp;
                    tmp %= MOD;
                    (ans += (LL(ed - bg) * n - LL(ed - bg) * (ed - bg - 1) / 2) % MOD * tmp % MOD) %= MOD;
                    break;
                }
            if (f)
                break;
        }
        printf("Case #%d: %d\n", cs, (cur - ans + MOD) % MOD);
        h.clear();
    }
    return 0;
}
