#include <stdio.h>

int m[10100];
int n;
int rate;
int ans1, ans2;

#define MIN(A,B) ( (A) < (B) ? (A) : (B) )
#define MAX(A,B) ( (A) > (B) ? (A) : (B) )

int main()
{
    int t0, t;
    scanf("%d", &t);
    for(t0 = 0; t0<t; t0++){
        scanf("%d", &n);
        int i, j;
        for(i = 0; i < n; i++){
            scanf("%d", &m[i]);
            }
        rate = 0;
        for(i = 0; i < n - 1; i++){
            if (rate < m[i] - m[i + 1])
                rate = m[i] - m[i + 1];
            }
        ans1 = ans2 = 0;
        for(i = 0; i < n - 1; i++){
            ans1 += MAX(m[i] - m[i + 1], 0);
            ans2 += MIN(m[i], rate);
            }

        printf("Case #%d: %d %d\n", t0 + 1, ans1, ans2);
        }

    return 0;
}
