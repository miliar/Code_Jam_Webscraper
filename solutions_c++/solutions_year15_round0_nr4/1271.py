#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int pancakes[1005];

int check(int n, int x, int y)
{
        if (n > 6 || (x * y) % n != 0) return 0;
        if (x > y) swap(x, y);
        if (n <= 2) return 1;
        if (x == 1) return 0;
        if (n >= 4 && x == 2) return 0;
        if (n == 6 && x == 3) return 0;
        return 1;
}

int main()
{
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);

    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++)
    {
            int n, x, y;
            cin >> n >> x >> y;

            printf("Case #%d: ", cas);
            if (check(n, x, y)) puts("GABRIEL");
            else puts("RICHARD");
    }

    return 0;
}
