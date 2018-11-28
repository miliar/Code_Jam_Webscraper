#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <iostream>
#define MAXN 10005
using namespace std;
char star[MAXN];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("Aout.out", "w", stdout);
    int t;
    int n;
    int numCase = 1;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        scanf("%s", star);
        int now = star[0] - '0';
        star[0] = '0';
        int ans = 0;
        for(int i = 1; i <= n; i++)
        {
            if(now >= i)
            {
                now += (star[i] - '0');
                star[i] = '0';
            }
            else
            {
                int temp = i - now;
                ans += temp;
                now += temp;
                now += star[i] - '0';
                star[i] = '0';
            }
        }
        printf("Case #%d: %d\n", numCase++, ans);
        memset(star, '\0', sizeof(star));
    }
    return 0;
}
