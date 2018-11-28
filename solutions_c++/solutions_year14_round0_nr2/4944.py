#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    //freopen("1.txt", "r", stdin);
    //freopen("2.txt", "w", stdout);
    int cases;
    double C, F, X;
    cin >> cases;
    for (int t = 1; t <= cases; t++)
    {
        cin >> C >> F >> X;
        double r = 2.0;
        double ret = 0.0;
        while(C * (r+F) <= F * X)
        {
            ret += C / r;
            r += F;
        }

        ret += X / r;
        printf("Case #%d: %.7lf\n", t, ret);
    }
    return 0;
}
