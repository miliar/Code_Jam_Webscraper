#include <cstdio>
#include <algorithm>

using namespace std;

double c,f,x;

double licz (int ile)
{
    double k,l,d,w;

    d=2;
    w=0;

    while (ile--)
    {
        w+=c/d;
        d+=f;
    }

    w+=x/d;

    return w;
}

int main ()
{
    int z,a,p,k,s;
    double m,n;

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        scanf ("%lf%lf%lf", &c, &f, &x);

        p=0;
        k=50000;

        while (p!=k)
        {
            s=(p+k)/2;

            m=licz(s);
            n=licz(s+1);

            if (m < n)
                k=s;
            else
                p=s+1;
        }

        printf ("Case #%d: %lf\n", a, licz(p));
    }

    return 0;
}
