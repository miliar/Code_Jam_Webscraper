#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

bool judge(int X, int R, int C)
{
    if (X == 1) return true;

    if (X == 2)
    {
        if (R % 2 == 0 || C % 2 == 0) return true;
        return false;
    }
    if (X == 3)
    {
        if (R % 2 == 0 && C == 3) return true;
        if (R == 3 && C % 2 == 0) return true;
        if (R == 3 && C == 3) return true;
        return false;
    }
    if (X == 4)
    {
        if (R == 3 && C == 4) return true;
        if (R == 4 && C == 4) return true;
        if (R == 4 && C == 3) return true;
        return false;
    }
}

void _main()
{
    int X, R, C;
    scanf("%d%d%d", &X, &R, &C);
    if (judge(X, R, C) == true)
        printf("GABRIEL\n");
    else 
        printf("RICHARD\n");
}

int main()
{
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-small.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++)
    {
        printf("Case #%d: ", cases);
        _main();
    }
}