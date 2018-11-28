#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
long long mo = 1000002013LL;
const int MaxN = 30000;

struct node1 {
    int x, y, z;
};
typedef struct node1 node2;
node2 b[MaxN];
node2 a[MaxN];
int fa[MaxN];

bool cmp(node2 x, node2 y) {
    return (x.x < y.x) || (x.x == y.x) && (x.y > y.y);
}
int test, n, m;
long long calc(long long N) {
    return (n * 2LL - N + 1) * (N) / 2;
}

int main() {
    freopen("A@.in", "r", stdin);
    freopen("APP.out", "w", stdout);
    cin >> test;
    for (int tt = 1; tt <= test; tt++) {
        long long ans = 0, ans1 = 0;
        scanf("%d%d", &n, &m);
        for (int i = 1; i <= m; i++) {
            scanf("%d%d%d", &a[i].x, &a[i].y, &a[i].z);
            long long t = calc(a[i].y - a[i].x);//(n * 2 - a[i].y + a[i].x + 1) * (a[i].y - a[i].x) / 2;
            t %= mo;
            t *= a[i].z;
            t %= mo;
            ans += t;
            //cout << ans << endl;
            ans %= mo;
        }
      //  cout << ans << endl;
        //sort(b + 1, b + m * 2 + 1, cmp);
        sort(a + 1, a + m + 1, cmp);
        a[m].x = 1000000000;
        for (int i = 1; i <= m; i++) {
            while (a[i].z > 0) {
                fa[i] = i;
                int l = a[i].y, s = i;
                for (int j = i + 1; j <= m; j++) {
                    if (a[j].z > 0 && a[j + 1].x > l && a[j].x <= l) {
                        l = a[j].y;
                        fa[j] = i;
                        s = j;
                    }
                }
                int w = s, delta = a[i].z;
                while (w != i) {
                    if (a[w].z < delta) delta = a[w].z;
                    w = fa[w];
                }
                long long t = 0;
                w = s;
                while (w != i) {
                    a[w].z -= delta;
                    t += calc(a[fa[w]].y - a[w].x);
                    t %= mo;
                   // cout << "!!" << w << ' ' << fa[w] << endl;
                    w = fa[w];
                }
                //cout << t << endl;
                a[w].z -= delta;
                t += calc(l - a[i].x);
                t %= mo;
                t *= delta;
                t %= mo;
                ans1 += t;
                //cout << a[i].x << ' ' << l << ' ' << ans1 <<endl;
                ans1 %= mo;
            }
        }
        ans -= ans1;
        ans %= mo;
        if (ans < 0) ans += mo;
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}
