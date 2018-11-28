#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;

typedef long long li;

int n, m;

bool get(li mask, int x, int y)
{
    return mask & (1 << (x * m + y));
}

void put(li& mask, int x, int y)
{
    mask = mask | (1 << (x * m + y));
}

int cnt(li mask, int x, int y)
{
    if (get(mask, x, y))
        return -1;
    int cnt = 0;
    for (int i = -1; i <= 1; i++)
        for (int j = -1; j <= 1; j++)
            if (x + i >= 0 && x + i < n && y + j >= 0 && y + j < m && get(mask, x + i, y + j))
                cnt++;
    return cnt;
}

bool ok(li mask, int& fi, int& fj)
{
    int cc = 0;
    forn(i, n)
        forn(j, m)
            if (get(mask, i, j))
                cc++;
            else
                fi = i, fj = j;

    if (cc  == n * m - 1)
        return true;

    fi = -1, fj = -1;
    forn(i, n)
        forn(j, m)
            if (cnt(mask, i, j) == 0)
                fi = i, fj = j;
    li u = 0;
    put(u, fi, fj);
    queue<pair<int,int> > q;
    q.push(make_pair(fi, fj));
    while (!q.empty())
    {
        pair<int,int> s = q.front();
        q.pop();

        for (int i = -1; i <= 1; i++)
            for (int j = -1; j <= 1; j++)
            {
                int ni = s.first + i;
                int nj = s.second + j;
                if (ni >= 0 && ni < n && nj >= 0 && nj < m && !get(u, ni, nj) && cnt(mask, ni, nj) == 0)
                {
                    q.push(make_pair(ni, nj));
                    put(u, ni, nj);
                }
            }
    }

    forn(i, n)
        forn(j, m)
        {
            if (get(mask, i, j))
                continue;
            int c = cnt(mask, i, j);
            if (c == 0 && !get(u, i, j))
                return false;
            if (c == 0 && get(u, i, j))
                continue;
            bool ok = false;
            for (int dx = -1; dx <= 1; dx++)
                for (int dy = -1; dy <= 1; dy++)
                    if (i + dx >= 0 && i + dx < n && j + dy >= 0 && j + dy < m && get(u, i + dx, j + dy))
                        ok = true;
            if (!ok)
                return false;
        }

    return true;
}

int main(int argc, char* argv[])
{
    int tt;
    cin >> tt;

    forn(tx, tt)
    {
        int k;
        cin >> n >> m >> k;
        bool good = false;
        cout << "Case #" << (tx + 1) << ":" << endl;

        forn(mask, 1 << (n * m))
        {
            int c = 0;
            forn(j, n * m)
                if (mask & (1 << j))
                    c++;
            int fi, fj;
            if (c == k && ok(mask, fi, fj))
            {
                forn(i, n)
                {
                    forn(j, m)
                    {
                        if (i == fi && j == fj)
                            cout << "c";
                        else if (get(mask, i, j))
                            cout << "*";
                        else
                            cout << ".";
                    }
                    cout << endl;
                }
                good = true;
                break;
            }
        }

        if (!good)
            cout << "Impossible" << endl;
    }
}

