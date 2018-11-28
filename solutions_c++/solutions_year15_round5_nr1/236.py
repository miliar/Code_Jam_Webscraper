#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MIN(x,y) ((x)<(y)?(x):(y))
#define MAX(x,y) ((x)>(y)?(x):(y))

int n, d;

int s[1000010];
int m[1000010];

struct ran{
    int hi, lo;
    };

ran r[1000010];

int cl[1000010];
int cu[1000010];

void fillcl(){
    int i, j;
    for(i = 0, j = 0; i<n; i++)
        for(; j <= r[i].lo; j++)
            cl[j] = i;
    for(;j <= 1000000; j++)
        cl[j] = i;
    }

void fillch(){
    int i, j;
    for(i = 0, j = 1000000; i<n; i++)
        for(; j >= r[i].hi; j--)
            cu[j] = i;
    for(;j >= 0; j--)
        cu[j] = i;
    }

void calcr(int k){
    if (r[k].hi >= 0)
        return;
    calcr(m[k]);
    r[k].hi = MAX(s[k], r[m[k]].hi);
    r[k].lo = MIN(s[k], r[m[k]].lo);
    }

int complo(ran *a, ran *b){ return a->lo - b->lo; }
int comphi(ran *a, ran *b){ return b->hi - a->hi; }


int main()
{
    int t0, t;
    scanf("%d", &t);
    for(t0 = 0; t0<t; t0++){
        scanf("%d%d", &n, &d);
        {
            int as, cs, rs;
            scanf("%d%d%d%d", &s[0], &as, &cs, &rs);
            cs %= rs;
            for(int i = 1; i < n; i++)
                s[i] = (s[i-1] * as + cs) % rs;
            }
        {
            int am, cm, rm;
            scanf("%d%d%d%d", &m[0], &am, &cm, &rm);
            cm %= rm;
            for(int i = 1; i < n; i++)
                m[i] = (m[i-1] * am + cm) % rm;
            }
        m[0] = 0;
        for(int i = 1; i < n; i++)
            m[i] %= i;
        memset(r, -1, sizeof r);
        r[0].hi = r[0].lo = s[0];
        for(int i = 1; i < n; i++)
            calcr(i);


        for(int j = 0; j < n;)
            if(r[j].hi - r[j].lo > d){
                r[j] = r[--n];
                }
            else
                j++;


        qsort(r, n, sizeof r[0], (int(*)(const void*,const void*))complo);
        fillcl();
        qsort(r, n, sizeof r[0], (int(*)(const void*,const void*))comphi);
        fillch();
        int ans = 0, x;
        for(int i = 0; i+d <= 1000000; i++){
            x = n - cl[i] - cu[i+d];
            if (ans < x)
                ans = x;
            }


        printf("Case #%d: %d\n", t0 + 1, ans);
        }
    return 0;
}
