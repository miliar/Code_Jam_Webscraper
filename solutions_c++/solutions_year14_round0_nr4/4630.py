#include <cstdio>
#include <algorithm>

using namespace std;

double t1[1005], t2[1005], w1[1005], w2[1005];

int main ()
{
    int z,a,b,c,d,e,n,wyn,wyn2;

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        scanf ("%d", &n);

        for (b=0; b<n; b++)
            scanf ("%lf", &t1[b]);

        for (b=0; b<n; b++)
            scanf ("%lf", &t2[b]);

        sort(t1,t1+n);
        sort(t2,t2+n);

        for (b=0; b<n; b++)
            w1[b]=t1[b];

        for (b=0; b<n; b++)
            w2[b]=t2[b];

        wyn=wyn2=0;

        for (b=0; b<n; b++)
        {
            for (c=0; c<n && t2[c]<t1[b]; c++);

            if (c==n)
                wyn++;
            else
                t2[c]=0;
        }

        b=c=0;
        e=n-1;

        while (b < n)
        {
            if (w1[b]>w2[c])
            {
                c++;
                wyn2++;
            }

            b++;
        }

        printf ("Case #%d: %d %d\n", a, wyn2, wyn);
    }

    return 0;
}
