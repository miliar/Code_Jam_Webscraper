#include <stdio.h>

struct pnt{
    int x, y;
    };

int n;

pnt p[3100];

#define MIN(A,B) ( (A) < (B) ? (A) : (B) )
#define MAX(A,B) ( (A) > (B) ? (A) : (B) )

int cnt_min(int from, int to)
{
    int i, j, k;
    int cnt_pos = 0, cnt_neg = 0;
    long long dx1 = p[to].x - p[from].x;
    long long dy1 = p[to].y - p[from].y;
    for(i = 0; i < n; i++){
        long long dx2 = p[i].x - p[from].x;
        long long dy2 = p[i].y - p[from].y;
        long long prod = dx1 * dy2 - dy1 * dx2;
        if (prod > 0)
            cnt_pos++;
        if (prod < 0)
            cnt_neg++;
        }
    return MIN(cnt_pos, cnt_neg);
}

int solve()
{
    scanf("%d", &n);
    int i, j, k;
    for(i = 0; i < n; i++)
        scanf("%d%d", &p[i].x, &p[i].y);
    if(n == 1){
        printf("%d\n", 0);
        return 0;
        }

    for(i = 0; i < n; i++){
        int ans = n;
        for(j = 0; j < n; j++)
            if(i != j){
                k = cnt_min(i, j);
                if (ans > k)
                    ans = k;
                }
        printf("%d\n", ans);
        }
    return 0;
}

int main()
{
    int t, t0;
    scanf("%d", &t);
    for(t0 = 0; t0<t; t0++){
        printf("Case #%d:\n", t0 + 1);
        solve();
        }
    return 0;
}
