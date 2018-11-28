#include <iostream>
#include <cstdio>
#include <vector>
#define For(i, n) for (int i = 0; i < n; i++)
using namespace std;

int main()
{
    int t;
    scanf("%d", &t);

    For (i, t)
    {
        int r, c, w;
        scanf("%d %d %d", &r, &c, &w);
        int tries = (c - w) / (w);
        if (c % w != 0)
            tries += 1;

        tries = max(tries, w < c ? 1 : 0);

        printf("Case #%d: %d\n", i + 1, tries + w + (r - 1) * c / w);
    }
}
