#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <memory.h>
#include <ctime>
#include <cmath>

using namespace std;

void solve()
{
    double c, f, x;
    scanf("%lf%lf%lf", &c, &f, &x);
    double ans = x / 2.;
    double cur_time = 0.;
    for (int i = 0; cur_time <= ans; ++i)
    {
        ans = min(ans, cur_time + x / (2. + double(i) * f));
        cur_time += c / (2. + double(i) * f);
    }
    cout << fixed << setprecision(10) << ans << endl;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
    {
        printf("case #%d: ", i + 1);
        solve();
    }
    return 0;
}
