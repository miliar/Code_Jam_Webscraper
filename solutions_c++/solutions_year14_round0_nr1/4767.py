#include <cstdio>
#include <algorithm>

using namespace std;

int t1[4][4], t2[4][4];

int main ()
{
    int z,a,b,c,d,n,m;

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        scanf ("%d", &n);
        n--;

        for (b=0; b<4; b++)
            for (c=0; c<4; c++)
                scanf ("%d", &t1[b][c]);

        scanf ("%d", &m);
        m--;

        for (b=0; b<4; b++)
            for (c=0; c<4; c++)
                scanf ("%d", &t2[b][c]);

        d=0;

        for (b=1; b<=16; b++)
            if (t1[n][0]==b || t1[n][1]==b || t1[n][2]==b || t1[n][3]==b)
                if (t2[m][0]==b || t2[m][1]==b || t2[m][2]==b || t2[m][3]==b)
                {
                    if (d == 0)
                        d = b;
                    else
                        break;
                }

        if (b==17 && d == 0)
            printf ("Case #%d: Volunteer cheated!\n", a);

        if (b == 17 && d)
            printf ("Case #%d: %d\n", a, d);

        if (b < 17)
            printf ("Case #%d: Bad magician!\n", a);
    }

    return 0;
}
