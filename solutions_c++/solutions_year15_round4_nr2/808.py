#include <iostream>
#include <string.h>
#include <stdio.h>
#include <cmath>
using namespace std;
double r[2],t[2];

int cmp(double a, double b)
{
    double eps = 1e-10;
    if (abs(a-b)< 1e-10)    return 0;
    else return 1;
}
int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B.out","w",stdout);
    int times;
    cin >> times;
    for (int ti = 1; ti <= times ; ti ++)
    {
        int n;
        cin >> n;
        double vt,tt;
        cin >> vt >> tt;
        for (int i = 0; i < n; i ++)
        {
            scanf("%lf %lf",&r[i],&t[i]);
        }
        if (n == 1)
        {
            if (cmp(t[0],tt)) printf("Case #%d: IMPOSSIBLE\n",ti);
            else printf("Case #%d: %.8lf\n",ti,vt/r[0]);
        }
        if (n == 2)
        {
            if (t[0] > t[1])
            {
                swap(t[0],t[1]);
                swap(r[0],r[1]);
            }
            if ((cmp(t[0],tt) == 0) && cmp(t[0],tt)) printf("Case #%d: IMPOSSIBLE\n",ti);
            else if (tt < t[0] || tt > t[1]) printf("Case #%d: IMPOSSIBLE\n",ti);
            else{
                if (t[0] == t[1])
                {
                    printf("Case #%d: %.8lf\n",ti,vt/(r[0]+r[1]));
                    continue;
                }
                double x = (vt*tt - vt*t[1])/(r[0]*(t[1]-t[0]));
                x = abs(x);
                double y = (vt - r[0]*x) / r[1];

                y = abs(y);
                double ans = max(x,y);
                printf("Case #%d: %.8lf\n",ti,ans);
            }
        }
    }
}
