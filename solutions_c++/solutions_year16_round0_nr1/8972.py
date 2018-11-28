#include <bits/stdc++.h>

using namespace std;

int T , x , ok, i , ans;
bool ap[11];

void aparitii(long long x)
{
    while (x)
    {
        if (!ap[x%10]) ok++;
        ap[x%10] = 1;
        x /= 10;
    }
}

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    scanf("%d", &T);
    for (i = 1; i <= T; ++i)
    {
        scanf("%d", &x);
        if (x == 0)
        {
            printf("Case #%d: INSOMNIA\n", i);
            continue;
        }

        ok = 0;
        for (int j = 0; j < 10; ++j) ap[j] = 0;

        for (ans = 1; ; ++ans)
        {
            aparitii(1LL*x*ans);
            if (ok == 10) break;
        }

        printf("Case #%d: %lld\n", i , 1LL * ans * x);
    }

    return 0;
}
