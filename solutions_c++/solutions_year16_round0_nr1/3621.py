#include <cassert>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <cstddef>
#include <cctype>
#include <cmath>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <numeric>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <list>
#include <string>
#include <functional>
#include <utility>
using namespace std;
typedef long long llint;
int f(int x)
{
    int ret = 0;
    while (x != 0)
    {
        ret |= 1 << (x % 10);
        x /= 10;
    }
    return ret;
}
int gao(int x)
{
    int mask = 0;
    for (int i = 1; i <= 1000; ++i)
    {
        mask |= f(i * x);
        if (__builtin_popcount(mask) == 10)
        {
            return i * x;
        }
    }
    return -1;
}
int main()
{
    int tc;
    int x;
    scanf("%d", &tc);
    for (int cc = 1; cc <= tc; ++cc)
    {
        scanf("%d", &x);
        if (x != 0)
        {
            printf("Case #%d: %d\n", cc, gao(x));
        }
        else
        {
            printf("Case #%d: INSOMNIA\n", cc);
        }
    }
    return 0;
}
