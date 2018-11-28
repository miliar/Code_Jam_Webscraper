#include <stdio.h>
#include <cstdlib>
#include <string.h>

const int n = 4;

using namespace std;

int a[n][n], b[n][n];
int v[20];

long double get(long double c, long double x, long double f, int i)
{
            long double mans = 0;
            for (int j = 0; j < i; ++j)
                mans += c / (2 + f * j);
            mans += x / (2 + f * i);
            return mans;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int qw = 0; qw < t; ++qw)
    {
        printf("Case #%d: ", qw + 1);
        fprintf(stderr, "Case #%d\n", qw + 1);
        long double c, f, x;
        scanf("%Lf%Lf%Lf", &c, &f, &x);
        long double ans = 1e100;
        
        int l = 0;
        int r = 1000000;
        for (int i = 0; i < 100; ++i)
        {
            int lt = l +  (r - l) / 3;
            int rt = r - (r - l) / 3;
            if (get(c, x, f, lt) < get(c, x, f, rt))
                r = rt;
            else
                l = lt;
        }
        if (l < 0)
            l = 0;
        for (int i = l; i < r + 10; ++i)
        {
            long double mans = 0;
            for (int j = 0; j < i; ++j)
                mans += c / (2 + f * j);
            mans += x / (2 + f * i);
            if (mans < ans)
                ans = mans;
            else
                break;
        }
        printf("%.10Lf\n", ans);
    }
}
