#include <bits/stdc++.h>

using namespace std;

#define FILE_IO

typedef long long LL;

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
        LL K, C, S;
        scanf("%lld%lld%lld", &K, &C, &S);
        printf("Case #%lld: ", test);
        for(LL i = 1; i <= K; i++)
            printf("%lld ", i);
        printf("\n");
    }

    return 0;
}
