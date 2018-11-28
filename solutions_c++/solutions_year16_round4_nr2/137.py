#pragma warning(disable:4996)

#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <vector>
using namespace std;

double p[200];
int n,k;

std::vector<double> x;

double t[200];
double s[200];

double compute()
{
    t[0] = 1;
    for (int i=0; i<k; i++)
    {
        memset(s, 0, sizeof s);
        for (int j=0; j<=i; j++)
        {
            s[j] += (1-x[i]) * t[j];
            s[j+1] += x[i] * t[j];
        }
        for (int j=0; j<=i+1; j++)
            t[j] = s[j];
    }

    return t[k/2];
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t, tt=0;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &n, &k);
        for (int i=0; i<n; i++)scanf("%lf", &p[i]);
        sort(p, p+n);

        double ans=0;
        for (int i=0; i<=k; i++)
        {
            x.clear();
            for (int j=0; j<i; j++)
                x.push_back(p[j]);

            int t=n-1;
            while (x.size() != k)
                x.push_back(p[t--]);

            double pt = compute();
            if (ans < pt)
                ans = pt;
        }
        fprintf(stderr, "%d\n", tt);
        printf("Case #%d: %.8lf\n", ++tt, ans);
    }

    return 0;
}
