#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <vector>
using namespace std;

long long pot[55];

int main ()
{
    long long t,n,a,b,c,d,e,f,p;

    pot[0]=1;

    for (a=1; a<=50; a++)
        pot[a]=(long long)2*pot[a-1];

    scanf ("%lld", &t);

    for (a=1; a<=t; a++)
    {
        scanf ("%lld %lld", &n, &p);

        b=pot[n]; //tyle musi nagrod
        c=pot[n]-1; //najw
        e=1; //tyle mniej nagord next step

        while (p<b)
        {
            b-=e;
            c/=2;
            e*=2;
        }

        if (c==pot[n]-1)
            printf ("Case #%lld: %lld ", a, c);
        else
            printf ("Case #%lld: %lld ", a, c*2);

        b=pot[n]; //tyle musi nagrod
        c=pot[n]-1; //najw
        d=1; //o tyle zleci

        while (p<b)
        {
            b/=2;
            c-=d;
            d*=2;
        }

        printf ("%lld\n", c);
    }

    getchar();
    getchar();
    return 0;
}
