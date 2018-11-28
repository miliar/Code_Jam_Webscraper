#include <cstdio>
using namespace std;

int T, n;
int f[10];

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);

    scanf("%i", &T);
    for (int t = 1; t <= T; ++ t)
    {
        scanf("%i", &n);
        printf("Case #%d: ", t);

        for (int j = 0; j < 10; ++ j)
            f[j] = 0;

        int iter = 0;
        long long nr = n;
        while (iter < 100000)
        {
            long long tmp = nr;
            while (tmp) f[tmp % 10] = 1, tmp /= 10;

            bool ok = 1;
            for (int j = 0; j < 10; ++ j)
                if (f[j] == 0)
                    ok = 0;
            if (ok) break;
            nr += n;
            iter ++;
        }
        if (iter == 100000) printf("INSOMNIA\n");
        else printf("%lld\n", nr);
    }
}
