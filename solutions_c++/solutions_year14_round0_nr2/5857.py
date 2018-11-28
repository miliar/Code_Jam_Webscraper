#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(void)
{
//    freopen("B-small.in", "r", stdin);
//    freopen("B-small.out", "w", stdout);

    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int tests;
    double c, f, x;

    scanf("%d", &tests);

    for (int test=1;test<=tests;++test) {
        scanf("%lf %lf %lf", &c, &f, &x);
        double cookies = 2.0, timeSpent = 0.0;
        while(true) {
            double withBuying = c / cookies + x / (cookies + f);
            if (x / cookies <= withBuying) {
                break;
            }
            timeSpent += c / cookies;
            cookies += f;
        }

        printf("Case #%d: %lf\n", test, timeSpent + x / cookies);
    }
    return 0;
}
