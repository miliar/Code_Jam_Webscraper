#define _CRT_SECURE_NO_WARNINGS
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iterator>
#include <ctime>
#include <iomanip>

using namespace std;

int n;
vector<string> capa;

bool check2(vector<vector<int>> const& edges, int mask, int worker)
{
    if (worker == n)
    {
        assert(mask == (1 << n) - 1);
        return true;
    }

    bool ok = false;
    for (int i = 0; i < edges[worker].size(); ++i)
    {
        if ((mask & (1 << edges[worker][i])) == 0)
        {
            ok = true;
            if (!check2(edges, mask | (1 << edges[worker][i]), worker + 1))
                return false;
        }
    }

    return ok;
}

bool check(int mask)
{
    vector<vector<int>> edges(n);

    for (int worker = 0; worker < n; ++worker)
    {
        for (int mach = 0; mach < n; ++mach)
        {
            if (mask & (1 << (worker * n + mach)))
                edges[worker].push_back(mach);
        }
    }

    sort(edges.begin(), edges.end());
    do
    {
        if (!check2(edges, 0, 0))
            return false;
    } while (next_permutation(edges.begin(), edges.end()));

    return true;
}

int popcount(int a)
{
    int res = 0;
    while (a)
    {
        res += a & 1;
        a >>= 1;
    }

    return res;
}

int main()
{
    int CASES;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        int bMask = 0;
        int idx = 0;
        cin >> n;
        capa.resize(n);
        for (int i = 0; i < n; ++i)
        {
            cin >> capa[i];

            for (int j = 0; j < n; ++j)
            {
                if (capa[i][j] == '1')
                    bMask |= 1 << idx;
                ++idx;
            }
        }

        int res = 999999;
        for (int mask = 1; mask < (1 << (n*n)); ++mask)
        {
            if ((mask & bMask) != bMask)
                continue;

            if (check(mask))
                res = min(res, popcount(mask ^ bMask));
        }

        printf("Case #%d: %d\n", CASE, res);
    }


    return 0;
}
