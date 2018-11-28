#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
int a, b;
bool IsP(int x)
{
    int pp[10], i, j;
    for(i = 0; x; i ++)
        pp[i] = x % 10, x /= 10;
    for(j = 0, i --; j < i; j ++, i --)
        if(pp[i] != pp[j]) return false;
    return true;
}
int main()
{
    int t, ca, i, j, ans;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    for(scanf("%d", &t), ca = 1; ca <= t; ca ++)
    {
        scanf("%d%d", &a, &b);
        for(i = 1, ans = 0; i <= 1000; i ++)
        {
            if(IsP(i))
            {
                j = i * i;
                ans += j >= a  && j <= b && IsP(j);
            }
        }
        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
