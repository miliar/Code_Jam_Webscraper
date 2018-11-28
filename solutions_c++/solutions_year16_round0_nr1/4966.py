#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
bool v[10];

void solve()
{
    int n;
    scanf("%d", &n);
    if (n == 0)
    {
        puts("INSOMNIA");
        return;
    }
    memset(v, 0, sizeof(v));
    int s = 0;
    int m = n;
    while (1)
    {
        for (int i = m; i; i /= 10)
        {
            if (!v[i % 10])
                ++s;
            v[i % 10] = 1;
        }
        if (s == 10)
        {
            printf("%d\n", m);
            return;
        }
        m += n;
    }
}

int main()
{
    int t;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt)
    {
        printf("Case #%d: ", tt);
        solve();
    }
    return 0;
}