#define _USE_MATH_DEFINES
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cmath>
#include <queue>
#include <functional>
#include <cstdio>
#include <cassert>
#include <stack>

#define mp make_pair
#define mt(x,y,z) mp((x), mp((y), (z)))
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;

// globals starts here

const double EPS = 1e-8;
const int MAX_N = 105;
int n;
double v, x;
double R[MAX_N];
double C[MAX_N];

pair<double, double> solve()
{
    if (n == 1)
    {
        if (abs(C[0] - x) < EPS)
        {
            return mp(v / R[0], 0);
        }
        return mp(-1,-1);
    }

    if ((C[0] < x && C[1] < x) || (C[0] > x && C[1] > x))
    {
        return mp(-1, -1);
    }

    if (abs(C[0] - C[1]) < EPS)
    {
        return mp(v / (R[0] + R[1]), v / (R[0] + R[1]));
    }

    if (abs(C[0] - x) < EPS)
    {
        return mp(v / R[0], 0);
    }

    if (abs(C[1] - x) < EPS)
    {
        return mp(0, v / R[1]);
    }

    double c = R[1] * C[1] - R[1] * C[0];
    double d = x * v - v * C[0];
    double t1 = d / c;

    double t0 = (v - R[1] * t1) / R[0];

    return mp(t0, t1);
}

int main()
{
#ifdef DEBUGAGA
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#elif defined(CONTEST)
    freopen(CONTEST ".in", "r", stdin);
    freopen(CONTEST ".out", "w", stdout);
#endif

    int tests;
    cin >> tests;
    for (int tc = 1; tc <= tests; ++tc)
    {
        cin >> n;
        cin >> v >> x;
        for (int i = 0; i < n; ++i)
        {
            cin >> R[i] >> C[i];
        }

        pair<double,double> sol = solve();

        if (sol.first != -1)
        {
            if (n == 1)
            {
                if (sol.first * R[0] != v)
                {
                    return 1;
                }
                if (C[0] != x)
                {
                    return 1;
                }
            }
            if (n == 2)
            {
                double vact = sol.first * R[0] + sol.second * R[1];
                if (abs(vact - v) > EPS)
                {
                    return 1;
                }
                double xact = (sol.first * R[0] * C[0] + sol.second * R[1] * C[1]) / vact;
                if (abs(xact - x) > EPS)
                {
                    return 1;
                }
            }
        }

        if (sol.first == -1)
        {
            printf("Case #%d: IMPOSSIBLE\n", tc);
        }
        else
        {
            printf("Case #%d: %.8lf\n", tc, max(sol.first, sol.second));
        }
    }

    return 0;
}