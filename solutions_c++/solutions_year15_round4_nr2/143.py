#include <bits/stdc++.h>
#define DB double
const DB eps=1e-13;
int sgn(DB d)
{
    return d < -eps ? -1 : d > eps;
}
struct PP
{
        DB r, c;
        bool operator < (const PP & cmp) const {
                return sgn(c - cmp.c) < 0;
        }
        void in() {
                scanf("%lf%lf", &r, &c);
        }
}A[200];
DB x, v; int n;
bool check(DB t, DB& mx, DB& mi)
{
        DB tmpv = v; mx = 0, mi = 0;
        for (int i = 0 ; i < n ; ++i){
                if (sgn(t * A[i].r - tmpv) <= 0){
                        mi += t * A[i].r  * A[i].c;
                        tmpv -= A[i].r * t;
                } else{
                        mi += A[i].c *tmpv;
                        tmpv = 0;
                }
        }
        if (sgn(tmpv) > 0) {
                return false;
        }
        tmpv = v; mi = mi / v;
        for (int i = n - 1 ; i >= 0 ; --i){
                if (sgn(A[i].r * t - tmpv) <= 0){
                        mx += t * A[i].r * A[i].c;
                        tmpv -= A[i].r * t;
                } else{
                        mx += A[i].c * tmpv;
                        tmpv = 0;
                }
        }
        mx /= v;
        if (sgn(mx - x) < 0 || sgn(x - mi) < 0){
                return false;
        }
        return true;
}
void in()
{
        freopen("B-large.in", "r", stdin);
        freopen("out.txt", "w",stdout);
}
int main()
{
        in();
        int ca = 1, t;
        scanf("%d", &t);
        while(t--) {
                DB mx = -1, mi = 1e9;
                scanf("%d%lf%lf", &n, &v, &x);
                for(int i = 0; i < n; i++) {
                        A[i].in();
                        if(A[i].c > mx) mx = A[i].c;
                        if(A[i].c< mi) mi = A[i].c;
                }
                printf("Case #%d: ", ca++);
                if(sgn(mx - x) < 0 || sgn(x - mi) < 0) {
                        puts("IMPOSSIBLE");
                        continue;
                }
                std::sort(A, A + n);
                DB l = 0, r = 1e16, best = r;
                int step = 100;
                while(step--) {
                        DB mid = (l + r) * 0.5;
                        if(check(mid, mx, mi)) {
                                if(mid < best) best = mid;
                                r = mid;
                        } else {
                                l = mid;
                        }
                }
                printf("%.15f\n", best);

        }
        return 0;
}
