#include <iostream>
#include <cstdio>

using namespace std;

bool rec[10], result, f;

bool check(int n)
{
    while (n)
    {
        int t = n % 10;
        result = true;
        rec[t] = true;
        for (int i = 0; i < 10; i++)
        {
            if (!rec[i])
            {
                result = false;
                break;
            }
        }
        if (result)
        {
            return true;
        }
        n /= 10;
    }
}

int main() {
    freopen("/Users/ChaiDuo/Code/Codejam/A/A.in", "r", stdin);
    freopen("/Users/ChaiDuo/Code/Codejam/A/A.out", "w", stdout);

    int ncase, n;

    scanf("%d", &ncase);

    for (int _ = 1; _ <= ncase; _++)
    {
        scanf("%d", &n);
        printf("Case #%d: ", _);
        memset(rec, false, sizeof(rec));
        int p = 0;
        for (int i = 1; i <= int(1e5); i++)
        {
            p += n;
            if (check(p))
            {
                f = true;
                break;
            }
        }
        if (f)
        {
            printf("%d\n", p);
        }
        else
        {
            printf("INSOMNIA\n");
        }
    }

    return 0;
}