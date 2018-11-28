#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int n;
        scanf("%d", &n);
        if (n == 0)
        {
            printf("Case #%d: INSOMNIA\n", cas);
            continue;
        }
        int x = n, bit = 0, dst = (1 << 10) - 1;
        while(bit < dst)
        {
            int tmp = x;
            while (tmp)
            {
                int cur = tmp % 10;
                tmp /= 10;
                bit |= (1 << cur);
            }
            x += n;
        }
        printf("Case #%d: %d\n", cas, x - n);
    }
    return 0;
}
