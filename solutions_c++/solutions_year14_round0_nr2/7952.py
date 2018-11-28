#include<bits/stdc++.h>
using namespace std;

int main()
{
    int testcases;
    scanf("%d", &testcases);

    for(int i=1; i<=testcases; i++)
    {
        double c, f, x;
        scanf("%lf %lf %lf", &c, &f, &x);
        double ans = (x/2.0), newans = ((c/2.0) + (x/(2.0 + f)));

        double j=1;

        while(newans<ans)
        {
            ans = newans;
            newans -= (x/(2.0 + j*f));
            newans += ((c/(2.0 + j*f)) + (x/(2.0 + (j + 1.0)*f)));
            j += 1.0;
        }

        printf("Case #%d: %lf\n", i, ans);
    }

    return 0;
}
