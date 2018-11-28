#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <vector>

#define f first
#define s second
#define pb push_back

using namespace std;

double C , F , X;

int main()
{
    freopen("input-l.in","r",stdin);
    freopen("output.out","w",stdout);

    int t , k;

    scanf("%d",&t);

    for (int k = 1; k <= t; k++) {
        double rate = 2.0 , res = 0.0 , res2 = 0.0 , res3 = 0.0;

        scanf("%lf %lf %lf",&C,&F,&X);
        while (X > 0.0) {
            if (C / rate + X / (rate + F) >= X / (rate)) {
                res += X / rate;
                break;
            }
            res += C / rate;
            rate += F;
        }
        printf("Case #%d: %.7lf\n",k,res);
    }

    return 0;
}
