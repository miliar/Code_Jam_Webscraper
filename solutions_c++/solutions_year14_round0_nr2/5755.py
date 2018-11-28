#include <cstdio>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <climits>
#include <cmath>
#include <queue>
#include <vector>
#include <stack>
#include <set>
#include <map>
#define INF 0x3f3f3f3f
#define eps 1e-8
using namespace std;

int main()
{
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int T = 1; T <= cas; T ++)
    {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        double ans = x;
        for (int lim = 0; lim <= ceil(x); lim ++)
        {
            double sum = 0.0, rate = 2.0, time = 0.0;
            for (int i = 0; i < lim; i ++)
            {
                time += c / rate;
                rate += f;
            }
            ans = min(ans, time + x / rate);
        }
        printf("Case #%d: %.7f\n", T, ans);
    }
    return 0;
}
