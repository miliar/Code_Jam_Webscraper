#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>

#define inf 1000000000

using namespace std;

double min(double a, double b)
{
    if (a > b) return b;
    else return a;
}

double c, f, x, ans1, ans2, ans3, ans, ans4;

double calc(int n)
{
    if (n < -1) return inf;
    double tmp = 0;
    for (int i = 0; i <= n; i++) {
        tmp = tmp + c/(2+i*f);
    }
    tmp = tmp + x/(2 + f + n * f);
    return tmp;
}

int main()
{
    int testcase, n1;
    freopen("cookieL.in", "r", stdin);
    freopen("cookieL.out", "w", stdout);
    scanf("%d", &testcase);
    for (int test = 1; test <= testcase; test++) {
        scanf("%lf%lf%lf", &c, &f, &x);
        n1 = int((f * (x - c) - 2 * c) / (f * c));
        if (n1 < 0) n1 = -1;
        ans1 = calc(n1);
        ans2 = calc(n1+1);
        ans3 = calc(n1+2);
        ans4 = calc(n1-1);
        ans = min(ans1, ans2);
        ans = min(ans, ans3);
        ans = min(ans, ans4);
        printf("Case #%d: ", test);
        printf("%.7lf\n", ans);
    }
    return 0;
}
