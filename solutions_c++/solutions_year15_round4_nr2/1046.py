#include <stdio.h>
#include <algorithm>

int t, tn;

int n;
long double v, x;
long double s, e, m;

struct supply
{
    long double r, c;
    bool operator < (const supply &r) const {return c < r.c;}
}in[110];

long double max(long double a, long double b) {return a > b ? a : b;}

bool able(long double t)
{
    int i;
    long double rv, max, min;
    
    rv = v; min = 0;
    for (i = 0; i < n; i++)
    {
        if (in[i].r*t < rv)
        {
            rv -= in[i].r*t;
            min += in[i].r*t/v*in[i].c;
            continue;
        }
        min += rv*in[i].c/v;
        rv = 0;
        break;
    }
    if (rv > 0) return false;
    
    rv = v; max = 0;
    for (i = n-1; i >= 0; i--)
    {
        if (in[i].r*t < rv)
        {
            rv -= in[i].r*t;
            max += in[i].r*t/v*in[i].c;
            continue;
        }
        max += rv*in[i].c/v;
        rv = 0;
        break;
    }
    
    //printf("%.9Lf %.9Lf %.9Lf %.9Lf\n", t, min, x, max);
    return min-(1e-6) <= x && x <= max+(1e-6);
}

int main()
{
    freopen("B-small-attempt4.in", "r", stdin);
    freopen("result.out", "w", stdout);
            
    int i;
    scanf("%d", &t);
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%d %Lf %Lf", &n, &v, &x);
        for (i = 0; i < n; i++) scanf("%Lf %Lf", &in[i].r, &in[i].c);
        std :: sort(in, in+n);
        
        s = 0; e = 1e8+1;
        while (e-s > 0.00000000001)
        {
            m = (s+e)/2;
            if (able(m)) e = m;
            else s = m;
        }
        
        printf("Case #%d: ", tn);
        //if (s > 1e8) puts("IMPOSSIBLE");
        //else printf("%.9Lf\n", s);
        
        //printf("      %d  ", tn);
        if (n == 1 && in[0].c == x) printf("%.9Lf\n", v/in[0].r);
        else if (n == 1) puts("IMPOSSIBLE");
        else if ((x > in[0].c && x > in[1].c) || (x < in[0].c && x < in[1].c)) puts("IMPOSSIBLE");
        else if (in[0].c == in[1].c) printf("%.9Lf\n", v/(in[0].r+in[1].r));
        else printf("%.9Lf\n", max((in[1].c-x)/(in[1].c-in[0].c)*v/in[0].r, (x-in[0].c)/(in[1].c-in[0].c)*v/in[1].r));
    }
}