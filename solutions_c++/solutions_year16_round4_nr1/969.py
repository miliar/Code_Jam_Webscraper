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
vector<int> sol;
vector<int> inv = { 1, 2, 0 };

bool solve(int level, int idx, int winner, vector<int>& prs)
{
    if (level == n)
    {
        sol[idx] = winner;
        if (--prs[winner] == -1)
            return false;

        return true;
    }

    int idx1 = idx;
    int idx2 = idx + (1 << (n - level - 1));

    return solve(level + 1, idx1, winner, prs) && solve(level + 1, idx2, inv[winner], prs);
}

bool cmpV(vector<int> const& v, int start1, int start2, int len)
{
    for (int i = 0; i < len; ++i)
        if (v[start1 + i] > v[start2 + i])
            return true;

    return false;
}

void swapV(vector<int>& v, int start1, int start2, int len)
{
    for (int i = 0; i < len; ++i)
        swap(v[start1 + i], v[start2 + i]);
}

vector<int> _sort(vector<int> v)
{
    for (int level = 1; level < (1 << n); level *= 2)
    {
        for (int idx = 1; idx + level < v.size(); idx += 2 * level)
        {
            if (cmpV(v, idx, idx + level, level))
                swapV(v, idx, idx + level, level);
        }
    }

    return v;
}

int main()
{
    int CASES;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        int r, s, p;
        cin >> n >> r >> p >> s;
        vector<int> res;
        res.clear();
        res.resize((1 << n) + 1, 4);

        bool ok = false;
        for (int i = 0; i < 3; ++i)
        {
            sol.clear();
            sol.resize((1 << n) + 1);
            vector<int> prs = { p, r, s };

            if (solve(0, 1, i, prs))
            {
                vector<int> s = _sort(sol);
                if (res > s)
                    res = s;

                ok = true;
            }
        }

        printf("Case #%d: ", CASE);
        if (!ok)
            printf("IMPOSSIBLE\n");
        else
        {
            for (int i = 1; i <= (1 << n); ++i)
                printf("%c", "PRS"[res[i]]);

            printf("\n");
        }
    }


    return 0;
}
