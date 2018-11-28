#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <set>
#include <iostream>

using namespace std;

#define MAX 5
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define eps 1e-9

typedef long long LL;

double GetValue(int len, double C, double F, double X) {
    double sum = 0;
    for (int i = 0; i < len; ++i) {
        sum += C / (2 + F * i);
    }
    sum += X / (2 + len * F);

    return sum;
}

int main(void) {
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B.out", "w", stdout);
    int nCase;
    while (~scanf("%d", &nCase)) {
        for (int cas = 1; cas <= nCase; ++cas) {
            double C;
            double F;
            double X;
            scanf("%lf%lf%lf", &C, &F, &X);

            int lt = 0;
            int rt = (int)X;
            int mid;
            int mid2;
            double mn = X / 2;
            double ans;
            double ans2;
            while (lt <= rt) {
                mid = (lt + rt) / 2;
                mid2 = (lt + mid) / 2;
                ans = GetValue(mid, C, F, X);
                ans2 = GetValue(mid2, C, F, X);
                if (ans2 >= ans) {
                    lt = mid2 + 1;
                    mn = min(mn, ans);
                } else {
                    rt = mid - 1;
                    mn = min(mn, ans2);
                }
            }
            /*
            for (int i = 0; i <= rt; ++i) {
                mn = min(mn, GetValue(i, C, F, X));
            }*/
            
            printf("Case #%d: %.7lf\n", cas, mn);
        }
    }
    return 0;
}