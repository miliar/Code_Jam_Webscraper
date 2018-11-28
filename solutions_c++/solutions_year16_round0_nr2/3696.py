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
int const N = 100;
int solve(char const *s)
{
    int ret = 0;
    int n = strlen(s);
    int i = 0, j;
    while (i < n)
    {
        ret += 1;
        for (j = i; j < n && s[j] == s[i]; ++j)
        {
        }
        i = j;
    }
    if (s[n - 1] == '+')
    {
        ret -= 1;
    }
    return ret;
}
int main()
{
    int tc;
    char s[N + 10];
    scanf("%d", &tc);
    for (int cc = 1; cc <= tc; ++cc)
    {
        scanf("%s", s);
        printf("Case #%d: %d\n", cc, solve(s));
    }
    return 0;
}
