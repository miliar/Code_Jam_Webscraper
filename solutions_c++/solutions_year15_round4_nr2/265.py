#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define EPS 1e-10
#define EQ(X,Y) ( fabs( (X) - (Y) ) < EPS )

struct wat {double r, c;};


int comp(const wat *a, const wat *b){
    return (a->c - b->c)*10000000.0;
    }

wat w[110];

wat cumul(int from, int to){
    wat res;
    res.r = res.c = 0.0;
    for(int i = from; i <= to; i++){
        res.r += w[i].r;
        res.c += w[i].r * w[i].c;
        }
    res.c /= res.r;
    return res;
    }

double v, x;
int n;

int main()
{
    int t0, t;
    scanf("%d", &t);
    for(t0 = 0; t0<t; t0++){
        scanf("%d%lf%lf", &n, &v, &x);
        for(int i = 0; i < n; i++){
            scanf("%lf%lf", &w[i].r, &w[i].c);
            }
        qsort(w, n, sizeof w[0], (int(*)(const void*, const void*))comp);
        wat res = cumul(0, n-1);

        if(EQ(res.c, x)){
            printf("Case #%d: %0.9lf\n", t0 + 1, v / res.r);
            continue;
            }

        if(res.c < x){
            int from;
            for (from = 1; from < n && (res = cumul(from, n-1)).c < x - EPS; from++){
            }
            if(from == n){
                printf("Case #%d: IMPOSSIBLE\n", t0 + 1);
                continue;
                }
            from--;
            double r0 = res.r * (x - res.c) / (w[from].c - x);
            if(r0 < -EPS || r0 > w[from].r + EPS)
                return -1;
            w[from].r = r0;
            res = cumul(from, n-1);
            }
        else{
            int to;
            for (to = n-2; to >= 0 && (res = cumul(0, to)).c > x + EPS; to--){
            }
            if(to < 0){
                printf("Case #%d: IMPOSSIBLE\n", t0 + 1);
                continue;
                }
            to++;
            double r0 = res.r * (x - res.c) / (w[to].c - x);
            if(r0 < -EPS || r0 > w[to].r + EPS)
                return -1;
            w[to].r = r0;
            res = cumul(0, to);
            }


        printf("Case #%d: %0.9lf\n", t0 + 1, v / res.r);
        }

    return 0;
}
