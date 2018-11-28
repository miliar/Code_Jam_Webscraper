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

typedef long double ld;
const ld EPS = 1E-11;

using namespace std;

int n;
ld V, C;
ld r[1000], c[1000];
ld v[1000];

bool can(ld t)
{
    ld sum = 0;
    forn(i, n)
        v[i] = r[i] * t,
        sum += v[i];
    if (sum + EPS < V)
        return false;
    
    vector<pair<ld,ld> > p;
    forn(i, n)
        p.push_back(make_pair(c[i], v[i]));    
    sort(p.begin(), p.end());

    ld left = V;
    sum = 0;

    forn(i, n)
    {
        if (left > EPS)
        {
            ld d = min(left, p[i].second);
            sum += d * p[i].first;
            left -= d;
        }
    }

    ld minc = sum / V;

    left = V;
    sum = 0;

    for (int i = n - 1; i >= 0; i--)
    {
        if (left > EPS)
        {
            ld d = min(left, p[i].second);
            sum += d * p[i].first;
            left -= d;
        }
    }

    ld maxc = sum / V;

    return minc <= C + EPS && C <= maxc + EPS;
}

int main(int argc, char* argv[])
{
    int tt;
    cin >> tt;

    forn(test, tt)
    {
        cin >> n >> V >> C;
        forn(i, n)
            cin >> r[i] >> c[i];

        bool t[3] = {0, 0, 0};
        forn(i, n)
        {
            if (c[i] + 1E-10 < C)
                t[0] = true;
            if (fabsl(c[i] - C) < 1E-10)
                t[1] = true;
            if (c[i] > C + 1E-10)
                t[2] = true;
        }

        ld lf = 0.0;
        ld rg = 1E25;

        if (!((!t[0] && !t[1]) || (!t[1] && !t[2])))
        {
            forn(tx, 400)
            {
                ld mid = (lf + rg) / 2.0;
                if (can(mid))
                    rg = mid;
                else
                    lf = mid;
            }
        }
        else
            cerr << "*" << endl;

        if (rg > 1E20)
            cout << "Case #" << (test + 1) << ": IMPOSSIBLE" << endl;
        else
        {
            printf("Case #%d: %.10f\n", test + 1, double((lf + rg) / 2.0));
        }
    }

    return 0;
}
