#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int K, C, S;

long long findpos(long long x)
{
    long long ret(x);
    for (int i=1; i<C; i++)
        ret = (ret-1) * K + x;
    return ret;
}

int main()
{
    freopen("d.in", "r", stdin);
    freopen("d.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int tt=1; tt<=T; tt++)
    {
        scanf("%d%d%d", &K, &C, &S);
        printf("Case #%d:", tt);
        for (int i=1; i<=K; i++)
            printf(" %I64d", findpos(i));
        putchar('\n');
    }
    return 0;
}

