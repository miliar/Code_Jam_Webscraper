#include <stdio.h>
#include <string.h>

int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        int n;
        scanf("%d", &n);
        printf("Case #%d: ", t);
        if (n == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        long long ans = 0;
        bool z[10];
        int c = 0;
        memset(z, false, sizeof(z));
        while(c < 10)
        {
            ++ans;
            long long now = ans * n;
            while (now > 0)
            {
                if (false == z[now % 10])
                {
                    z[now % 10] = true;
                    ++c;
                }
                now = now / 10;
            }
        }
        printf("%lld\n", ans * n);
    }
    return 0;
}
