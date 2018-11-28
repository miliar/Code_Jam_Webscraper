#include <iostream>
#include <cstdio>

using namespace std;

int t, x, r, c;

int conv(int a, int b)
{
    return (a == r && b == c || a == c && b == r);
}

int solve()
{
    if (x == 1)
        return 1;
    if (x == 2)
    {
//        if (conv(1, 2))
//            return 1;
//        if (conv(1, 4))
//            return 1;
//        if (conv(2, 2))
//            return 1;
//        if (conv(2, 3))
//            return 1;
//        if (conv(2, 4))
//            return 1;
//        if (conv(3, 4))
//            return 1;
//        if (conv(4, 4))
//            return 1;
        if ((r*c)%2 != 0)
            return 0;
        return 1;
    }
    if (x == 3)
    {
        if ((r*c)%3 != 0)
            return 0;
        if (r <= 1 || c <= 1)
            return 0;
        return 1;
    }
    if (x == 4)
    {
        if ((r*c)%4 != 0)
            return 0;
        if (r <= 2 || c <= 2)
            return 0;
        return 1;
    }
    cerr << "ERROR";
}

void print(int e, int ind)
{
    if (e == 1)
        printf("Case #%d: GABRIEL\n", ind);
    else
        printf("Case #%d: RICHARD\n", ind);
}

int main()
{
    freopen("omino.in", "r", stdin);
    freopen("omino.out", "w", stdout);

    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        scanf("%d %d %d", &x, &r, &c);
        print(solve(), i);
    }
    return 0;
}
