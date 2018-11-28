#include <cstdio>
#include <algorithm>

using namespace std;

int t[1005][2], kol[1005];

int main ()
{
    int a,b,c,d,z,n,x,w,mam;

    scanf ("%d", &z);

    for (a=1; a<=z; a++)
    {
        scanf ("%d", &n);
        w=0;
        mam=n-1;

        for (b=0; b<n; b++)
        {
            scanf ("%d", &t[b][0]);
            t[b][1]=b;
            kol[b]=t[b][0];
        }

        sort(kol,kol+n);

        for (b=0; b<n; b++)
        {
            for (c=0; t[c][0]!=kol[b]; c++);

            w+=min(t[c][1],mam-t[c][1]);

            for (d=0; d<=mam; d++)
                if (t[d][1]>t[c][1])
                    t[d][1]--;

            t[c][0]=t[mam][0];
            t[c][1]=t[mam][1];
            mam--;
        }

        printf ("Case #%d: %d\n", a, w);
    }

    return 0;
}
