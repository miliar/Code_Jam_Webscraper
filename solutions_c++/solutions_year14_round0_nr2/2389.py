#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const double eps = 1e-9;
int t;
double C, F, X;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int ic = 1;
    scanf("%d", &t);
    while ( t-- )
    {
        scanf("%lf%lf%lf", &C, &F, &X);
        double S = 2.0, itm = 0.0;
        while (1)
        {
            if ( C/S + X/(S+F) - X/S < eps ) {
                itm += C/S;
                S += F;
            }
            else break;
        }
        itm += (X/S);
        printf("Case #%d: %.7lf\n", ic++, itm);
    }
}
