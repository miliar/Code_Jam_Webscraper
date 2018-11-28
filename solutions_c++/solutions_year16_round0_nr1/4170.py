#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

typedef long long LL;

LL solve(LL N)
{
    int f[15] = {0};
    int rem = 10;
    for(LL i = 1; i <= 100; i++)
    {
        int aux = N * i;
        while(aux)
        {
            f[aux % 10]++;
            if(f[aux % 10] == 1)    rem--;
            aux /= 10;
        }
        if(!rem)
            return (N * i);
    }
    return -1;
}

int main()
{
    #ifdef FILE_IO
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    #endif

    LL T;
    scanf("%lld", &T);
    for(LL test = 1; test <= T; test++)
    {
        LL N;
        scanf("%lld", &N);
        LL ans = solve(N);
        printf("Case #%lld: ", test);
        if(ans == -1)
            printf("INSOMNIA\n");
        else
            printf("%lld\n", ans);
    }

    return 0;
}
