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
int solve(vector <int> const &coin, int v)
{
    int const MC = 16;
    int used = 0;
    for (vector <int>::const_iterator it = coin.begin();
            it != coin.end(); ++it)
    {
        if (*it <= MC)
        {
            used |= (1 << (*it - 1));
        }
    }
    int ret = INT_MAX;
    for (int mask = 0; mask < (1 << MC); ++mask)
    {
        if ((mask & used) != 0)
        {
            continue;
        }
        vector <int> cur;
        for (int i = 0; i < MC; ++i)
        {
            if (((mask | used) & (1 << i)) != 0)
            {
                cur.push_back(i + 1);
            }
        }
        for (vector <int>::const_iterator it = coin.begin();
                it != coin.end(); ++it)
        {
            if (*it > MC)
            {
                cur.push_back(*it);
            }
        }
        vector <bool> ok(v + 1, false);
        ok[0] = true;
        for (vector <int>::const_iterator it = cur.begin();
                it != cur.end(); ++it)
        {
            for (int i = v - *it; i >= 0; --i)
            {
                if (ok[i])
                {
                    ok[i + *it] = true;
                }
            }
        }
        if (find(ok.begin(), ok.end(), false) == ok.end())
        {
            ret = min(ret, __builtin_popcount(mask));
        }
    }
    return ret;
}
int main()
{
    int tc;
    int c, d, v;
    scanf("%d", &tc);
    for (int cc = 1; cc <= tc; ++cc)
    {
        scanf("%d%d%d", &c, &d ,&v);
        vector <int> coin(d);
        for (int i = 0; i < d; ++i)
        {
            scanf("%d", &coin[i]);
        }
        printf("Case #%d: %d\n", cc, solve(coin, v));
    }
    return 0;
}
