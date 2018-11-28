#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
using namespace std;

const int Maxn = 105;
int n, m;
bool valid(int x)
{
    vector<int> vec;
    while(x)
    {
        vec.push_back(x % 10);
        x /= 10;
    }
    int size = vec.size();
    for (int i = 0; i < size / 2; ++i)
    {
        if (vec[i] != vec[size - 1 - i]) return false;
    }
    return true;
}
int solve()
{
    int fac = 1;
    int ret = 0;
    for (fac = 1; fac * fac < n; ++fac);
    for (; fac * fac <= m; ++fac)
    {
        if (valid(fac) && valid(fac * fac)) ret++;
    }
    return ret;
}

int main()
{
   // freopen("in.txt", "r", stdin);
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);
   // freopen("large.in", "r", stdin);
   // freopen("large.out", "w", stdout);
    int T;scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d: ", cas);
        scanf ("%d%d", &n, &m);
        printf("%d\n", solve());
    }


    return 0;
}
