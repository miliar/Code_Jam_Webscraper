#include <cstdio>
#include <algorithm>
using namespace std;

long long solve(int n, long long p)
{
    if (p == 0)
        return -1;

    p -= 1;
    for (int i = n-1; i >= 0; --i)
    {
        if (!(p&(1LL<<i)))
        {
            long long num = (1LL<<(n-i)) - 1;
            return num - 1;
        }
    }
    return (1LL<<n)-1;
}

int main()
{
    int T;
    scanf("%d", &T);

    for (int Ti = 0; Ti < T; ++Ti)
    {
        int n;
        long long p;
        scanf("%d %lld", &n, &p);

        long long ans_a = solve(n, p);
        long long ans_b = solve(n, (1LL<<n)-p);

        printf("Case #%d: %lld %lld\n", Ti+1, ans_a, (1LL<<n) - (ans_b+1) - 1);
    }
}
