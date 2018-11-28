#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

const double eps = 1e-7;
int dcmp(double x) {if (fabs(x) < eps) return 0; return x < 0 ? -1 : 1;}
double C, F, X;

double solve(int n)
{
    double ret = X/(2.0+n*F);
    for (int i=0;i<n;i++) ret += C/(2.0+i*F);
    return ret;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T, cas = 1;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%lf%lf%lf", &C, &F, &X);
        printf("Case #%d: ", cas++);
        if (dcmp(C-X) >= 0)
        {
            printf("%.7lf\n", X/2.0);
            continue;
        }
        int n = (F*X/C - 2.0 - F) / F;
        printf("%.7lf\n", min(solve(n), solve(n+1)));
    }
    return 0;
}
