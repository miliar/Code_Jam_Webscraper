#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

double C, F, X;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;

    scanf("%d", &T);
    for(int cse = 1; cse <= T; cse++){
        scanf("%lf%lf%lf", &C, &F, &X);
        int t =(int) (max(0., (X * F - 2 * C) / (C * F)) + 1e-6);
        //printf("%d\n", t);
        double ans = 0.;
        for(int i = 1; i <= t; i++)
            ans += (double)C / ((i - 1) * F + 2);
        ans += X / (t * F + 2);
        printf("Case #%d: %.7f\n", cse, ans);
    }
    return 0;
}
