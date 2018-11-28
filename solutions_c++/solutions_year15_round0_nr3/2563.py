#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;

int w[5][5];
int t[10005];

int coto(char x)
{
    if (x=='1')
        return 1;

    if (x=='i')
        return 2;

    if (x=='j')
        return 3;

    return 4;
}

int pal (int x, int y)
{
    if (x<0)
        return -w[-x][y];

    return w[x][y];
}

int main ()
{
    int a,b,c,d,e,f,g,n,z,co1,co2,co3;
    char x;

    w[1][1]=1;
    w[1][2]=2;
    w[1][3]=3;
    w[1][4]=4;
    w[2][1]=2;
    w[2][2]=-1;
    w[2][3]=4;
    w[2][4]=-3;
    w[3][1]=3;
    w[3][2]=-4;
    w[3][3]=-1;
    w[3][4]=2;
    w[4][1]=4;
    w[4][2]=3;
    w[4][3]=-2;
    w[4][4]=-1;

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        scanf ("%d %d\n", &b, &c);

        for (d=0; d<b; d++)
        {
            x=getchar();
            t[d]=coto(x);
        }

        for (d=b; d<b*c; d++)
            t[d]=t[d-b];

        co1=t[0];

        for (d=1; d<b*c; d++)
        {
            if (co1!=2)
            {
                co1=pal(co1,t[d]);
                continue;
            }

            co2=1;

            for (e=d; e<b*c; e++)
            {
                if (co2!=3)
                {
                    co2=pal(co2,t[e]);
                    continue;
                }

                co3=1;

                for (f=e; f<b*c; f++)
                    co3=pal(co3,t[f]);

                if (co3==4)
                {
                    printf ("Case #%d: YES\n", a);
                    break;
                }

                co2=w[co2][t[e]];
            }

            if (e<b*c)
                break;

            co1=w[co1][t[d]];
        }

        if (d==b*c)
            printf ("Case #%d: NO\n", a);
    }

    return 0;
}
