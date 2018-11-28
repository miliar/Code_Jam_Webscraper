#include <iostream>
#include <fstream>
#include <cstdio>
#include <sstream>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <iomanip>
#include <cstring>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define TR(i, a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)

double c, f, x;

double solve()
{
    double res = 1e10, v = 2.0, sum = 0.0;
    FOR(i, 0, 1111111)
    {
        res = min(res, sum + x / v);
        sum += c / v;
        v += f;
    }
    return res;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int t;
    cin >> t;
    FOR(ti, 1, t + 1)
    {
        cin >> c >> f >> x;
        printf("Case #%d: ", ti);
        cout << fixed << setprecision(15) << solve() << endl;
    }
}

