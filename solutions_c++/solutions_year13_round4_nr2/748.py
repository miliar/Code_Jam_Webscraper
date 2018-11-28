#include <iostream>
#include <algorithm>
using namespace std;

typedef long long int64;

int pw;
int64 p, pl;

void readInput()
{
    scanf("%d%lld", &pw, &pl);
    p = (1LL << pw);
}

int64 getCnt(int64 x)
{
    int ans = 0;
    while (x > 0)
    {
        x = (x - 1) / 2;
        ans++;
    }
    return ans;
}

int64 gur(int64 x)
{
    int cnt = getCnt(x);
    int inv = pw - cnt;
    return p - (1LL << inv);
}

int64 bet(int64 x)
{
    int cnt = getCnt(p - 1 - x);
    int inv = pw - cnt;
    return (1LL << inv) - 1;
}

void solve()
{
    int64 l = -1, r = p;
    while (r - l > 1)
    {
        int64 m = (l + r) / 2;
        if (gur(m) < pl)
            l = m;
        else
            r = m;
    }

    printf("%lld ", l);

    l = -1, r = p;
    while (r - l > 1)
    {
        int64 m = (l + r) / 2;
        if (bet(m) < pl)
            l = m;
        else
            r = m;
    }

    printf("%lld", l);
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tstCnt;
    scanf("%d", &tstCnt);

    for (int i = 0; i < tstCnt; i++)
    {
        readInput();
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }

    return 0;
}
