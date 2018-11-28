#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int N, J;
long long ans[15];

long long interp(long long x, int k)
{
    long long base(1), ret(0);
    for (int i=0; i<N; i++, base*=k)
        if (x&(1<<i)) ret+=base;
    return ret;
}

int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    int T;
    scanf("%d", &T);
    printf("Case #1:\n");
    scanf("%d%d", &N, &J);
    for (long long x=(1<<(N-1))+1; x<(1<<N) && J; x+=2)
    {
        memset(ans, 0, sizeof ans);
        bool ok(true);
        for (int k=2; k<=10; k++)
        {
            long long v(interp(x, k));
            for (long long p=2; p*p<=v; p++)
                if (v % p == 0)
                {
                    ans[k] = p;
                    break;
                }
            if (! ans[k])
            {
                ok = false;
                break;
            }
        }
        if (ok)
        {
            for (int k=(1<<(N-1)); k; k>>=1)
                putchar((x&k) ? '1' : '0');
            for (int k=2; k<=10; k++)
                printf(" %I64d", ans[k]);
            putchar('\n');
            J--;
        }
    }
    return 0;
}

