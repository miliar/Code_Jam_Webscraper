#include<stdio.h>
#include<iostream>
using namespace std;

int T;
double C, F, X, ans;


void doit()
{
    double now, q;

    scanf("%lf%lf%lf", &C, &F, &X);
    ans = X/2;
    now = 0; q = 2;
    while (1)
    {
        now += C/q;
        q += F;
        if (now + X/q >= ans) break;
        ans = now + X/q;
    }
    printf("%.7lf\n", ans);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    for (int q = 1;q <= T;++q)
    {
        printf("Case #%d: ", q);
        doit();
    }
}
