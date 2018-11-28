#include <cstdio>
#include <deque>
#include <queue>
#include <vector>
#include <string>
#include <set>
#include <stack>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <climits>
#include <cfloat>
#include <map>
#include <cstring>
#include <ctime>
#include <cassert>

#define MOD 1000000007
#define EPS 1e-9
#define INF 2117117117
#define LLINF 2117117117117117117LL
#define mp(a, b) make_pair(a, b)
#define pb(a) push_back(a)
#define sqr(a) ((a) * (a))
#define sz(a) ((int) (a).size())

#define uNEG (ulong) -1
#ifndef M_PI
const double M_PI = acos(-1.0);
#endif

typedef unsigned int uint;
typedef long long llong;
typedef long double ldouble;
typedef unsigned long long ullong;

#define TASK "task"

using namespace std;

int q;
ldouble s, c, f, x, ans, cur;

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    //freopen(TASK".in", "r", stdin);
    //freopen(TASK".out", "w", stdout);

    //init + input
    scanf("%d", &q);

    //proc each test
    for (int qq = 0; qq < q; qq++)
    {
        cin >> c >> f >> x;
        ans = x / 2;
        s = 0;
        for (int i = 0; i < 1000117; i++)
        {
            cur = s + x / (2 + f * i);
            ans = min(cur, ans);
            s += c / (2 + f * i);
        }
        cout << "Case #" << (qq + 1) << ": " << fixed << setprecision(7) << ans << '\n';
    }

    return 0;
}
