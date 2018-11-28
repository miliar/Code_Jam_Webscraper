#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <functional>
#include <queue>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
using namespace std;

const int N = 1000100;
const int INF = 1000000000;
const double eps = 1e-8;


void solve()
{
    double c, f, x;
    scanf("%lf%lf%lf", &c, &f, &x);
    double ans = x/2.0, now=0, na=2;
    while(now<ans)
    {
        ans = min(ans, now+x/na);
        now += c/na;
        na += f;
    }
    printf("%.7f\n", ans);
}

int main()
{
    freopen("in_.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d", &t);
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
