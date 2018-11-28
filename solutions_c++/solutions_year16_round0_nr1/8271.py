#include <cstdio>
#include <cstring>

using namespace std;

int N, T;
bool seen[10];
long long tot;
void _main()
{
    scanf("%d", &N);
    if (N == 0)
    {
        tot = -1;
        return;
    }
    tot = N;
    memset(seen, 0, sizeof seen);
    while (1)
    {
        long long t = tot;
        while (t)
        {
            seen[t % 10] = 1;
            t /= 10;
        }
        bool done = 1;
        for (int i = 0; i < 10; i++)
        {
            if (!seen[i])
                done = 0;
        }
        if (done) break;
        tot += N;
    }
}
int main()
{
    freopen("countingsheepin.txt","r",stdin);
    freopen("countingsheepout.txt","w", stdout);
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++)
    {
        _main();
        if (tot == -1) {
            printf("Case #%d: INSOMNIA\n", i);
        } else
            printf("Case #%d: %lld\n", i, tot);
    }
}