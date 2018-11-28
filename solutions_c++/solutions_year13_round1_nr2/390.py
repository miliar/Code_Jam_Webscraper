#include <cstdio>
using namespace std;

long long e, r, n;
long long v[11111];

int find(int p1, int p2) {
    long long mx = -1;
    int p = -1;
    for(int i = p1; i < p2; i++) {
        if(mx < v[i]) {
            mx = v[i];
            p = i;
        }
    }
    return p;
}

long long calc(int p1, int p2, long long e1, long long e2) {
    if(p1 >= p2) {
        return 0;
    }
    long long res = 0;
    long long ep1, ep2;
    int p = find(p1, p2);

    ep1 = e1 + r * (p-p1);
    if(ep1 > e) {
        ep1 = e;
    }
    res += calc(p1, p, e1, ep1);

    ep2 = e2 - r * (p2-p);
    if(ep2 < 0) {
        ep2 = 0;
    }
    res += calc(p+1, p2, ep2+r, e2);

    return res + v[p] * (ep1 - ep2);

}

int main(void) {
    int T;
    scanf("%d", &T);
    for(int ti = 1; ti <= T; ti++) {
        printf("Case #%d: ", ti);

        scanf("%I64d %I64d %I64d", &e, &r, &n);
        for(int i = 0; i < n; i++) {
            scanf("%I64d", &v[i]);
        }

        printf("%I64d\n", calc(0, n, e, r));
    }
    return 48-48;
}
