#include<algorithm>
#include<iostream>
#include<cstring>
#include<vector>
#include<cstdio>
#include<cmath>
#include<queue>
#include<stack>
#include<map>
#include<set>
#define LL long long
#define CLR(a, b) memset(a, b, sizeof(a))
using namespace std;

const int maxn = 200;
const int INF = 0x3f3f3f3f;
const double eps = 1e-8;

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    double c, f, x, p, ans;
    int T, cas = 1;
    scanf("%d", &T);
    while(T --)
    {
        scanf("%lf%lf%lf", &c, &f, &x);
        p = 2.0;
        ans = 0.0;
        while(x / p - (x / (p + f) + c / p) > eps)
        {
            ans += c / p;
            p += f;
        }
        ans += x / p;
        printf("Case #%d: %.7f\n", cas ++, ans);
    }
}
