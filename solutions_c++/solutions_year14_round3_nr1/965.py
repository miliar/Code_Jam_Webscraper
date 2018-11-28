#include <cstdio>
#include <algorithm>

using namespace std;

int main(void)
{
    int t, i, tc=0;
    long long p, q, g;
    bool valid;
    for (scanf("%d", &t);t--;)
    {
        scanf("%lld/%lld", &p, &q);
        g=__gcd(p, q);
        p/=g;
        q/=g;
        printf("Case #%d: ", ++tc);
        if (q&(q-1))
            printf("impossible\n");
        else
        {
            valid=0;
            for (i=1;i<=40 && !valid;i++)
            {
                q>>=1;
                if (p>=q)
                {
                    valid=1;
                    printf("%d\n", i);
                }
            }
            if (!valid)
                printf("impossible\n");
        }
    }
    return 0;
}
