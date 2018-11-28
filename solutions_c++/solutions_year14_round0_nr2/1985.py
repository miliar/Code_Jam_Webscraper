#include <bits/stdc++.h>
#define inf 1 << 29
#define eps .0000000000001

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, caseno = 0;
    scanf("%d", &t);
    while(t--)
    {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        double presult = (x / 2.0) + eps, sum, result = presult;
        double prev = 2;
        for(double i = 2 + f; ; i = i + f)
        {
            sum = presult - (((x - c) / prev) + eps) + ((x /  i) + eps) + eps;
            prev = i;
            presult = sum;
            if(presult < result) result = presult;
            else break;
        }
        printf("Case #%d: %.7lf\n", ++caseno, result);
    }
    return 0;

}
