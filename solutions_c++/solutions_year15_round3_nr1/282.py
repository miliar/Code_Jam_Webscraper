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
int solve(int nr, int nc, int w)
{
    int r0 = INT_MAX;
    int r1 = INT_MAX;
    vector <int> num_l(nc + 1);
    vector <int> s(nc + 1);
    for (int mask = 0; mask < (1 << nc); ++mask)
    {
        fill(num_l.begin(), num_l.end(), 0);
        int i = 0, j;
        while (i < nc)
        {
            for (j = i; j < nc && (mask & (1 << j)) == 0; ++j)
            {
            }
            ++num_l[j - i];
            i = j + 1;
        }
        if (accumulate(num_l.begin() + w, num_l.end(), 0) == 0)
        {
            r0 = min(r0, __builtin_popcount(mask));
        }
        if (num_l[w] == 1 &&
                accumulate(num_l.begin() + (w + 1), num_l.end(), 0) == 0)
        {
            r1 = min(r1, __builtin_popcount(mask) + w);
        }
    }
    return r1 + (nr - 1) * r0;
}
int main()
{
    int tc, cc;
    int nr, nc, w;
    scanf("%d", &tc);
    for (cc = 1; cc <= tc; ++cc)
    {
        scanf("%d%d%d", &nr, &nc, &w);
        printf("Case #%d: %d\n", cc, solve(nr, nc, w));
    }
    return 0;
}
