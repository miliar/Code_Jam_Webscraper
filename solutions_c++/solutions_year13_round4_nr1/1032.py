#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define P 1000002013LL

struct Path {
    int a, b, p;
};

int n, m;
Path list[50000];

long long cost(long long a)
{
    long long r;
    if ( a < 0 ) return 0;
    r = (1 + a) * a;
    return (r >> 1);
}

int overlap(Path a, Path b)
{
    if ( a.b < b.a || b.b < a.a) return 0;
    if ( (a.a <= b.a && a.b >= b.b) ||
        (b.a <= a.a && b.b >= a.b)) return 0;
    return 1;
}

int main()
{
    int aa, nn;
    int i, j, k, l, a, b, l1, l2, mm, t;
    long long original, ans, tmp;
    scanf("%d", &nn);
    for (aa = 1; aa <= nn; ++aa) {
        scanf("%d %d", &n, &m);
        original = 0;
        for (i = 0; i < m; i++) {
            scanf("%d %d %d", &list[i].a, &list[i].b, &list[i].p);
            tmp = cost(list[i].b - list[i].a - 1);
            tmp %= P;
            tmp *= list[i].p;
            original += tmp;
            original %= P;
        }
        
        for ( i = 0; i < m; i++ ) {
            if (list[i].p == 0) continue;
            k = i; l = 0; mm = 0;
            for ( j = i+1; j < m; j++ ) {
                if (i == j || list[j].p == 0) continue;
                if (!overlap(list[i], list[j])) continue;
                a = (list[i].a < list[j].a)? list[i].a : list[j].a;
                b = (list[i].b > list[j].b)? list[i].b : list[j].b;
                if (b - a < l) continue;
                t = (list[i].p < list[j].p)? list[i].p : list[j].p;
                if (b - a == l) {
                    if (t > mm) {
                        k = j;
                        mm = t;
                    }
                } else {
                    l = b - a;
                    k = j;
                    mm = t;
                }
            }
            if (k == i) continue;
            list[i].p -= mm;
            list[k].p -= mm;
            a = (list[i].a < list[k].a)? list[i].a : list[k].a;
            b = (list[i].b > list[k].b)? list[i].b : list[k].b;
            list[m].a = a; list[m].b = b; list[m].p = mm;
            m++;
            a = (list[i].a > list[k].a)? list[i].a : list[k].a;
            b = (list[i].b < list[k].b)? list[i].b : list[k].b;
            list[m].a = a; list[m].b = b; list[m].p = mm;
            m++;
            i--;
        }

        // ans
        ans = 0;
        for ( i = 0; i < m; i++ ) {
            if (list[i].p == 0) continue;
            tmp = cost(list[i].b - list[i].a - 1);
            tmp %= P;
            tmp *= list[i].p;
            ans += tmp;
            ans %= P;
        }
        ans -= original;
        if (ans < 0) ans += P;
        printf("Case #%d: %lld\n", aa, ans);
    }
    return 0;
}

