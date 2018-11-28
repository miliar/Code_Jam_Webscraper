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

int n, a[2005];

int next(int ind)
{
    int next_ind = ind + 1;
    while(next_ind < 2 * n + 2 and a[ind] != a[next_ind]) next_ind++;
    return next_ind;
}

int get(int p)
{
    int res = 0;
    int x = next(p), y = next(1 - p);
    while(x < 2 * n + 2)
    {
        if(x > y)
        {
            res++;
            y = next(y);
        }
        x = next(x);
    }
    return res;
}

int main()
{
    freopen("D-large.in", "r", stdin);
    //freopen("D.out", "w", stdout);
    int t;
    cin >> t;
    FOR(ti, 1, t + 1)
    {
        cin >> n;
        vector< pair<double, int> > v(2 * n);
        FOR(i, 0, 2 * n)
        {
            cin >> v[i].first;
            v[i].second = i / n;
        }
        sort(v.begin(), v.end());
        FOR(i, 0, 2 * n) a[i + 2] = v[i].second;
        a[0] = 0;
        a[1] = 1;
        a[2 * n + 2] = 0;
        a[2 * n + 3] = 1;
        printf("Case #%d: %d %d\n", ti, get(0), n - get(1));
    }
}

