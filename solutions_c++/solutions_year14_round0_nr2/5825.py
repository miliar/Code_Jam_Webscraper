#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>

using namespace std;

double  C, F, X;
int T;

double calc()
{
    double rate = 2.0;
    double ans = X / rate;
    double cur = 0.0;
    while (true) {
        cur += C / rate;
        rate += F;
        double time = cur + X / rate;
        if (time < ans) {
            ans = time;
        }
        else break;
    }
    return ans;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large-out.txt", "w", stdout);
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        scanf("%lf%lf%lf", &C, &F, &X);
        printf("%.7lf\n", calc());
    }
    return 0;
}