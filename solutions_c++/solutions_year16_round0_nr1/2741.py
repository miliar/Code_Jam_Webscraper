#pragma warning(disable:4996)

#include <stdio.h>

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int t,tt=0;
    scanf("%d", &t);
    while(t--) {
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", ++tt);
        if (n==0) printf("INSOMNIA\n");
        else
        {
            int d=0;
            for (int i=0; ; i++)
            {
                long long m = (long long)n * i;
                int digits=0;
                while (m) 
                {
                    digits |= 1 << (m%10);
                    m /= 10;
                }
                d |= digits;
                if (d == (1<<10)-1)
                {
                    printf("%lld\n", (long long)n*i);
                    break;
                }
            }
        }
    }

    return 0;
}
