#include <cstdio>
#include <algorithm>
#include <set>
#include <string>
#include <iostream>
using namespace std;

double p[16],x,v;
bool mam[16], mam2[16];
int n,k;

void wal2(int nr, int ilu)
{
    if (nr==n)
    {
        if (ilu!=0)
            return;

        double y=1;

        for (int i=0; i<n; i++)
            if (mam[i])
            {
                if (mam2[i])
                    y*=p[i];
                else
                    y*=(1.0-p[i]);
            }

        v+=y;
    }
    else
    {
        if (ilu==0 || !mam[nr])
            wal2(nr+1,ilu);
        else
        {
            wal2(nr+1,ilu);
            mam2[nr]=1;
            wal2(nr+1,ilu-1);
            mam2[nr]=0;
        }
    }
}

void wal(int nr, int ilu)
{
    if (nr==n)
    {
        if (ilu!=0)
            return;

        v=0;
        wal2(0,k);
        x=max(x,v);
    }
    else
    {
        if (ilu==0)
            wal(nr+1,0);
        else
        {
            wal(nr+1,ilu);
            mam[nr]=1;
            wal(nr+1,ilu-1);
            mam[nr]=0;
        }
    }
}

int main ()
{
    int a,b,c,d,e,f,g,t;

    scanf ("%d", &t);

    for (a=1; a<=t; a++)
    {
        scanf ("%d%d", &n, &k);
        k/=2;

        for (b=0; b<n; b++)
            scanf ("%lf", &p[b]);

        x=0;
        wal(0,2*k);

        printf ("Case #%d: %.8lf\n", a,x);
    }

    return 0;
}
