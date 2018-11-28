#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;

int main ()
{
    int a,b,c,d,n,z;
    char x;

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        scanf ("%d ", &n);
        b=0;
        c=0;

        for (d=0; d<=n; d++)
        {
            x=getchar();

            if (b<d)
            {
                c++;
                b++;
            }

            b+=x-'0';
        }

        printf ("Case #%d: %d\n", a, c);
    }

    return 0;
}
