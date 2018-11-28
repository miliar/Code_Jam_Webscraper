#include<stdio.h>

int min(int a, int b) { return a < b? a : b; }

int solve(int mye, int e, int r, int n, int v[], int i)
{
    int k, p, max, rem;

    if(i >= n) return 0;
    max = 0;
    for(k = 0; k <= mye; k++) {
        rem = min(e, mye-k+r);
        p = k*v[i] + solve( rem, e, r, n, v, i+1 );
        if(p > max) max = p;
    }
    return max;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out_B.txt", "w", stdout);
    int t, e, r, n, v[10], x, y, i;
    scanf("%d", &t);
    for(x = 1; x <= t; x++) {
        scanf("%d %d %d", &e, &r, &n);
        for(i = 0; i < n; i++) {
            scanf("%d", &v[i]);
        }
        y = solve(e, e, r, n, v, 0);
        printf("Case #%d: %d\n", x, y);
    }
    return 0;
}
