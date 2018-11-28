#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>
using namespace std;

bool Check(int X, int R, int C)
{
    if (X == 1)
    {
        return true;
    }
    else if (X == 2 && R*C%2 == 0)
    {
        return true;
    }
    else if (X == 3 && R != 1 && C != 1 && R*C%3 == 0)
    {
        return true;
    }
    else if (X == 4 && (R*C == 12 || R*C == 16))
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    freopen ("D-small-attempt1.in","r",stdin);
    freopen ("D-small-attempt1.out","w",stdout);

    int cas, X, R, C;

    scanf("%d", &cas);

    for (int c = 1; c <= cas; ++c)
    {
        scanf("%d%d%d", &X, &R, &C);

        if (Check(X, R, C))
        {
            printf("Case #%d: GABRIEL\n", c);
        }
        else
        {
            printf("Case #%d: RICHARD\n", c);
        }
    }

    return 0;
}
