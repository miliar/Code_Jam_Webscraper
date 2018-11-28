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
int const N = 10000;
int n, x;
int s[N];
void readin()
{
    scanf("%d%d", &n, &x);
    for (int i = 0; i < n; ++i)
    {
        scanf("%d", &s[i]);
    }
}
int solve()
{
    int ret = 0;
    multiset <int> m(s, s + n);
    while (!m.empty())
    {
        ++ret;
        int cur_max = *(m.rbegin());
        m.erase(m.lower_bound(cur_max));
        multiset <int>::iterator it = m.lower_bound(x - cur_max + 1);
        if (it != m.begin())
        {
            --it;
            m.erase(it);
        }
    }
    return ret;
}
int main()
{
    int tc;
    scanf("%d", &tc);
    for (int cc = 1; cc <= tc; ++cc)
    {
        readin();
        printf("Case #%d: %d\n", cc, solve());
    }
    return 0;
}
