#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
#define rep(i,a,b) for (int i = a; i <= b; ++i)
using namespace std;

const double eps = 1e-8;

int main(){
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    int T, cas(0);
    scanf("%d", &T);
    while (T--)
    {
        double C, F, X, ans(1e20);
        scanf("%lf%lf%lf", &C, &F, &X);
        double ps(2.0), farmt(0);
        while (true)
        {
            if (ans > farmt + X / ps + eps)
                ans = farmt + X / ps;
            else
                break;
            farmt += C/ps;
            ps += F;
        }
        printf("Case #%d: %.7lf\n", ++cas, ans);
    }
    return 0;
}
