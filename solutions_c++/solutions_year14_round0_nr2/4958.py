#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

int main()
{
//    freopen("in.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
//    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);

    double C, F, X;

    while (t--){
        scanf(" %lf %lf %lf", &C, &F, &X);
        double speed = 2.0;
        double ans = 0;

        while (1){
            double no_buy = X/speed;
            double buy = C/speed + X/(speed+F);

            if (no_buy <= buy){
                ans += no_buy;
                break;
            }

            ans += C/speed;
            speed += F;
        }

        printf("Case #%d: %.7lf\n", ++cas, ans);
    }

    return 0;
}
