#include <cstdio>
#include <algorithm>
#include <set>
#include <string>
#include <iostream>
using namespace std;

int w[5005];

bool mn(int a, int b)
{
    if (a==1)
        return (b!=1);

    if (a==0)
        return (b==2);

    return 0;
}

int main ()
{
    int a,b,c,d,e,f,g,z,n;
    int t[3],tmp[3];

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        scanf ("%d%d%d%d", &n, &t[0], &t[1], &t[2]);
        d=1<<n;

        for (c=0; c<3; c++)
            if (t[c]<d/3 || (d==2 && t[c]==2) || t[c]>d/3+1)
                break;

        if (c<3)
        {
            printf ("Case #%d: IMPOSSIBLE\n", a);
            continue;
        }

        for (b=d; b>2; b/=2)
        {
            tmp[0]=(t[0]+t[1]-t[2])/2;
            tmp[1]=t[1]-tmp[0];
            tmp[2]=t[2]-tmp[1];
            t[0]=tmp[0];
            t[1]=tmp[1];
            t[2]=tmp[2];
        }

        if (t[0] && t[1])
        {
            w[0]=1;
            w[d/2]=0;
        }

        if (t[0] && t[2])
        {
            w[0]=0;
            w[d/2]=2;
        }

        if (t[1] && t[2])
        {
            w[0]=1;
            w[d/2]=2;
        }

        for (b=d/4; b>0; b/=2)
        {
            for (c=b; c<d; c+=2*b)
                w[c]=(w[c-b]+1)%3;
        }

        for (b=1; b<d; b*=2)
        {
            for (c=0; c+b<d; c+=2*b)
            {
                for (e=c; e<c+b; e++)
                    if (mn(w[e+b],w[e]))
                        break;

                if (e<c+b)
                {
                    for (e=c; e<c+b; e++)
                        swap(w[e],w[e+b]);
                }
            }
        }

        printf ("Case #%d: ", a);

        for (b=0; b<d; b++)
        {
            if (w[b]==0)
                printf ("R");

            if (w[b]==1)
                printf ("P");

            if (w[b]==2)
                printf ("S");
        }

        printf ("\n");
    }

    return 0;
}
