#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;

int main ()
{
    int a,b,d,e,f,g,n,z;
    double x,y,r1,r2,c1,c2,r,c,rati;

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        scanf ("%d%lf%lf", &n, &r, &c);
        scanf ("%lf%lf", &r1, &c1);

        if (n==1)
        {
            if (c1!=c)
            {
                printf ("Case #%d: IMPOSSIBLE\n", a);
                continue;
            }

            printf ("Case #%d: %lf\n", a, r/r1);
        }
        else
        {
            scanf ("%lf%lf", &r2, &c2);

            if (c<c1 && c<c2)
            {
                printf ("Case #%d: IMPOSSIBLE\n", a);
                continue;
            }

            if (c>c1 && c>c2)
            {
                printf ("Case #%d: IMPOSSIBLE\n", a);
                continue;
            }

            if (c1==c2)
            {
                printf ("Case #%d: %lf\n", a, r/(r1+r2));
                continue;
            }

            if (c==c1)
            {
                printf ("Case #%d: %lf\n", a, r/(r1));
                continue;
            }

            if (c==c2)
            {
                printf ("Case #%d: %lf\n", a, r/(r2));
                continue;
            }

            if (c2<c1)
            {
                swap(c1,c2);
                swap(r1,r2);
            }

            rati=(c-c1)/(c2-c1);

            if ((r*rati)/r2 < r*(1.0-rati)/r1)
                printf ("Case #%d: %lf\n", a, r*(1.0-rati)/r1);
            else
                printf ("Case #%d: %lf\n", a, r*rati/r2);
        }
    }

    return 0;
}
