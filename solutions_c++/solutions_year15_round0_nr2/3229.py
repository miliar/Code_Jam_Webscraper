#include <cstdio>
using namespace std;

int p[1000100];

int Solve()
{
    int n, maxp = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &p[i]);
        if (p[i] > maxp) maxp = p[i];
    }

    int ret = 1000100;
    for (int block = 1; block <= maxp; ++block)
    {
        int mm = block;
        for (int i = 0; i < n; ++i)
        {
            mm += p[i] / block;
            if (p[i] % block == 0) mm--;
        }
        if (mm < ret) ret = mm;
    }
    return ret;
}

int main()
{
    freopen("b-large.in", "r", stdin);
    freopen("b-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int cid = 1; cid <= T; ++cid)
    {
        printf("Case #%d: %d\n", cid, Solve());
    }

    fclose(stdout);
    return 0;
}
