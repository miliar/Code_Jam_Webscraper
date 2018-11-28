#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

const long long MaxSize = 1000000;
long long S[MaxSize + 100];

long long Reverse(long long N)
{
    long long ret = 0;
    while (N > 0)
    {
        ret = (ret * 10) + (N % 10);
        N /= 10;
    }
    return ret;
}

void PreProcess()
{
    memset(S, 0, sizeof(S));
    S[1] = 1;
    for (long long N = 1; N <= MaxSize; ++N)
    {
        long long M = N + 1;
        if (M <= MaxSize && (S[M] == 0 || S[M] > S[N] + 1))
        {
            S[M] = S[N] + 1;
        }
        M = Reverse(N);
        if (M <= MaxSize && (S[M] == 0 || S[M] > S[N] + 1))
        {
            S[M] = S[N] + 1;
        }
    }
}

int main()
{
    freopen("a-small.in", "r", stdin);
    freopen("a-small.out", "w", stdout);

    PreProcess();

    int T;
    scanf("%d", &T);
    for (int cid = 1; cid <= T; ++cid)
    {
        long long N;
        scanf("%lld", &N);
        printf("Case #%d: %lld\n", cid, S[N]);
    }

    fclose(stdout);
    return 0;
}
