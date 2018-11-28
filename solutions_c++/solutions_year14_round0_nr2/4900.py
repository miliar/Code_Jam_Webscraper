#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <fstream>
using namespace std;
int cases;
double e = 0.0000001;
int main() {
    freopen("B-small-attempt.in", "r", stdin);
    freopen("B.out", "w", stdout);
    scanf("%d", &cases);
    for(int t = 1; t <= cases; t++)
    {
        double c, f, x, ans, v = 2.0, ost = 0;
        bool ok = 0;
        scanf("%lf%lf%lf", &c, &f, &x);
        ans = x/2;
        while(x-v>=e || ok)
        {
            ost += c/v;
            v+=f;
            double tm = x/v + ost;
            //cout<<v<<" "<<tm<<endl;
            if(ans-tm>=e) ans = tm, ok=1;
            else ok=0;
        }
        printf("Case #%d: %.7lf\n", t, ans);
    }
    return 0;
}
