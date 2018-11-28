#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
using namespace std;


typedef long long LL;
#define INF 0x3f3f3f3f
#define eps 1e-8
#define lson (pos << 1)
#define rson (pos << 1 | 1)

template<class T> void checkMax(T &a, T b){a = max(a, b);}
template<class T> void checkMin(T &a, T b){a = min(a, b);}

int main()
{
    freopen("B-small-attempt2.in", "r", stdin);
    freopen("B-small-attempt2.out", "w", stdout);
    int t, cas = 1, i, j;
    double C, F, X;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%lf%lf%lf", &C, &F, &X);
        double cur = 0, rate = 2;
        double ans = X / rate;
        while(1)
        {
            cur += C / rate;
            rate += F;
            if(cur + X / rate + eps < ans)
                ans = cur + X / rate;
            else
                break;
            //checkMin(ans, cur + X / rate);
        }
        printf("Case #%d: %.7lf\n", cas++, ans);
    }
    return 0;
}
