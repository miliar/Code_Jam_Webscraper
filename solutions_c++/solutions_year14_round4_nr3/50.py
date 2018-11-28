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

#define y1 y111

using namespace std;

const long long INF = 1LL << 60LL;

int X, Y, n;
vector<long long> x1, x2, y1, y2;

long long dist(int i, int j)
{   
    if (i == j)
        return 0;

    long long best = INF;

    {
        long long a = max(x1[i], x1[j]);
        long long b = min(x2[i], x2[j]);
        if (a <= b)
            best = min(best, min(min(abs(y1[i] - y1[j]), abs(y1[i] - y2[j])), min(abs(y2[i] - y1[j]), abs(y2[i] - y2[j]))) - 1);
    }

    {
        long long a = max(y1[i], y1[j]);
        long long b = min(y2[i], y2[j]);
        if (a <= b)
            best = min(best, min(min(abs(x1[i] - x1[j]), abs(x1[i] - x2[j])), min(abs(x2[i] - x1[j]), abs(x2[i] - x2[j]))) - 1);
    }

    long long xx[4] = {x1[i], x2[i], x1[j], x2[j]};
    long long yy[4] = {y1[i], y2[i], y1[j], y2[j]};

    forn(i1, 2)
        forn(j1, 2)
            for (int i2 = 2; i2 < 4; i2++)
                for (int j2 = 2; j2 < 4; j2++)
                    best = min(
                        best,
                        max(abs(xx[i1] - xx[i2]), abs(yy[j1] - yy[j2])) - 1
                    );

    return best;
}

int main(int argc, char* argv[])
{
    int tt;
    cin >> tt;

    forn(tx, tt)
    {
        assert(cin >> X >> Y >> n);
        x1 = x2 = y1 = y2 = vector<long long>(n + 2);
        forn(i, n)
            assert(cin >> x1[i] >> y1[i] >> x2[i] >> y2[i]);

        x1[n] = -1;
        x2[n] = -1;
        y1[n] = 0;
        y2[n] = Y - 1;

        x1[n + 1] = X;
        x2[n + 1] = X;
        y1[n + 1] = 0;
        y2[n + 1] = Y - 1;

        n += 2;

        vector<long long> d(n, INF);
        d[n - 2] = 0;
        vector<bool> used(n);

        while (true)
        {
            int minp = -1;
            long long mind = INF;
            forn(i, n)
                if (d[i] < mind && !used[i])
                {
                    mind = d[i];
                    minp = i;
                }

            if (mind == INF || minp == -1)
                break;

            used[minp] = true;
            forn(i, n)
            {
                long long dd = d[minp] + dist(minp, i);
                if (dd < d[i])
                    d[i] = dd;
            }
        }

        cout << "Case #" << (tx + 1) << ": " << d[n - 1] << endl;
    }
}
