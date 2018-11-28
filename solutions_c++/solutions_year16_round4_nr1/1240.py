#include <stdio.h>

int t, n;
int abs(int a) {return a > 0 ? a : -a;}

void rps(int r, int p, int s)
{
    if (r+p+s == 2)
    {
        if (p) printf("P");
        if (r) printf("R");
        if (s) printf("S");
        return;
    }
    if (r == p)
    {
        rps(r/2, p/2+1, s/2);
        rps(r/2+1, p/2, s/2);
    }
    if (p == s)
    {
        rps(r/2, p/2+1, s/2);
        rps(r/2, p/2, s/2+1);
    }
    if (s == r)
    {
        rps(r/2+1, p/2, s/2);
        rps(r/2, p/2, s/2+1);
    }
}

int main()
{
    freopen("/Users/IohcEjnim/Downloads/A-large.in.txt", "r", stdin);
    freopen("/Users/IohcEjnim/Downloads/result.txt", "w", stdout);
    int tn, r, p, s;
    scanf("%d", &t);
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%d %d %d %d", &n, &r, &p, &s);
        printf("Case #%d: ", tn);
        if (abs(r-p) > 1 || abs(p-s) > 1 || abs(s-r) > 1)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        rps(r, p, s);
        puts("");
    }
}